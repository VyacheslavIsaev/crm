#!/usr/bin/env python

"""
Author: Viacheslav Isaev
Purpose: Define database which read from plain files.
"""

import json
import logging
import yaml

from db import Database

class FileDB(Database):
    """
    Represent the interface to the data (model).
    """

    def __init__(self, filename):
        self.load_yaml(filename)
        logging.debug(self._data)

    def load_json(self, filename):
        """ Loads json file as database."""
        with open(filename, "r") as filehandle:
            self._data = json.load(filehandle)

    def load_yaml(self, filename):
        """ Loads yaml file. """
        with open(filename, "r") as filehandle:
            self._data = yaml.safe_load(filehandle)
        