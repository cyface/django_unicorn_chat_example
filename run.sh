#!/bin/bash
python manage.py migrate
python manage.py loaddata initial_data
python manage.py runserver