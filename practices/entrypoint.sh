#!/bin/sh


echo "Running entrypoint.sh..."


python manage.py collectstatic --noinput

python manage.py makemigrations --noinput

python manage.py migrate --noinput

exec  gunicorn --bind 0.0.0.0:8000 practices.wsgi:application