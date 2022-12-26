# [justBLOG](https://justblog.herokuapp.com/)

A blog website, created as project to apply and display my current knowledge of front-end techonologies and back-end, using Django. The website, justBlog, is an open blog created to allow any user to express himself, by creating a blog post or commenting on other's user post as well, or just "surf" the blog and read content.

<img src="https://github.com/gioZAK/justblog_v1/blob/e5a81acdb151425cd63a464212242331d9aade29/docs/screenshots/amiresponsive.png">
 
[Click here](https://justblog.herokuapp.com/) to visit the deployed site.


---

# Table of contents

1. [Design](#design)
2. [UX](#ux)
3. [Agile Workflow](#agile-workflow)
4. [Structure](#structure)
5. [Features](#features)
6. [Technologies Used](#technologies-used)    
8. [Testing](#testing)
8. [Deployment](#deployment)
9. [Credits](#credits)

## Design

The main idea was to develop a website with a simple design which would not distract the user, the color scheme used allows a good contrast.

### Colors

The colors used were: 
- White primary color: #fafafa;
- White secondary color: #fff;
- Blue color: #0004ff;
- Dark color: #000000;
- Accent color: #fb0202;

### Typography

- The main font fmaily used is Roboto and sans-serif as backup.
- For the logo Lato was used and sans-serif as a backup.

### Wireframe

<details>
<summary>
Wireframe
</summary>
<details>
<summary>
Wireframe Home
</summary>
<img src="https://github.com/gioZAK/justblog_v1/blob/e35d49ae59977c2161793588133778f4262a8ec2/docs/wireframes/wireframeshome.png">
</details>
<details>
<summary>
Wireframe Blog Post
</summary>
<img src="https://github.com/gioZAK/justblog_v1/blob/877e87b738533609b4573be0e7ec50a93b608b65/docs/wireframes/wireframesblogpost.png">
</details>
<details>
<summary>
Wireframe Profile
</summary>
<img src="https://github.com/gioZAK/justblog_v1/blob/12b74f02a971a523264797465a0fb4cd9d540569/docs/wireframes/wireframesuserprofile.png">
</details>
<details>
<summary>
Wireframe Post/Edit/Profile
</summary>
<img src="https://github.com/gioZAK/justblog_v1/blob/12b74f02a971a523264797465a0fb4cd9d540569/docs/wireframes/wireframespostedit.png">
</details>
</details>

## UX

The blog objective is to be accessible to everyone, anyone can create an account and post there, there is no fixed topic, any content is accepted.
Only the comments require aprove so insults can be avoided.

### Site User Goal

- Read new content posted by someone.
- Read other user comments related to a post.
- Post and Comment in the website to express himself.

### Site Goal

- Provide a platform where people can express themselves.
- Moderate unwanted comments or if needed delete a post.
- Provide entertainment.

## Agile Workflow

This project was created using Agile techniques during development, such as:

- User stories: displayed using GitHub Issues.
- MoSCoW method: by adding a priority to each issue and display it using tags.
- ToDo, In Progress and Done: using the GitHub Kanban board.

You can access the Kanban board that was used during the project development [here](https://github.com/users/gioZAK/projects/10/views/1).

<img src="https://github.com/gioZAK/justblog_v1/blob/befb8792d84f802ab5ff00067eb2213b2a3d7b03/docs/screenshots/kanban.png">


## Features

### Home page
- Content:
    - Blog post list
    - Paginated list of post
    - Post Title, Summary, Author's name and image, number of likes

<img src="https://github.com/gioZAK/justblog_v1/blob/92e9029ec1e2024a882a0dbd72e6c9ba246fd48f/docs/features/mainimg.png">

### Post Page
- Content:
    - Post content
    - Like button and number of comments
    - Allows the owner of the post to edit or delete the post
    - Display to the blog post viewer an invitation to check on the author's profile
    - Comment field and the posted comments

<img src="https://github.com/gioZAK/justblog_v1/blob/92e9029ec1e2024a882a0dbd72e6c9ba246fd48f/docs/features/postimg.png">
<img src="https://github.com/gioZAK/justblog_v1/blob/24618026b25f9a95213dadada593b2737848f510/docs/screenshots/postimg2.png">
<img src="https://github.com/gioZAK/justblog_v1/blob/24618026b25f9a95213dadada593b2737848f510/docs/screenshots/postimgowner.png">


### Profile
- Content:
    - Username, username picture, biography and his list of post.
    - Allows the owner of the profile to edit his profile, edit or delete account and change his password.

<img src="https://github.com/gioZAK/justblog_v1/blob/92e9029ec1e2024a882a0dbd72e6c9ba246fd48f/docs/features/profileimg.png">

### NavBar

- Content:
    - The Logo, Home page button, register button, user profile button, login or logout button
    - Welcome user status, which tells which username is logged in.

    <img src="https://github.com/gioZAK/justblog_v1/blob/24618026b25f9a95213dadada593b2737848f510/docs/screenshots/navbar.png">

### Future Features

- Search bar
    - Could be added so the user can search for the blog topic or user he wants to find
- Post Categories
    - Could be added in order to classify the post by it's content.

## Technologies Used

### Main Tech

 - [Django](https://www.djangoproject.com/) 
 - [JavaScript](https://www.javascript.com/)
 - [Bootstrap](https://getbootstrap.com/)


### Applications, Libraries and Platforms

- Git
    - Used for version control to commit to Git and Push to GitHub.
- Gitpod
    - Used as the IDE to write all the code used in this project.
- Github
    - GitHub is used to store the projects code after being pushed from Git.
- Heroku
    - Used to deploy the application.
- Google Fonts
    - Used to import the fonts Roboto and Lato.
- FontAwesome
    - Used to import the ThumbsUp and Comment icon.
- Balsamiq Wireframes
    - Used to create the project's wireframe.
- Cloudinary
    - Used to host all images.
- Django AllAuth
    - Used to deal with user account registration.
- Chrome DevTool
    - Used to debug and test new styles.
- ChatGTP
    - Used to debug.


## Testing
- I have used automated test and manual testing to check if all the website's functionalities were working as intended.
    -They all passed.

### Python Testing
- I have tested all python files and they all passed
- Tested with [CI pep8](https://pep8ci.herokuapp.com/)
<img src="https://github.com/gioZAK/justblog_v1/blob/92e9029ec1e2024a882a0dbd72e6c9ba246fd48f/docs/testing/testblogview.png">

### JavaScript Testing
- I have tested the script.js and it passed with no major error.
- The undefined variable is not a glitch.
- Tested with [JSHint](https://jshint.com/)
<img src="https://github.com/gioZAK/justblog_v1/blob/f4041e03caf785922b34513733c03cf422969b69/docs/testing/jshint.png">

### CSS Testing
- I have tested the script.css file and it passed.
- Tested with [Jigsaw](https://jigsaw.w3.org/css-validator/)
<img src="https://github.com/gioZAK/justblog_v1/blob/92e9029ec1e2024a882a0dbd72e6c9ba246fd48f/docs/testing/csstest.png">

### HTML Testing
- I have tested all templates and they all passed.
- Tested with [Validator.w3](https://validator.w3.org/nu/#textarea)
<img src="https://github.com/gioZAK/justblog_v1/blob/92e9029ec1e2024a882a0dbd72e6c9ba246fd48f/docs/testing/htmltest.png">

### LightHouse
- I have tested the all webpages with LightHouse and they all exceeded with good scores
<img src="https://github.com/gioZAK/justblog_v1/blob/c54571c2a8efe681addf5f4a9e9aead32a888584/docs/screenshots/lighthouseimg.png">

### Manual Testing
 




## Deployment

### Forking

- In order to Fork this repository:

    1. Access your GitHub account and find the relevant repository.
    2. Click on 'Fork' on the top right of the page.
    3. You will find a copy of the repository in your own Github account.

### Clone

- In order to Clone this repository:

    1. Create repository where you will work with this clone.
    2. Copy "https://github.com/gioZAK/justblog.git".
    3. Run the directory you want the clone to be.
    6. In your IDE's terminal type 'git clone' and the paste the URL you just copied.
    7. Press Enter.
    8. You now have a local clone.

### Heroku 


## Credits

### Code Institute
- I have relied on the Code Institute Django Blog Walktrough project in order to make my own.

### Corey Schafer
- [Corey Schafer Django Course](https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p)

### Django For Everybody - Full Python University Course
- [Django For Everybody - Full Python University Course](https://www.youtube.com/watch?v=o0XbHvKxw7Y&t)

### ChatGPT
- I have used [ChatGPT](https://chat.openai.com/chat) as a tool to debug and to guide me on how to apply new functionalities.

### Unsplash
- I have taken the images for the blog post from [Unsplash](https://unsplash.com/)

[Back to Table of contents](#table-of-contents)