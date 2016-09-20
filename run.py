from werkzeug.contrib.fixers import ProxyFix

from app import app
from app import views
app.wsgi_app = ProxyFix(app.wsgi_app)
app.run(debug = True, host = '0.0.0.0', port = 80)
