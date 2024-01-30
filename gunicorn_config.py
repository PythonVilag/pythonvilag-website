"""
Deploying the application with Gunicorn.

@author "Daniel Mizsak" <info@pythonvilag.hu>
"""

bind = "0.0.0.0:5000"
workers = 2
