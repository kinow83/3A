#!/bin/bash
sudo mkdir -p /var/log/gunicorn
sudo touch /var/log/gunicorn/error.log
sudo PYTHONPATH=.  gunicorn app.wsgi -c gunicorn/gunicorn.py 
