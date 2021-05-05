import os
import tempfile

import pytest
from flask_apis import create_app

@pytest.fixture
def app():
    app = create_app({
        'TESTING': True,
    })
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()
    
@pytest.fixture
def input_name():
    return "adidas tshirt men size XL"