#!/usr/bin/env python

"""
Author" Viacheslav Isaev
Idea by: Nick Russo
Purpose: A simple Flask web app that demonstrates the Model View Controller
(MVC) pattern in a meaningful and somewhat realistic way.
"""
import os

from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
from file_db import FileDB

CERT_PATH = "./certs"

# Create Flask object and instantiate database object
app = Flask(__name__)
csrf = CSRFProtect(app)

DB_FILE = "data/data.json"
db = FileDB(DB_FILE)
acct_balance = "N/A"

@app.route("/", methods=["GET", "POST"])
def index():
    """
    This is a view function which responds to requests for the top-level
    URL. It serves as the "controller" in MVC as it accesses both the
    model and the view.
    """

    # The button click within the view kicks off a POST request ...
    if request.method == "POST":
        acct_balance = processPost(request)
    else:
        acct_balance = processGet(request)

    # This is the "view", which is the jinja2 templated HTML data that is
    # presented to the user. The user interacts with this webpage and
    # provides information that the controller then processes.
    # The controller passes the account balance into the view so it can
    # be displayed back to the user.
    return render_template("index.html", acct_balance=acct_balance)

def processPost(req):
    """
    This collects the user input from the view. The controller's job
    is to process this information, which includes using methods from
    the "model" to get the information we need (in this case,
    the account balance).
    """
    acct_id = req.form["acctid"]
    acct_balance = db.balance(acct_id.upper())
    app.logger.debug(f"balance for {acct_id}: {acct_balance}")
    return acct_balance

def processGet(req):
    """
    During a normal GET request, no need to perform any calculations
    """
    return "N/A"

if __name__ == "__main__":
    # 2 tupel to save certificate and key
    ctx = (f"{CERT_PATH}/cert.pem", f"{CERT_PATH}/key.pem")

    # Assignign random flask secret key
    app.secret_key = os.urandom(24)
    app.run(host="0.0.0.0", 
        debug=True, 
        use_reloader=False, 
        ssl_context=ctx) #nosec
