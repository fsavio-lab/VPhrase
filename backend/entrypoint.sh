#!/bin/bash
cd vphrase
until python manage.py makemigrations && python3 manage.py migrate
do
    echo "Making migrations"
    sleep 1
done

until python manage.py collectstatic --noinput
do
    echo "Initialized Static Folder"
    sleep 1
done

until python manage.py ingestion --path $(pwd)/vphrase/data/movies.csv
do
    echo "Ingesting Data into DB"
    sleep 3
done

gunicorn vphrase.wsgi:application --bind 0.0.0.0:8000
# python manage.py runserver 0.0.0.0:8000
