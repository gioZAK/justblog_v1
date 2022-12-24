from django.urls import path
from . import views

urlpatterns = [
    path('<str:username>/', views.ProfileView.as_view(), name='profile'),
    path('account/delete/', views.DeleteAccountView.as_view(), name='delete_account'),
    path('edit/<str:username>/', views.edit_profile, name='edit')
]
