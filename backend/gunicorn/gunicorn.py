import os

#workers = 2
#threads = 5

idfile    = '/var/run/gunicorn/gunicorn.pid'
bind      = 'unix:/var/run/gunicorn/socket'
accesslog = '/var/log/gunicorn/access.log'
errorlog  = '/var/log/gunicorn/error.log'

def on_starting(server):
    if not os.path.exists("/var/run/gunicorn"):
        os.makedirs("/var/run/gunicorn")
    if not os.path.exists("/var/log/gunicorn"):
        os.makedirs("/var/log/gunicorn")
