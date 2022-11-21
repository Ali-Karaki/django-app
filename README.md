pip install django
python -m django --version

pip install virtualenvwrapper-win
mkvirtualenv myapp

django-admin startproject myproject

deactivate
workon myapp

python manage.py startapp myapp