import requests, urllib.parse
from flask import Flask, jsonify, request, json

app = Flask(__name__)

vacances = [
    {
        "date_debut": "2023-03-29T13:56:03.106Z",
        "date_fin": "2023-03-29T13:56:03.106Z",
        "description": "Vacances de la Toussaint",
        "zone": "Zone B"
    }
]

current = True

zone = [
    {
        "nom": "Zone B"
    }
]

user = {
    "id": 10,
    "utilisateurname": "theUtilisateur",
    "zones": [
        {
            "nom": "Zone B"
        }
    ],
    "password": "12345"
}

code200 = "200 Success"


@app.route('/')
def hello_world():  # put application's code here
    return 'Coucou !'


@app.route('/vacances', methods=['GET'])
def getVacances():
    url = "https://data.education.gouv.fr/api/v2/catalog/datasets/fr-en-calendrier-scolaire/records?where=%222022-2023%22%20AND%20%28%22Zone%20A%22%20or%20%22Zone%20B%22%20or%20%22Zone%20C%22%29&limit=100&offset=0&lang=fr&timezone=Europe%2FParis"
    r = requests.request('GET', url)
    data = r.json()
    tab_vac = []

    for item in data["records"]:
        dico = {
            "date_debut": item["record"]["fields"]["start_date"].split("T")[0],
            "date_fin": item["record"]["fields"]["end_date"].split("T")[0],
            "description": item["record"]["fields"]["description"],
            "zone": item["record"]["fields"]["zones"]
        }
        if dico not in tab_vac:
            tab_vac.append(dico)
        else:
            continue
    return tab_vac


@app.route('/vacances/zones/zone', methods=['GET'])
def getVacancesByZone():
    zone = urllib.parse.quote(request.args.to_dict()["zone"])
    url = "https://data.education.gouv.fr/api/v2/catalog/datasets/fr-en-calendrier-scolaire/records?where=%222022" \
          "-2023%22%20AND%20%22{}%22&limit=100&offset=0&lang=fr&timezone=Europe%2FParis".format(zone)
    r = requests.request('GET', url)
    data = r.json()
    tab_vac = []
    # print(json1)
    for record in data["records"]:
        # print(record["record"]["fields"]["description"])
        dico = {
            "date_debut": record["record"]["fields"]["start_date"].split("T")[0],
            "date_fin": record["record"]["fields"]["end_date"].split("T")[0],
            "description": record["record"]["fields"]["description"],
            "zone": record["record"]["fields"]["zones"]
        }
        if dico not in tab_vac:
            tab_vac.append(dico)
        else:
            continue
    return tab_vac


@app.route('/vacances/zones/zones', methods=['POST'])
def getVacancesByZones():
    # rq = request.get_json()
    # TODO
    return jsonify(vacances)


@app.route('/vacances/zones/dates', methods=['POST'])
def getVacancesByDatesAndZone():
    # TODO
    return jsonify(vacances)


@app.route('/vacances/dates', methods=['POST'])
def getVacancesByDates():
    # TODO
    return jsonify(vacances)


@app.route('/vacances/villes/ville', methods=['GET'])
def getVacancesByVille():
    # TODO
    return jsonify(vacances)


@app.route('/vacances/villes/dates', methods=['POST'])
def getVacancesByDatesAndVille():
    # TODO
    return jsonify(vacances)


@app.route('/vacances/adresses/dates', methods=['POST'])
def getVacancesByDatesAndAdresse():
    # TODO
    return jsonify(vacances)


@app.route('/vacances/adresses', methods=['POST'])
def getVacancesByAdresse():
    # TODO
    return jsonify(vacances)


@app.route('/vacances/current/ville', methods=['GET'])
def getStatusByVille():
    # TODO
    return jsonify(current)


@app.route('/vacances/current/adresse', methods=['POST'])
def getStatusByAdresse():
    # TODO
    return jsonify(current)


# a tester


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


@app.route('/utilisateur', methods=['POST'])
def createUser():
    # TODO
    return jsonify(user)


@app.route('/utilisateur/login', methods=['GET'])
def loginUser():
    # TODO
    return jsonify(code200)


@app.route('/utilisateur/logout', methods=['GET'])
def logoutUser():
    # TODO
    return jsonify(code200)


@app.route('/utilisateur/actions/<nom>', methods=['GET', 'PUT', 'PATCH', 'DELETE'])
def getUser(nom):
    # TODO
    match request.method:
        case 'GET':
            return jsonify(user)
        case 'PUT':
            return jsonify(user)
        case 'PATCH':
            return jsonify(user)
        case 'DELETE':
            return jsonify(user)
        case _:
            return jsonify("404")


if __name__ == '__main__':
    app.run(host='0.0.0.0')
