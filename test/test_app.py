def test_home(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Hello, World!"
    }


def test_about(client):
    response = client.get("/about")

    assert response.status_code == 200