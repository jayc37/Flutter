from datetime import datetime, timedelta
from flask_restful import Resource
from flask import request,jsonify
import logging
import re
from tofirebase import process_notifi
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------

class GetData(Resource):
    def get(self):
        try:
            data = str(request.args.get('data'))
            format_object = eval(data)
            format_dictionary = dict(format_object)
            process_notifi(format_dictionary)
            return str(format_dictionary), 200
        except Exception as e:
            return 'false', 400