# Install & check versions
pip install django
python -m django --version

# Virtual Env
pip install virtualenvwrapper-win
mkvirtualenv myapp

# Create a project
django-admin startproject myproject

# Enter / exit venv
deactivate
workon myapp

# Create an app
python manage.py startapp myapp

# Run project
python manage.py runserver

# Migrate
python manage.py migrate

# Routing
- create a view in `views.py`
- add url of view in `urls.py` (app)
- include url of app in `urls.py` (project)

# Templates
- create `template` folder
- add template to `TEMPLATES.DIRS` in `settings.py`

# Dynamic data
- create `context` dict in `views.py`
- pass context to `render()`
- use {{}} in template

# GET
- define `CounterGET` function in `views.py`
- define url for `CounterGET` (also called that) in `urls.py`
- in `index.html`, on submit, call `action=CounterGET` which is our route
- this method will send the content of the form in URL, req.GET['textAreaName']
# POST
- same logic as get
- add `{% csrf_token %}` above form bcs of it's a POST function
- add line 125 in `settings.py` https://stackoverflow.com/questions/70285834/forbidden-403-csrf-verification-failed-request-aborted-reason-given-for-fail
- no changes in URL, req.POST['textAreaName']


# Static Files
- add static files (css) in static `folder`
- tell `settings.py` where to locate static files `STATICFILES_DIRS`
- loading static files:
  - on top of page `{% load static %}`
  - `href="{% static 'style.css' %}"`
