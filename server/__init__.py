from flask import *
from flask_restful import *
from flask_restful import reqparse
from server.db.auth import *

app = Flask(__name__)
app.debug = True
app.secret_key = "RANUGA D 2008"
api = Api(app)

from server.rest_api import *
