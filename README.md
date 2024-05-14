# User Blog

A web application with user and blog modules. The user module provides APIs for registration, login, and logout, while the blog module offers APIs for CRUD operations on blogs and a blog list API with a search option for title and content. The project is dockerized and can be run using Docker Compose.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
  - [User Module](#user-module)
  - [Blog Module](#blog-module)

## Installation

To set up and run the project locally, ensure you have Docker and Docker Compose installed. Then follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/neethubaskar/user_blog.git
2. Navigate to the project directory:
   ```bash
   cd user_blog
3. Build and start the application using Docker Compose:
   ```bash
   docker-compose up

## Usage

Once the application is running, you can access the APIs through the following endpoints.

## API Endpoints

### User Module

- Registration

  - Endpoint: /users/api/v1/register/
  - Method: POST
  - Description: Registers a new user.
  - Request body.
  ```bash
  {
    "username": "neethu", 
    "email": "neethu@mail.com", 
    "first_name": "Neethu", 
    "last_name": "M V", 
    "password": "Neethu@123", 
    "password2": "Neethu@123"
  }

- Login

  - Endpoint: /users/api/v1/login/
  - Method: POST
  - Description: Logs in a user.
  - Request body.
  ```bash
  {
    "username": "neethumv",
    "password": "Neethu@123"
  }

- Logout

  - Endpoint: /users/api/v1/logout/
  - Method: GET
  - Description: Logs out the current user.
 
### Blog Module

- Create Blog

  - Endpoint: /blog/api/v1/blogposts/
  - Method: POST
  - Description: Creates a new blog post.
  - Request body.
  ```bash
  {
    "title": "Big Data Made Simple",
    "content": "Run by: Crayon Data Website link: bigdata-madesimple.com/ Big Data Made Simple is a collection of articles that covers almost every vertical and technology in the big data sphere. Whether you are interested in the latest in artificial intelligence or are trying to use data in your marketing, there’s something for everyone on this site."
  }

- Update Blog

  - Endpoint: /blog/api/v1/blogposts/{id}
  - Method: PUT/PATCH
  - Description: Updates a blog post by its ID.
  - Request body.
  ```bash
  {
    "title": "Big Data Made Simple",
    "content": "Run by: Crayon Data Website link: bigdata-madesimple.com/ Big Data Made Simple is a collection of articles that covers almost every vertical and technology in the big data sphere. Whether you are interested in the latest in artificial intelligence or are trying to use data in your marketing, there’s something for everyone on this site."
  }

- Delete Blog

  - Endpoint: /blog/api/v1/blogposts/{id}
  - Method: DELETE
  - Description: Deletes a blog post by its ID (set is_active flag to False).
 
- List Blog

  - Endpoint: /blog/api/v1/blog-list/
  - Method: GET
  - Description: Lists all blog posts with optional search parameters. When the user is authenticated it only shows autheticated user blogs.
  - Query Parameters: ?q={title/content}

