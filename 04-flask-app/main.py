#!/bin/python
from flask import Flask, jsonify
# for loading secrets file
from dotenv import load_dotenv

import os
import json
import logging
# from datetime import datetime, tzinfo
# from dateutil import tz
# import pytz

logging.basicConfig(level=logging.DEBUG)

logging.info("Start")

# read in the secrets file
load_dotenv()

api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")

logging.info(f" API_KEY: {api_key}")
logging.info(f" API_SECRET: {api_secret}")


app = Flask(__name__)

fname = "./metra.json"
with open(fname) as inpfile:

    # returns JSON object
    chunks = json.load(inpfile)


# Get list of all trains in a route name Ex: "BNSF" and Number "1236"
def getTrainsWithLabel(routeId, label):
    trains = []
    for chunk in chunks:
        # logging.debug("Found Chunk: " + chunk["id"])

        if "trip_update" in chunk:
            # trip_update:trip json
            trip_update = chunk["trip_update"]

            if "vehicle" in trip_update:
                vehicle = trip_update["vehicle"]
                if vehicle is not None:
                    if vehicle["label"] == label:
                        trains.append(chunk)
    return trains


# Get list of all trains in a route Ex: "BNSF"
def getTrains(routeId):
    trains = []

    for chunk in chunks:
        # logging.debug("Found Chunk: " + chunk["id"])

        if "trip_update" in chunk:
            # trip_update:trip json
            trip_update = chunk["trip_update"]

            if "trip" in trip_update:
                trip = trip_update["trip"]
                if "route_id" in trip:
                    route_id = trip["route_id"]
                if "trip_id" in trip:
                    trip_id = trip["trip_id"]
                    print(trip_id)
                # logging.debug(
                #    "Route id: [{}] trip_id [{}]".format(route_id, trip_id))

                if (route_id == routeId):
                    trains.append(chunk)

    return trains


@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({'message': 'Hello, World!'})

@app.route('/ping')
def ping():
    return "pong"


@app.route('/routes/<string:route>', methods=['GET'])
def returnAll(route):
    trains = getTrains(route)
    return jsonify(trains)


@app.route('/routes/<string:route>/<string:label>', methods=['GET'])
def returnTrainWithLabel(route, label):
    trains = getTrainsWithLabel(route, label)
    return jsonify(trains)


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=5000, debug=True)
