import firebase_admin
from firebase_admin import credentials, firestore
import firebase_admin
from firebase_admin import credentials, firestore
from server.db.add_info import *
import requests
from server.db.send_email import *

config = {}
cred = credentials.Certificate(config)
firebase_admin.initialize_app(cred)
db = firestore.client()


def add_info(info):
    doc_ref = db.collection("info rest api").document()
    doc_ref.set(info)
