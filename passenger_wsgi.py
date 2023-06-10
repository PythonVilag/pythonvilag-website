import imp
import os
import sys

sys.path.extend(
    [
        os.path.join(os.path.dirname(__file__), "src"),
        os.path.dirname(__file__),
    ]
)

wsgi = imp.load_source("wsgi", "src/run.py")
application = wsgi.app
