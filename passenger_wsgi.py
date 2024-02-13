"""
Deploying the application with Passenger WSGI.

@author "Daniel Mizsak" <info@pythonvilag.hu>
"""

import imp

wsgi = imp.load_source("wsgi", "src/run.py")
application = wsgi.app
