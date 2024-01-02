#!/bin/python

from flask import Flask, jsonify, request
from flask_cors import cross_origin
from functools import wraps
from auth0.authentication import GetToken
from auth0.management import Auth0
from six.moves.urllib.request import urlopen
from jose import jwt

from dotenv import load_dotenv
import random
import json
import os

import logging
# from datetime import datetime, tzinfo
# from dateutil import tz
# import pytz

logging.basicConfig(level=logging.DEBUG)

logging.info("Start")

# read in the secrets file
load_dotenv()


AUTH0_DOMAIN = os.getenv("AUTH0_DOMAIN")
client_id = os.getenv("AUTH0_CLIENT_ID")
client_secret = os.getenv("AUTH0_CLIENT_SECRET")


app = Flask(__name__)

quotes = [
    "Learn to sell. Learn to build. If you can do both, you will be unstoppable.",
    "Wealth is assets that earn while you sleep",
    "The quality of your mind is the quality of your life.",
    "The only true test of intelligence is if you get what you want out of  life.",
    "Trade money for time, not time for money. You’re going to run out of time    first.",
    "If it entertains you now but will bore you someday, it’s a    distraction. Keep looking.",
    "Don’t do things that you know are morally wrong. Not because someone is watching, but because you are. Self-esteem is just the reputation that you    have with yourself.",
    "Earn with your mind, not your time.",
    "A rational person can find peace by cultivating indifference to things outside of their control.",
    "Someone who is using a lot of fancy words and big concepts probably doesn’t know what they’re talking about. The smartest people can explain things to a child; if you can’t do that, you don’t understand the concept.",
    "A rational person can find peace by cultivating indifference to things outside their control.",
    ]


class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


@app.errorhandler(AuthError)
def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response


def get_token_auth_header():
    """
    Obtains the Access Token from the Authorization Header
    """
    auth = request.headers.get("Authorization", None)
    if not auth:
        raise AuthError({"code": "authorization_header_missing",
                        "description":
                            "Authorization header is expected"}, 401)

    parts = auth.split()

    if parts[0].lower() != "bearer":
        raise AuthError({"code": "invalid_header",
                        "description":
                            "Authorization header must start with"
                            " Bearer"}, 401)
    elif len(parts) == 1:
        raise AuthError({"code": "invalid_header",
                        "description": "Token not found"}, 401)
    elif len(parts) > 2:
        raise AuthError({"code": "invalid_header",
                        "description":
                            "Authorization header must be"
                            " Bearer token"}, 401)

    token = parts[1]
    return token


def requires_auth(f):
    """
    Determines if the Access Token is valid
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        token = get_token_auth_header()
        jsonurl = urlopen("https://"+AUTH0_DOMAIN+"/.well-known/jwks.json")
        jwks = json.loads(jsonurl.read())
        unverified_header = jwt.get_unverified_header(token)
        rsa_key = {}
        for key in jwks["keys"]:
            if key["kid"] == unverified_header["kid"]:
                rsa_key = {
                    "kty": key["kty"],
                    "kid": key["kid"],
                    "use": key["use"],
                    "n": key["n"],
                    "e": key["e"]
                }
        if rsa_key:
            try:
                payload = jwt.decode(
                    token,
                    rsa_key,
                    algorithms=ALGORITHMS,
                    audience=API_IDENTIFIER,
                    issuer="https://"+AUTH0_DOMAIN+"/"
                )
            except jwt.ExpiredSignatureError:
                raise AuthError({"code": "token_expired",
                                "description": "token is expired"}, 401)
            except jwt.JWTClaimsError:
                raise AuthError({"code": "invalid_claims",
                                "description":
                                    "incorrect claims,"
                                    "please check the audience and issuer"}, 401)
            except Exception:
                raise AuthError({"code": "invalid_header",
                                "description":
                                    "Unable to parse authentication"
                                    " token."}, 401)

            _request_ctx_stack.top.current_user = payload
            return f(*args, **kwargs)
        raise AuthError({"code": "invalid_header",
                        "description": "Unable to find appropriate key"}, 401)
    return decorated


@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({'message': 'Hello, World!'})


@app.route('/quotes/all', methods=['GET'])
def get_all_quotes():
    return jsonify(quotes)


@app.route('/quotes/<id>', methods=['GET'])
def get_quotes(id):
    return quotes[int(id)]


@app.route('/quotes/rand', methods=['GET'])
def get_random_quotes():
    random_number = random.randint(1, len(quotes))
    print(random_number)
    return jsonify(quotes[random_number])


@app.route('/quotes/', methods=['POST'])
def add_quotes():
    quotes.append(request.get_json())
    return '', 204


@app.route('/quotes/<id>', methods=['DELETE'])
def delete_quotes(id):
    quotes.pop(int(id))
    return '', 204


@app.route('/quotes/<id>', methods=['PATCH'])
def patch_quotes(id):
    print(request.get_json())
    # current_quote = quotes[int(id)]
    quotes[int(id)] = request.get_json()
    return '', 204


@app.route("/user")
@cross_origin(headers=["Content-Type", "Authorization"])
def user_view():
    """
    User endpoint, can be accessed by authorized user
    """
    return jsonify(msg="Hello user!")


@app.route("/admin")
def admin_view():
    """
    Admin endpoint, can be accessed by admin
    """
    return jsonify(msg="Hello admin!")


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=5010, debug=True)
