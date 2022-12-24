
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils.text import slugify
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm, PostForm
from cloudinary.uploader import upload


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


class PostLike(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'create_post.html'

    def form_valid(self, form):
        # Set the author and status of the post
        form.instance.author = self.request.user
        form.instance.status = 1
        form.instance.slug = slugify(form.instance.title)
        # Save the post and redirect to the success URL
        response = super().form_valid(form)
        messages.success(self.request, f'Post "{form.instance}" created successfully')
        return response

    def get_success_url(self):
        # Get the slug of the post that was just created
        slug = self.object.slug
        # Return the post detail page URL for the post with the given slug
        return reverse('post_detail', args=[slug])


class PostEditView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'edit_post.html'

    def get_success_url(self):
        return reverse('post_detail', args=[self.object.slug])

    def form_valid(self, form):
        # Save the post and redirect to the post detail page
        response = super().form_valid(form)
        messages.success(self.request, f'Post "{form.instance}" updated successfully')
        return response


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

    def delete(self, request, *args, **kwargs):
        # Delete the post and redirect to the home page
        response = super().delete(request, *args, **kwargs)
        messages.success(request, f'Post "{self.object}" deleted successfully')
        return response


class ProfileView(TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get the user whose profile is being viewed
        user = get_object_or_404(User, username=self.kwargs['username'])
        context['user'] = user
        context['posts'] = Post.objects.filter(author=user)
        # Check if the logged-in user is the owner of the profile
        context['is_owner'] = self.request.user == user
        return context


class DeleteAccountView(LoginRequiredMixin, TemplateView):
    template_name = 'delete_account.html'

    def post(self, request, *args, **kwargs):
        # Handle form submission
        username = request.POST['username']
        # Get the user object
        user = User.objects.get(username=username)
        # Delete the user's account
        User.objects.filter(username=username).delete()
        # Delete the user's comments
        Comment.objects.filter(name=username).delete()
        # Display a success message
        messages.success(request, f'Account "{username}" was deleted.')
        # Redirect to a home page
        return redirect('home')