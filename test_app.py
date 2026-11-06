from app import app  # import the Flask app to test it


def test_home():
    client = app.test_client()  # fake client, no real server needed
    response = client.get("/")  # call the home page
    assert response.status_code == 200  # page must load successfully


def test_health():
    client = app.test_client()
    response = client.get("/health")  # call the health endpoint
    assert response.get_json() == {"status": "ok"}  # must return ok status
