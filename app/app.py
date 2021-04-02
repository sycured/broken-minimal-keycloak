#!/usr/bin/env python3

import os
from flask import Flask, redirect
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp

try:
    ISSUER_URL = os.environ["ISSUER_URL"]
    AUTH_URL = os.environ["AUTH_URL"]
    TOKEN_URL = os.environ["TOKEN_URL"]
    USERINFO_URL = os.environ["USERINFO_URL"]
    JWKS_URL = os.environ["JWKS_URL"]
    SECRET_KEY = os.getenv(key='SECRET_KEY', default=None)
except Exception as ex:
    raise

app = Flask(__name__)
app.secret_key = SECRET_KEY


@app.route('/')
def index():
    return 'Hello world!'


@app.route("/login")
def login():
    return redirect(AUTH_URL, code=302)


@app.route("/auth/callback")
def custom_callback():
    return "Logged in!"


if __name__ == "__main__":
    app.run()
