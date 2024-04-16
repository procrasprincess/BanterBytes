# BanterBytes

## Setup

### Env

- [x] Install `virtualenv` to create isolated Python environments
  - `pip3 install virtualenv`
- [x] Activate the newly created virtual environment
  - Unix: `source env/bin/activate`
  - Windows: `env\Scripts\activate`
- [x] Deactivate the virtual environment when done
  - `deactivate`

### Init and Configue

- [x] Install Django within the virtual environment
  - `pip install django`
- [x] Initialize the Django project
  - `django-admin startproject banterbytes`
- [x] Start the Django development server
  - `python manage.py runserver`
- [x] Apply database migrations 
  - `python manage.py migrate`
- [x] Create a new Django application within the project
  - `python manage.py startapp banterbytes` 

### Structure

```
banterbytes/                    # Django project root directory
├── banterbytes/                # Django project configuration directory
│   ├── __init__.py             # Indicates a Python package
│   ├── asgi.py                 # ASGI config for async web servers
│   ├── settings.py             # Settings/configuration for the Django project
│   ├── urls.py                 # The URL declarations for the Django project
│   └── wsgi.py                 # WSGI config for web servers
├── base/                       # Django app directory
│   ├── migrations/             # Database migration files
│   ├── templates/              # Template files specific to the 'base' app
│   │   └── base/
│   │       ├── home.html       # Home page template for the 'base' app
│   │       └── room.html       # Room page template for the 'base' app
│   ├── admin.py                # Admin site configuration for the 'base' app
│   ├── apps.py                 # Application configuration for the 'base' app
│   ├── models.py               # Database models for the 'base' app
│   ├── tests.py                # Test suite for the 'base' app
│   └── views.py                # Views for the 'base' app
├── templates/                  # Global templates directory
│   └── navbar.html             # Navigation bar template
├── db.sqlite3                  # Default SQLite database file used by Django
└── manage.py                   # Command-line utility for administrative tasks
```
