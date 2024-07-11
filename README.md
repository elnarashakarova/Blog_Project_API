# Task: Create a Blog API Server Using Django Rest Framework (DRF)
## Objective:
Develop a Blog API server that allows users to manage blog posts and comments using Django Rest Framework (DRF).

## Requirements:
### Set Up the Project:

Create a new Django project named blog_project.
Create a new Django app named blog.
## Models:

### Post Model:
Fields: title, content, author, created_at, updated_at.
Ensure title and content are required fields.
The author field should be a foreign key to the built-in Django User model.
The created_at and updated_at fields should be auto-populated with the current timestamp.
### Comment Model:
Fields: post (ForeignKey to Post), author, content, created_at.
Ensure content is a required field.
The author field should be a foreign key to the built-in Django User model.
The created_at field should be auto-populated with the current timestamp.
Serializers:

### Create serializers for the Post and Comment models.
Ensure nested representation of comments in the Post serializer. Implement data validation/sanitization.
### Views:

Create views for Post and Comment.
Implement CRUD operations for Post and Comment.

### URLs:

Configure the project URLs to include the routes for the blog app.
Ensure the API endpoints are accessible.
### Authentication:

Implement basic authentication to secure the API endpoints.
Only authenticated users should be able to create, update, or delete posts and comments.

## Deliverables:
A Git repository with the Django project and app code.
A README file with instructions on how to set up and run the project.
CI with testing.
Ensure that the code is clean, well-documented, and adheres to best practices.

## Extra: Likes 
Create functionality for likes 
