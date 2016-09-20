#!flask/bin/python

from app import app
from app import views
app.run(debug = True, host = '0.0.0.0', port = 80)
