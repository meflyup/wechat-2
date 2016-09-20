from werkzeug.contrib.fixers import ProxyFix

from app import app
from app import views
<<<<<<< HEAD
app.wsgi_app = ProxyFix(app.wsgi_app)
app.run(debug = True, host = '0.0.0.0', port = 80)
=======
app.run(debug = True, host='23.21.52.24', port = 80)
>>>>>>> dcd6695087b9593fc138b2b300ef152881d1a5de
