# README.md

## Overview

Welcome to the **LETS Company Blog**, a feature-rich social blogging platform built using Flask. This project is the culmination of my efforts to design and implement a full-stack web application that emphasizes modular design, user interaction, and robust functionality. The application allows users to register, log in, create blog posts, manage their profiles, and browse content posted by others. It also includes custom error handling for seamless user experiences.

This project was developed with scalability, security, and responsiveness in mind. Leveraging Bootstrap for the front-end and Flask's extensions for the back-end, the blog ensures a professional appearance and smooth operation across various devices.

---

## Files and Their Purpose

### Core Files
- **`app.py`**:
  This is the entry point of the application. It initializes the Flask app and runs it in debug mode for development purposes.

- **`LETScompanyblog/__init__.py`**:
  Initializes the Flask application, database, and login manager. It also registers blueprints for modular routing and ensures that configurations, like the `SECRET_KEY` and database URI, are properly set up.

- **`LETScompanyblog/models.py`**:
  Contains the database schema and models for the application. It includes the `User` model for handling user authentication and profile management, and the `BlogPost` model for storing blog content.

### Modules
- **`LETScompanyblog/core`**:
  - **`views.py`**: Contains routes for the homepage (`/`) and the info page (`/info`). The homepage lists recent blog posts with pagination, while the info page provides details about the company.

- **`LETScompanyblog/blog_posts`**:
  - **`forms.py`**: Defines a form for creating and editing blog posts, including fields for the title and content.
  - **`views.py`**: Implements CRUD operations for blog posts. Users can create, read, update, and delete their posts. Authorization checks ensure that only the author can modify or delete posts.

- **`LETScompanyblog/users`**:
  - **`forms.py`**: Includes forms for user registration, login, and profile updates. It ensures validation for unique emails and usernames.
  - **`views.py`**: Handles user registration, login, logout, and account management. It also includes functionality to display all posts by a specific user.
  - **`picture_handler.py`**: Processes and resizes uploaded profile pictures, ensuring consistent dimensions for display.

- **`LETScompanyblog/error_pages`**:
  - **`handlers.py`**: Contains custom error handlers for 403 (Forbidden) and 404 (Not Found) errors. It ensures users receive meaningful feedback when encountering these issues.

### Templates
- **Base Templates**:
  - **`base.html`**: The primary layout file that includes navigation and defines blocks for extending other pages.
- **Specific Pages**:
  - **`index.html`**: Displays recent blog posts with pagination.
  - **`register.html`**: User registration page with a Bootstrap-styled form.
  - **`login.html`**: Login page featuring flash message integration.
  - **`account.html`**: Profile management page where users can update their details and profile picture.
  - **`create_post.html`**: Form for creating or editing a blog post.
  - **`user_blog_posts.html`**: Displays all posts by a specific user.
  - **Error Templates**:
    - **`403.html`** and **`404.html`**: Custom error pages for forbidden access and missing resources.

### Static Files
- **Profile Pictures**:
  - Stored in the `static/profile_pics` directory. Includes default and user-uploaded profile images.

### Database
- **`data.sqlite`**:
  The SQLite database file storing user and blog post data.

---

## Design Choices

### Modular Architecture
One of the key design decisions was to use Flask's blueprint system to organize routes and views into separate modules (`core`, `blog_posts`, `users`, `error_pages`). This ensures scalability and maintainability as the application grows.

### Security
- Passwords are hashed using `werkzeug.security` to ensure user credentials are secure.
- Forms are protected from CSRF attacks using Flask-WTF's built-in capabilities.
- File uploads are restricted to `.jpg` and `.png` formats and resized to a standard size before storage.

### Responsive Design
Bootstrap was chosen to provide a clean and responsive front-end design. This decision simplifies styling while ensuring the app functions well on various devices.

### Pagination
Pagination for blog posts was implemented to improve usability and reduce load times for pages with many posts. Flask-SQLAlchemy's `paginate` function made this feature straightforward to implement.

### Custom Error Pages
Meaningful error pages (403 and 404) were added to enhance user experience and provide feedback in case of navigation issues.

---

## Challenges and Design Trade-Offs
1. **Database Choice**:
   - SQLite was chosen for simplicity, but it may require migration to a more robust database like PostgreSQL for larger-scale deployment.

2. **User Profile Images**:
   - The current implementation stores images locally. This simplifies the process but could be replaced with a cloud storage solution for better scalability.

3. **Authorization**:
   - A basic user role system could be added in the future to differentiate between admins and regular users.

4. **Deployment**:
   - While the app is configured for development (`debug=True`), additional steps like using environment variables and configuring a production-ready web server are needed for deployment.

---

## Video Demo
Check out the project in action: [LETS Company Blog Video Demo](https://youtu.be/81DOnO989ME)

---

## Live Website
Explore the live application here: [LETS Company Blog](https://lets-company-blog-a636485104e1.herokuapp.com/)

---

## Conclusion
The **LETS Company Blog** is a comprehensive Flask application that highlights key web development skills, including back-end programming, database management, front-end integration, and security. With additional features like comments and admin roles, it could evolve into a full-fledged blogging platform. This project represents my dedication to learning and implementing modern web development practices, and I am proud of its outcome.

