from app.api import base_bp
from app.core.exceptions import ApiException
from app.core.error import ERR

@base_bp.route('/')
def index():
    return "aaaaaaaaaaaaaa"


