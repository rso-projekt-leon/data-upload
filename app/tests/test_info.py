import json


def test_info(test_app):
    client = test_app.test_client()
    resp = client.get("/v1/demo/info")
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert "ls4262" in data["clani"][0]
    assert "Projekt implementira platformo za podatkovno analizo." in data["opis_projekta"]
