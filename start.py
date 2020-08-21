#!/usr/bin/env python

"""
Author: Nick Russo
Purpose: A simple Flask web app that demonstrates the Model View Controller
(MVC) pattern in a meaningful and somewhat realistic way.
"""

from flask import Flask, render_template, request
from static_db import StaticDB
from file_db import FileDB

# Create Flask object and instantiate database object
app = Flask(__name__)

db_file = "data/data.json"
db = FileDB(db_file)
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

def processPost(request):
    # This collects the user input from the view. The controller's job
    # is to process this information, which includes using methods from
    # the "model" to get the information we need (in this case,
    # the account balance).
    acct_id = request.form["acctid"]
    acct_balance = db.balance(acct_id.upper())
    app.logger.debug(f"balance for {acct_id}: {acct_balance}")
    return acct_balance

def processGet(request):
    # During a normal GET request, no need to perform any calculations
    return "N/A"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
