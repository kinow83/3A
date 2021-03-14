import flask_babel as babel
from flask import Flask, Blueprint, request, g
from flask._compat import text_type
from flask.json import JSONEncoder as BaseEncoder
from speaklater import _LazyString
from babel.support import NullTranslations
from flask_babel import gettext, ngettext, lazy_gettext, get_translations


class JSONEncoder(BaseEncoder):
    def default(self, o):
        if isinstance(o, _LazyString):
            return text_type(o)

        return BaseEncoder.default(self, o)
        


def create_app():
    b = babel.Babel()
    @b.localeselector
    def get_locale():
        lang = getattr(g, 'lang', 'ko')
        if lang:
            return lang
        return  request.accept_languages.best_match(['en', 'ko', 'en'])

    app = Flask(__name__)
    b.init_app(app)

    with app.app_context():
        assert isinstance(get_translations(), NullTranslations)
    
    app.config.update({
        'BABEL_TRANSLATION_DIRECTORIES': 'translations',
        'BABEL_DEFAULT_LOCALE': 'ko'
    })
    
    print(app.config['BABEL_DEFAULT_LOCALE'])
    print(app.config['BABEL_DEFAULT_TIMEZONE'])
    print(app.config['BABEL_TRANSLATION_DIRECTORIES'])

    lazy_string = gettext('Error Sample')
    print(lazy_string)

    app.json_encoder = JSONEncoder

    from app.api.sample import sample_bp
    app.register_blueprint(sample_bp, url_prefix='')
    from app.api import base_bp
    app.register_blueprint(base_bp, url_prefix='')
    from app.api.hr import hr_bp
    app.register_blueprint(hr_bp, url_prefix='/api')

    return app
