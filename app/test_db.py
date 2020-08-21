""" Database functionality test """
import pytest
import file_db

CURRENCY = "USD"

@pytest.fixture
def db_mock():
    """ Test fixture """
    return file_db.FileDB("app/data/data.json")

def assert_balance(db_mock, account, val):
    """ Assert test helper for balance function"""
    assert db_mock.balance(account) == (f"{val:.2f}"+" "+CURRENCY)

def assert_none(value):
    assert value is None

def test_balance(db_mock):
    """ Testing balance method """
    assert_balance(db_mock, "ACCT100", 40.00)
    assert_balance(db_mock, "ACCT200", -10.00)
    assert_balance(db_mock, "ACCT300", 0.00)
    assert_none(db_mock.balance("blablaInc"))

def test_owes_money(db_mock):
    """ Testing if user owes money """
    assert db_mock.owes_money("ACCT100")
    assert not db_mock.owes_money("ACCT200")
    assert not db_mock.owes_money("ACCT300")
    assert_none(db_mock.owes_money("blablaInc"))