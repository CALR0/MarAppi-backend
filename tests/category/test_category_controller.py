import json


def test_category_endpoints(client):
    # create
    rv = client.post(
        "/api/categories", data=json.dumps({"name": "API-Test"}), content_type="application/json"
    )
    assert rv.status_code == 201
    data = rv.get_json()
    assert data["name"] == "API-Test"

    cid = data["id"]

    # list
    rv = client.get("/api/categories")
    assert rv.status_code == 200
    lst = rv.get_json()
    assert any(x["id"] == cid for x in lst)

    # get
    rv = client.get(f"/api/categories/{cid}")
    assert rv.status_code == 200

    # update
    rv = client.put(
        f"/api/categories/{cid}", data=json.dumps({"name": "API-New"}), content_type="application/json"
    )
    assert rv.status_code == 200
    assert rv.get_json()["name"] == "API-New"

    # delete
    rv = client.delete(f"/api/categories/{cid}")
    assert rv.status_code == 204
