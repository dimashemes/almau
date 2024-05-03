#!/bin/sh

export DJANGO_SETTINGS_MODULE=core.settings

python manage.py collectstatic --noinput

echo 'Applying migrations...'
python manage.py migrate

echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@gmail.com', 'password')" | python manage.py shell

gunicorn core.wsgi:application --bind 0.0.0.0:$PORT
