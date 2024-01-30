"""
Deploying the application with Gunicorn.

@author "Daniel Mizsak" <info@pythonvilag.hu>
"""

bind = "0.0.0.0:5000"
worker_tmp_dir = "/dev/shm"  # noqa: S108
workers = 2
wsgi_app = "src.run:app"
