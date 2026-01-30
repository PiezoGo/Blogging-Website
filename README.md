# Blogging Website
## Overview
This is a simple blogging website built using Django, a Python web framework. It allows users to sign up, log in, create blog posts, view existing posts, and delete their own posts. The project uses SQLite as the database and basic HTML templates for the frontend. It's designed as a beginner-friendly example of a full-stack web application with user authentication and CRUD operations for blog content.
Features

User Authentication: Secure sign-up, login, and logout functionality.
Blog Post Management: Create new posts, view a list of all posts, view individual post details, and delete posts (for authenticated users).
Database Integration: Uses SQLite for storing user data and blog posts.
Simple Templates: Basic HTML templates for rendering pages, with potential for extension to CSS/JS enhancements.

## Technologies Used

- Backend: Django (Python framework)
- Database: SQLite
- Frontend: HTML templates (with Django's templating engine)
- Dependencies: Managed via Pipenv (see Pipfile for details, including Django and related - packages)
- Languages: Python (81.5%), HTML (18.5%)

## Installation

### Clone the Repository:
```
textgit clone https://github.com/PiezoGo/Blogging-Website.git
cd Blogging-Website
```

### Set Up Virtual Environment (using Pipenv):
```
pip install pipenv
pipenv install
pipenv shell
```
### Apply Migrations:textpython manage.py makemigrations
```python manage.py migrate```
Create Superuser (optional, for admin access):textpython manage.py createsuperuser
Run the Server:textpython manage.py runserverOpen your browser and navigate to http://127.0.0.1:8000/ to access the site.

## Usage

Home Page: View a welcome message or featured content.
Sign Up/Login: Create an account or log in to access post creation features.
Create Post: Navigate to the post creation page (available after login) to add new blog entries.
View Posts: Browse the list of all posts or click on a post for details.
Delete Post: Authenticated users can delete their own posts.
Admin Panel: Access /admin/ with superuser credentials to manage users and posts.

## Project Structure

accounts/: Handles user authentication (models, views, forms).
blog/: Core blog app (models for posts, views for listing and details).
blog2/: Additional blog-related functionality (e.g., post deletion).
templates/: HTML templates for all pages.
manage.py: Django management script.
Pipfile & Pipfile.lock: Dependency management.
db.sqlite3: SQLite database file (do not commit sensitive data).

## Contributing
Contributions are welcome! Feel free to fork the repository, make improvements (e.g., adding CSS styling, animations, or advanced features like comments/search), and submit a pull request.

### Fork the repo.
Create a new branch: 
```git checkout -b feature-branch```
Commit your changes: 
```git commit -m 'Add some feature```
Push to the branch: 
```git push origin feature-branch```
Open a pull request.

## License
This project is open-source and available under the MIT License. See the LICENSE file for details (if not present, assume MIT).
Contact
For questions or suggestions, open an issue on GitHub or reach out to the repository owner.
Last updated: January 2026