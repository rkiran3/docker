import os
import pytest

import main

@pytest.fixture
def client():
    main.app.testing = True
    return main.app.test_client()

def test_handler_no_env_variable(client):
    r = client.get("/")

    assert r.data.decode() == '{"message":"Hello, World!"}\n'
    assert r.status_code == 200
