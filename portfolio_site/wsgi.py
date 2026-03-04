import sys
import os

# Add your project directory to the sys.path
project_home = '/home/AliArayz/portfolio-website'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'portfolio_site.settings'

# Import Django WSGI handler
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
