
from flask import Flask, Blueprint, request, g
from flask._compat import text_type
from flask.json import JSONEncoder as BaseEncoder

class JSONEncoder(BaseEncoder):
    def default(self, o):
        if isinstance(o, _LazyString):
            return text_type(o)

        return BaseEncoder.default(self, o)

def create_app():
    app = Flask(__name__)
    app.json_encoder = JSONEncoder

    from app.api.main import main_bp
    app.register_blueprint(main_bp, url_prefix='')

    from app.api.hr import hr_bp
    app.register_blueprint(hr_bp, url_prefix='/api')

    return app
