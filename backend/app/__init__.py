
from flask import Flask, Blueprint, request, g
from flask_babel import Babel
from flask._compat import text_type
from flask.json import JSONEncoder as BaseEncoder
from speaklater import _LazyString


class BabelExt(Babel):
    def __init__(self, app=None, default_locale='en', default_timezone='UTC',
                 date_formats=None, configure_jinja=True):
        Babel.__init__(self, app, default_locale, default_timezone, date_formats, configure_jinja)
        self.locale_selector_func = None
        self.timezone_selector_func = None

babel = BabelExt()


@babel.localeselector
def get_locale():
    if 'accept_languages' in dir(request) \
            and str(request.accept_languages) in ['en', 'ko', 'ja']:
        # Accept-Language 헤더값으로 오버라이드 되었는지 확인
        return str(request.accept_languages)

    lang = getattr(g, 'lang', 'ko')
    return lang


class JSONEncoder(BaseEncoder):
    def default(self, o):
        if isinstance(o, _LazyString):
            return text_type(o)

        return BaseEncoder.default(self, o)
        

def create_app():
    app = Flask(__name__)
    app.json_encoder = JSONEncoder

    from app.api import base_bp
    app.register_blueprint(base_bp, url_prefix='')
    from app.api.hr import hr_bp
    app.register_blueprint(hr_bp, url_prefix='/api')

    return app
