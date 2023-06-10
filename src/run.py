"""
Script for hosting the web application.

@author "Dániel Lajos Mizsák" <info@pythonvilag.hu>
"""

from pythonvilag_website import app

if __name__ == "__main__":
    app.run(debug=app.config["FLASK_DEBUG"], host="0.0.0.0")
