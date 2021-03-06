"""
ORM DB implementation tests.
"""

import pytest

from orm_db import OrmDB
import test_db_body

orm_db = None

@pytest.fixture
def db_mock():
    """ Test fixture """
    return OrmDB("sqlite:///:memory:", "data/db_init.json")


def test_balance(db_mock):
    """ Testing balance method """
    db_mock.connect();
    test_db_body.balance_test_body(db_mock)
    db_mock.disconnect();

def test_owes_money(db_mock):
    """ Testing if user owes money """
    db_mock.connect();
    test_db_body.owes_money_test_body(db_mock)
    db_mock.disconnect();
