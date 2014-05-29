from __future__ import with_statement
from fabric.api import *

def push():
    local("git push origin master")

env.hosts = ['jvwong@107.170.63.152']

def remote_pull():
    code_dir = '/home/jvwong/projects/django_projects/'
    with cd(code_dir):
        run("git pull origin master")

def remote_collectstatic():
    code_dir = '/home/jvwong/projects/django_projects/'
    with cd(code_dir):
        run("/home/jvwong/.virtualenvs/practical_django/bin/python2.7 manage.py collectstatic")

def remote_restart_apache2():
    sudo('service apache2 reload')

def reboot():
    sudo('reboot')


def deploy(collectstatic=False):
    push()
    remote_pull()

    if collectstatic:
        remote_collectstatic()

    remote_restart_apache2()
