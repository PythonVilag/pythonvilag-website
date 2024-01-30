"""
Deploying the application with Gunicorn.

@author "Daniel Mizsak" <info@pythonvilag.hu>
"""

bind = "0.0.0.0:8080"
workers = 2
