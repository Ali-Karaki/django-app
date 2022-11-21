> Install & check versions
pip install django
python -m django --version

> Virtual Env
pip install virtualenvwrapper-win
mkvirtualenv myapp

> Create a project
django-admin startproject myproject

> Enter / exit venv
deactivate
workon myapp

> Create an app
python manage.py startapp myapp

> Run project
python manage.py runserver

> Migrate
python manage.py migrate

> Routing
- create a view in `views.py`
- add url of view in `urls.py` (app)
- include url of app in `urls.py` (project)

