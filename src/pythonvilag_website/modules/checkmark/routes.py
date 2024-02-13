"""
Import and add the checkmark module to the app.

@author "Daniel Mizsak" <info@pythonvilag.hu>
"""

from pythonvilag_website import app, csrf

if app.config["CHECKMARK"]:
    from checkmark.server.routes import checkmark_page

    csrf.exempt(checkmark_page)
    app.register_blueprint(checkmark_page, url_prefix="/checkmark")
