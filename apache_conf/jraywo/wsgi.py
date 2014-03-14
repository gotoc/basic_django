import os
import sys
import site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('/home/jvwong/.virtualenvs/practical_django/local/lib/python2.7/site-packages')

# Add the app's directory to the PYTHONPATH
sys.path.append('/home/jvwong/projects/django_projects')
sys.path.append('/home/jvwong/projects/django_projects/jraywo')
sys.path.append('/home/jvwong/projects/django_projects/config')
sys.path.append('/home/jvwong/.virtualenvs/practical_django')

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings.jraywo'

# Activate your virtual env
activate_env=os.path.expanduser("/home/jvwong/.virtualenvs/practical_django/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
