import pytest 

import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))
from main import app


def test_home_page():
    """
    GIVEN a Flask application
    WHEN the '/' page is requested (GET)
    THEN check the response is valid
    """
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert b"Hello Ridgemap World!!!" in response.data

def test_ridge_map():
    response = app.test_client().get('/ridge_map?inputcoords=-3.529,54.1743,-2.5128,54.6998&label=Lakes')
    assert response.status_code == 200
    assert response.mimetype == 'image/png'
