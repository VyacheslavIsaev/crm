#!/usr/bin/env python

"""
Author: Viacheslav Isaev
Purpose: Define DB interface.
"""

from abc import ABC, abstractmethod

class Database(ABC):
    """
    Represent the interface to the data (model). 
    """
    _data = {}

    def balance(self, acct_id):
        """
        Determines the customer balance by finding the difference between
        what has been paid and what is still owed on the account, The "model"
        can provide methods to help interface with the data; it is not
        limited to only storing data. A positive number means the customer
        owes us money and a negative number means they overpaid and have
        a credit with us.
        """
        acct = self._data.get(acct_id)
        if acct:
            return int(acct["due"]) - int(acct["paid"])
        return None
