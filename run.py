from werkzeug.contrib.fixers import ProxyFix

from app import app
from app import views
app.wsgi_app = ProxyFix(app.wsgi_app)
