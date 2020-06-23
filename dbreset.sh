#!/bin/sh
APP=app
cd ${APP}
rm -d -r migrations/
cd ..
rm -d -r db.sqlite3
python manage.py makemigrations ${APP}
python manage.py migrate
python manage.py createsuperuser --username admin --email admin@example.com
python manage.py loaddata ${APP}/fixtures/initial_data.json