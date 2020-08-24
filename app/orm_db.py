"""
Database through an ORM
Author: Viacheslav Isaev
"""

import time
import json
from sqlalchemy import create_engine, Table, Column, Float, String, MetaData

from db import Database

class OrmDB(Database):
    """
    Implements DB functinality through ORM.
    """
    _retries = 10
    _retry_timeout = 5
    _table  = None
    _result = None
    _conn   = None

    def __init__(self, db_url, json_file_path):
        """ Initializes ORM and connects to DB server instance. """
        super().__init__()
        self.init_db(db_url)
        self.force_connection()
        self.init_db_with_json_file(json_file_path)

    def init_db(self, db_url):
        """ Initializes ORM """
        self._engine = create_engine(db_url)
        self._meta = MetaData(self._engine)
        self.create_table()
        self._meta.create_all()

    def force_connection(self):
        """ Forcefull connection with retries. """
        for _ in range(self._retries):
            try:
                self.connect()
                break
            except:
                time.sleep(self._retry_timeout)
        if not self.is_connected:
            raise TimeoutError("Could not establish session to mysql db.")

    def is_connected(self):
        """ Checks if we are connected. """
        return hasattr(self, "_conn") or not self._conn.closed

    def create_table(self):
        """ Creates table. """
        self._table = Table(
            "account",
            self._meta,
            Column("acctid", String(15), primary_key=True),
            Column("paid",   Float,      nullable=False),
            Column("due",    Float,      nullable=False)
        )

    def init_db_with_json_file(self, json_file_path):
        """ Initialize DB with data from JSON file. """
        with open(json_file_path, "r") as file_handle:
            data = json.load(file_handle)
            self.init_db_with_json(data)

    def init_db_with_json(self, json_data):
        """ Initialize DB with data from JSON object. """
        self._result = self._conn.execute(self._table.insert(), json_data)

    def connect(self):
        """ Connects to DB. """
        self._conn = self._engine.connect()
        if self._conn.closed:
            raise OSError("connect() returned but seesion is closed.")

    def disconnect(self):
        """ Disconnect from DB. """
        if self.is_connected():
            self._conn.close()
            if not self._conn.closed:
                raise OSError("close() returned but session is still opened.")

    def get_acct(self, acct_id):
        """
        Overwrites default functionality.
        """
        select_acct_balance = self._table.select().where(
            self._table.c.acctid == acct_id.upper()
        )
        result = self._conn.execute(select_acct_balance)
        return result.fetchone()
