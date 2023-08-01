import os
import re
from flask import Flask, Response
from flask import request

app = Flask(__name__)

@app.route("/",methods=['post','get'])
def home():
    text=str(request.headers)+request.get_data().decode('utf-8')
    print(re.sub('\r?\n', ',,', text), flush=True)
    return Response(text, status=200, mimetype='application/json')

app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
