
import os
from flask import Flask, Blueprint, request

GUI_HOME="/root/git/3A/frontend"
main_bp = Blueprint('main', __name__,
                    template_folder='templates',
                    static_folder='',
                    root_path=os.path.abspath(os.path.join(GUI_HOME, 'frontend')))