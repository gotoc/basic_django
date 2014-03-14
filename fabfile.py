from __future__ import with_statement
from fabric.api import *

def commit():
    with settings(warn_only=False):
        local('git commit -a -m "latest update"')

def push():
    local("git push origin master")

def compush():
    commit()
    push()

env.hosts = ['jvwong@107.170.63.152']

def remote_pull():
    code_dir = '/home/jvwong/projects/django_projects/'
    with cd(code_dir):
        sudo("git pull origin master")

#def getStatus():
#    run('/usr/local/bin/supervisorctl status')

#def start_sup():
#    sudo('/usr/local/bin/supervisord -c /etc/supervisord.conf')

#def stop_sup():
#    run('/usr/local/bin/supervisorctl stop all')
#    run('/usr/local/bin/supervisorctl shutdown')

def restart():
    sudo('service apache2 restart')

def reboot():
    sudo('reboot')

def deploy(restart=True):
    push()
    remote_pull()
    with settings(warn_only=True):
        if restart:
            result1 = restart_sup()
