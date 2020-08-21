#!/usr/bin/env python

"""
Author: Nick Russo
Purpose: A simple Flask web app that demonstrates the Model View Controller
(MVC) pattern in a meaningful and somewhat realistic way.
"""

from db import Database

class StaticDB(Database):
    """
    Represent the interface to the data (model). Uses statically-defined
    data to keep things simple for now.
    """

    def __init__(self):
        """
        Constructor to initialize the data attribute as
        a dictionary where the account number is the key and
        the value is another dictionary with keys "paid" and "due".
        """

        self._data = {
            "ACCT100": {"paid": 60, "due": 100}, # balance = 40
            "ACCT200": {"paid": 70, "due": 60},  # balance = -10
            "ACCT300": {"paid": 0,  "due": 0},   # balance = 0
        }