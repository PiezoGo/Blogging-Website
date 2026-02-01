#!/bin/bash

# Upgrade pip and install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Collect static files – this is crucial!
python manage.py collectstatic --noinput --clear

# Optional: apply migrations if you add a real DB later
# python manage.py migrate