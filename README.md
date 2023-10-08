# Django-REST-API-Development

This is a simple Task Management API built using Django REST framework. It allows users to create, read, update, and delete tasks. Users can also register, log in, and associate tasks with their accounts.
# Table of Contents
Prerequisites
Getting Started
1. Clone the Repository
2. Set Up a Virtual Environment
3. Install Dependencies
4. Configure Environment Variables
5. Apply Database Migrations
6. Create a Superuser
7. Run the Development Server
API Documentation
Testing
Deployment


# Prerequisites
Before you begin, ensure you have met the following requirements:
Python (3.7 or higher) and pip installed.
Django and Django REST framework installed.
A relational database (e.g., PostgreSQL, MySQL, SQLite) and its driver installed.

# Clone the Repository
git clone https://github.com/rutuja-1201/Django-REST-API-Development.git

Set Up a Virtual Environment
python -m venv venv

Activate the virtual environment:
venv\Scripts\activate
\
Install Dependencies
pip install -r requirements.txt

Configure Environment Variables
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=your_database_url

Apply Database Migrations
python manage.py migrate


Create a Superuser
python manage.py createsuperuser

Run the Development Server
python manage.py runserver

The API should now be running at http://localhost:8000/. You can access the admin panel at http://localhost:8000/admin/


# API Documentation
API documentation is available through Swagger UI and ReDoc:

Swagger UI: http://localhost:8000/swagger/
ReDoc: http://localhost:8000/redoc/


# Testing
To run unit tests for the application, use the following command:
python manage.py test

# Deployment
For production deployment, follow these steps:

Set up a production-ready database.
Configure production settings in settings.py.
Collect static files:
python manage.py collectstatic






