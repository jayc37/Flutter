from flask import Flask,jsonify
from flask import render_template, request
from flask_restful import Api
from flask_cors import CORS
import json
import os.path
import logging
import os
from tofirebase import process_notifi,delete_collection
from tofirebase import *
from firebase_admin import credentials, firestore, initialize_app
from thesis import GetData
from flask_jwt_extended import JWTManager, jwt_required, create_access_token

# ------------------------------------------------------------------------------
app = Flask(__name__)
jwt = JWTManager(app)
# for develop
app.config["JWT_SECRET_KEY"] = "sTrOnG!StR0Gg@P4sSvv(!)r"
app.debug = True
api = Api(app)
CORS(app)

# for develop
logging.basicConfig(level = logging.INFO)

# thesis
api.add_resource(GetData, '/getData') # get

db = firestore.client()
todo_ref = db.collection('khaosatkh')
tokens = db.collection('fcm-token')
#firebase store
#
@app.route('/api/v1/add', methods=['POST'])
def create():
    try:
        devicename = request.json['device']
        auth_devicename = tokens.document(devicename).get()._data
        if auth_devicename:
            access_token = create_access_token(identity=devicename)
            process_notifi(request.json)
        return jsonify({"success": True},access_token=access_token), 200

    except Exception as e:
        return f"An Error Occured: {e}"
#
if __name__ == "__main__":
  app.run()