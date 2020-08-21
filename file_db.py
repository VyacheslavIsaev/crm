#!/usr/bin/env python

"""
Author: Viacheslav Isaev
Purpose: Define database which read from plain files.
"""

import json
from db import Database
import logging



class FileDB(Database):
    """
    Represent the interface to the data (model).
    """

    def __init__(self, filename):
        self.load_json(filename)
        logging.debug(self._data)

    def load_json(self, filename):
        """ Loads json file as database."""
        with open(filename, "r") as filehandle:
            self._data = json.load(filehandle)
