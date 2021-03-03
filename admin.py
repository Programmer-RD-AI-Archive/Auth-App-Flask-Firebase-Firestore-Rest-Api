import firebase_admin
from firebase_admin import credentials, firestore

config = {}
cred = credentials.Certificate(config)
firebase_admin.initialize_app(cred)
db = firestore.client()
doc_ref = db.collection("auth rest api").stream()
for doc in doc_ref:
    print("\n User Auth Info \n")
    print(doc.to_dict())
    print("\n User Auth Info \n")
print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
print("*"*50)
print("*"*50)
print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
doc_ref_ = db.collection("info rest api").stream()
for doc in doc_ref_:
    print("\n User Info \n")
    print(doc.to_dict())
    print("\n User Info \n")
