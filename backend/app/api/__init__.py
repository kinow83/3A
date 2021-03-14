import os
import logging

from flask import Flask, Blueprint, request
from flask_restful import Resource, Api, url_for
from app.config import GUI_HOME

base_bp = Blueprint('base', __name__,
                    template_folder='templates',
                    static_folder='',
                    root_path=os.path.abspath(os.path.join(GUI_HOME, 'frontend')))


from . import base