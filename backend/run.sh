#!/bin/bash

PYTHONPATH=/root/git/3A/backend  gunicorn app.wsgi -c /root/git/3A/backend/gunicorn/gunicorn.py 
