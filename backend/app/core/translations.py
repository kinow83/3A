import app
from flask_babel import lazy_gettext
from flask import _request_ctx_stack, current_app


def gettext(string, **variables):
    """Translates a string with the current locale and passes in the
    given keyword arguments as mapping to a string formatting string.

    ::

        gettext(u'Hello World!')
        gettext(u'Hello {name}!', name='World')
    """
    t = get_translations()
    if t is None:
        return string if not variables else string % variables

    s = t.ugettext(string)
    return s if not variables else s.format(**variables)

def get_translations():
    # If there is no context:  return None
    ctx = _request_ctx_stack.top
    if not ctx:
        return None

    # If context exists and contains a cashed value, return cached value
    if hasattr(ctx, 'flask_user_translations'):
        return ctx.flask_user_translations

    # If App has not initialized Flask-Babel: return None
    app_has_initalized_flask_babel = 'babel' in current_app.extensions
    if not app_has_initalized_flask_babel:  # pragma no cover
        ctx.flask_user_translations = None
        return ctx.flask_user_translations

    # Prepare search properties
    import os
    import gettext as python_gettext
    from flask_babel import get_locale, support
    domain = 'messages'
    locales = [app.get_locale()]
    languages = [str(locale) for locale in locales]

    # See if translations exists in Application dir    
    app_dir = os.path.join(current_app.root_path, 'translations')
    filename = python_gettext.find(domain, app_dir, languages)
    if filename:
        ctx.flask_user_translations = support.Translations.load(app_dir, locales, domain=domain)

    # See if translations exists in Flask-User dir
    else:
        flask_user_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'translations')
        ctx.flask_user_translations = support.Translations.load(flask_user_dir, locales, domain=domain)

    from flask.ext import babel
    # TODO: first babel.get_translations
    return babel.get_translations().merge(ctx.flask_user_translations)

_ = gettext
lazy_gettext = lazy_gettext
