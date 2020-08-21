#!/usr/bin/env python

"""
Author: Viacheslav Isaev
Purpose: Define database which read from plain files.
"""

from db import Database

class FileDB(Database):
    """
    Represent the interface to the data (model). 
    """

    def __init__(self, filename):

        with open(path, "r") as filehandle:
            import json
            self._data = json.load(filehandle)