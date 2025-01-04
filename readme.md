# LETS Company Blog

LETS Company Blog is a Flask-based web application designed for creating and sharing blog posts. The application includes user registration, authentication, profile management, and CRUD (Create, Read, Update, Delete) functionality for blog posts.

## Features

- User registration and login with secure password handling.
- Profile management, including updating usernames, emails, and profile pictures.
- Create, read, update, and delete blog posts.
- Pagination for viewing blog posts.
- Error handling for 404 and 403 errors.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/LETScompanyblog.git
   cd LETScompanyblog
   ```

2. **Set up a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database:**
   ```bash
   flask db init
   flask db migrate -m "Initial migration."
   flask db upgrade
   ```

5. **Run the Application:**
   ```bash
   flask run
   ```
   Visit `http://127.0.0.1:5000/` in your browser.

## File Structure

- **`app.py`**: Entry point of the application.
- **`models.py`**: Database models for users and blog posts.
- **`forms.py`**: WTForms for user registration, login, and post creation.
- **`handlers.py`**: Handles error pages and routes.
- **`views.py`**: Contains views for user and blog post functionality.
- **Templates**: HTML templates for rendering pages.
- **Static**: Contains static assets like profile pictures.

## Key Packages Used

- `Flask`
- `Flask-SQLAlchemy`
- `Flask-Migrate`
- `Flask-WTF`
- `Flask-Login`

## How to Contribute

1. Fork the repository.
2. Create a new branch for your feature/bugfix.
3. Make your changes and ensure the app runs correctly.
4. Push your branch and create a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
