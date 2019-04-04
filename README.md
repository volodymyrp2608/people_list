# List people

The project works using Django & Python and built on the REST API.

##To use this project, follow these steps:

###Install the virtual environment.

    pip install -m venv myvenv

activate it

mac: `source bin/activate`

windows: `.\Scripts\activate`

----

###Install django and other necessary components.

    pip install -r requirements.txt

----

###Create src folder

    mkdir src && cd src

----

###Create a data_people project

    django-admin startproject data_people

    django-admin startapp people

----

###settings.py

    INSTALLED_APPS = [
        ...
        'widget_tweaks',
        'rest_framework',
        'rest_framework.authtoken',
        'people',
    ]


    REST_FRAMEWORK = {
        'DEFAULT_PERMISSION_CLASSES': (
            'rest_framework.permissions.IsAuthenticatedOrReadOnly',
        ),
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
            'rest_framework.authentication.SessionAuthentication',
            'rest_framework.authentication.BasicAuthentication',
        ),
    }
