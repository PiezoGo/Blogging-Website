# api/index.py  (or api/wsgi.py)
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yourprojectname.settings')  # ← change to your actual settings module
application = get_wsgi_application()

# Vercel requires this alias for serverless
app = application