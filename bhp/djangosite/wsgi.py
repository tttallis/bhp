"""
WSGI config for bhp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

# Also import sys and site to help enable virtualenv
import os, sys, site
 
# Add the site packages, to override any system-wide packages
site.addsitedir('/home/ether/.virtualenvs/bhp/lib/python2.7/site-packages')

# As is
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangosite.settings")
 
 
# Activate the virtualenv
activate_this = os.path.expanduser("~/.virtualenvs/bhp/bin/activate_this.py")
execfile(activate_this, dict(__file__=activate_this))

# Calculate the path based on the location of the WSGI script
project = '/home/ether/webapps/bhp/bhp/'
workspace = os.path.dirname(project)
sys.path.append(workspace)
 
sys.path = ['/home/ether/webapps/bhp/bhp', '/home/ether/webapps/bhp/bhp/djangosite', '/home/ether/webapps/bhp'] + sys.path
 
 
# As is
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
 
