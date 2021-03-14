from app.api import base_bp
from app.core.exceptions import ApiException

@base_bp.route('/')
def index():
    raise ApiException(1000, "...................")
    return "aaaaaaaaaaaaaa"


