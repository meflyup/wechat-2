#!flask/bin/python

from app import app
from app import views
app.run(debug = True, host='23.21.52.24', port = 80)
