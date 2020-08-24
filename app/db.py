#!/usr/bin/env python

"""
Author: Viacheslav Isaev
Purpose: Define DB interface.
"""

from abc import ABC

class Database(ABC):
    """
    Represent the interface to the data (model).
    """
    _data = {}

    def get_acct(self, acct_id):
        """
        Returns data dictionary for a specified account.
        """
        return self._data.get(acct_id)

    def balance(self, acct_id):
        """
        Determines the customer balance by finding the difference between
        what has been paid and what is still owed on the account, The "model"
        can provide methods to help interface with the data; it is not
        limited to only storing data. A positive number means the customer
        owes us money and a negative number means they overpaid and have
        a credit with us.
        """
        acct = self.get_acct(acct_id)
        return self.calc_balance(acct)

    def calc_balance(self, acct):
        """
        Calcualte balance from data dictionary.
        """
        if acct:
            bal = float(acct["due"]) - float(acct["paid"])
            return f"{bal:.2f} USD"
        return None

    def owes_money(self, acct_id):
        """
        Return TRUE if account owes money
        """
        acct = self.get_acct(acct_id)
        if acct:
            return float(acct["due"]) > float(acct["paid"])
        return None
