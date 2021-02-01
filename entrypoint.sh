#!/bin/sh

echo "Apply database migrations"
python manage.py db upgrade

echo "Starting server"
if [ $FLASK_ENV = "production" ]
then
  gunicorn manage:app
else
  python manage.py runserver -h "0.0.0.0" -p "5000" --reload
fi
