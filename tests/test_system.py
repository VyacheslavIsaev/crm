"""
System test.
"""

import requests
from bs4 import BeautifulSoup

TEST_URL = "https://localhost"

TEST_PORTS = [8050]

def get_headers():
    """ Generate GET headers """
    return {"Accept": "text/html"}

def post_headers():
    """ Generate POST headers """
    p = get_headers()
    p["Content-Type"]="application/x-www-form-urlencoded"
    return p

def build_get_args(url):
    requests.packages.urllib3.disable_warnings()
    return {
        "url": url,
        "headers": get_headers(),
        "verify":  False
    }

def build_post_args(url):
    args = build_get_args(url)
    args["headers"] = post_headers()
    return args

def assert_get_correct_page(host_url, port):
    """
    Sunny case scenario
    """
    args = build_get_args(f"{host_url}:{port}")
    resp = requests.get(**args)
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
    args = build_get_args(f"{host_url}:{port}/bad.html")
    resp = requests.get(**args)
    assert resp.status_code == 404
    assert "Not Found" in resp.text

def test_get_wrong_page_all():
    """ Run get wrong page for all ports """
    for port in TEST_PORTS:
        assert_get_bad_page(TEST_URL, port)

def assert_post_acct(url, port, acct, expected):
    """ Assert for POST request """
    s = requests.session()
    args = build_get_args(f"{url}:{port}")
    resp = s.get(**args)
    assert resp.status_code == 200
    dom = BeautifulSoup(resp.text, 'html.parser')
    csrf = dom.find("input", {"name": "csrf_token"})
    data = f"acctid={acct}"
    if not csrf is None:
        csrf_token = csrf["value"]
        data = f"acctid={acct}&csrf_token={csrf_token}"
    args = build_post_args(f"{url}:{port}")    
    resp = s.post(**args, data=data)
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
