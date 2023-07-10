# first execution
py -m venv venv
.\venv\Scripts\activate
pip3 install django
pip install django-crispy-forms
pip install django-tables2
pip install djangorestframework
pip install markdown
pip install django-filter
py manage.py makemigrations users
py manage.py makemigrations funcionarios
py manage.py migrate
python manage.py createsuperuser --email admin@example.com --username admin
pip install drf-spectacular

py manage.py runserver