from tft_tier.app import app
from flask import jsonify
import json

@app.route('/')
def index():
    tier = getJSON('app/../tier.json')
    return jsonify(tier)

def getJSON(path):
   with open(path, 'r') as f:
    return json.load(f)