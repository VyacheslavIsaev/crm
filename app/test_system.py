"""
System test.
"""

import requests

TEST_URL = "http://localhost"

TEST_PORTS = [8050]

def get_headers():
    """ Generate GET headers """
    return {"Accept": "text/html"}

def post_headers():
    """ Generate POST headers """
    p = get_headers()
    p["Content-Type"]="application/x-www-form-urlencoded"
    return p

def assert_get_correct_page(host_url, port):
    """
    Sunny case scenario
    """
    resp = requests.get(f"{host_url}:{port}", headers=get_headers())
    assert resp.status_code == 200
    assert "Enter account ID" in resp.text

def test_get_correct_page_all():
    """ Run get_correct_page for all ports """
    for port in TEST_PORTS:
        assert_get_correct_page(TEST_URL, port)

def assert_get_bad_page(host_url, port):
    """
    Wrong page requested
    """
    resp = requests.get(f"{host_url}:{port}/bad.html", headers=get_headers())
    assert resp.status_code == 404
    assert "Not Found" in resp.text

def test_get_wrong_page_all():
    """ Run get wrong page for all ports """
    for port in TEST_PORTS:
        assert_get_bad_page(TEST_URL, port)

def assert_post_acct(url, port, acct, expected):
    """ Assert for POST request """
    resp = requests.post(f"{url}:{port}", headers=post_headers(), data=f"acctid={acct}")
    assert resp.status_code == 200
    if expected:
        assert f"Account balance: {expected}" in resp.text
    else:
        assert "Unknown account number" in resp.text

def assert_post_acct_all(acct, expected=None):
    """
    Helper function to test expected balance.
    """
    for port in TEST_PORTS:
        assert_post_acct(TEST_URL, port, acct, expected)

def test_post_correct_acct():
    """
    Testing balance request for correct IDs.
    """
    assert_post_acct_all("ACCT100", "40.00 USD")

def test_post_wrong_acct():
    """
    Testing balance request for correct IDs.
    """
    assert_post_acct_all("bbllaa")
