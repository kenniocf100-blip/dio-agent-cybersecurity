import pytest

from app_vulnerable import app as vulnerable_app
from app_fixed import app as fixed_app

@pytest.mark.parametrize("app", [vulnerable_app, fixed_app])
def test_valid_login_succeeds(app):
    response = app.test_client().post(
        "/login",
        json={"username": "admin", "password": "correct-horse-battery"},
    )
    assert response.status_code == 200
    assert response.get_json()["authenticated"] is True

def test_vulnerable_app_demonstrates_sql_injection():
    response = vulnerable_app.test_client().post(
        "/login",
        json={"username": "admin' -- ", "password": "wrong"},
    )
    assert response.status_code == 200
    assert response.get_json()["authenticated"] is True

def test_fixed_app_rejects_same_injection_input():
    response = fixed_app.test_client().post(
        "/login",
        json={"username": "admin' -- ", "password": "wrong"},
    )
    assert response.status_code == 401
    assert response.get_json()["authenticated"] is False
