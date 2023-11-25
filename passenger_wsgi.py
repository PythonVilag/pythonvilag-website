"""
Deploying the application with Passenger WSGI.

@author "Daniel Mizsak" <info@pythonvilag.hu>
"""

import imp
import sys
from pathlib import Path

sys.path.extend(
    [
        str(Path(__file__).parent / "src"),
        str(Path(__file__).parent),
    ],
)

wsgi = imp.load_source("wsgi", "src/run.py")
application = wsgi.app
