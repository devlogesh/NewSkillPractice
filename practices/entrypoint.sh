#!/bin/sh


echo "Running entrypoint.sh..."


python3 manage.py collectstatic --noinput

python3 manage.py makemigrations 
python3 manage.py migrate 

python3 manage.py runserver 0.0.0.0:8000

# exec  gunicorn --bind 0.0.0.0:8000 practices.wsgi:application