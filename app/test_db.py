""" Database functionality test """
import pytest

import file_db
import test_db_body

@pytest.fixture
def db_mock():
    """ Test fixture """
    return file_db.FileDB("data/data.json")

def test_balance(db_mock):
    """ Testing balance method """
    test_db_body.balance_test_body(db_mock)

def test_owes_money(db_mock):
    """ Testing if user owes money """
    test_db_body.owes_money_test_body(db_mock)
