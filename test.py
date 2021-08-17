from app import app

def test_case_1():
    response = app.test_client().get('/')
    assert response.status_code == 200


def test_case_2():
    response = app.test_client().get('/edit')
    assert response.status_code == 200


def test_case_3():
    response = app.test_client().get('/edit')
    assert b"Ticketing App" in response.data
    assert b"Add" in response.data