import requests, urllib.parse
from flask import Flask, jsonify, request, json
app = Flask(__name__)

zone = [
    {
        "nom": "Zone B"
    }
]


@app.route('/')
def accueil():
    return "Bonjour"


@app.route('/zones', methods=['GET'])
def getZones():
    # TODO
    return jsonify(zone)


@app.route('/zones/villes', methods=['GET'])
def getZonesByVille():
    # TODO
    return jsonify(zone)


@app.route('/zones/adresses', methods=['POST'])
def getZonesByAdresse():
    # TODO
    return jsonify(zone)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)