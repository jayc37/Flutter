
from firebase_admin import credentials, firestore, initialize_app
from flask import Flask, jsonify, request
#firebase store 
cred = credentials.Certificate('key.json')
default_app = initialize_app(cred)
db = firestore.client()
todo_ref = db.collection('authentication')
all_todos = [doc.to_dict() for doc in todo_ref.stream()]

