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
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── base/                       # Django app directory
│   ├── migrations/             # Database migration files
│   │   └── __init__.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── templates/                  # Templates directory
│   ├── home.html
│   ├── navbar.html
│   └── room.html
├── db.sqlite3                  # SQLite database file
└── manage.py                   # Django's command-line utility for administrative tasks
```
