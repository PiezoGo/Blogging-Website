#!/bin/bash

pip install --upgrade pip
pip install -r requirements.txt

# Collect static files (VERY IMPORTANT for admin, CSS, etc.)
python manage.py collectstatic --noinput

# Optional: migrate if you have DB (but Vercel usually uses external DB like Neon/Supabase)
# python manage.py migrate