import json


def test_place_endpoints(client):
    # create a category first
    rv = client.post(
        "/api/categories", data=json.dumps({"name": "PlacesCat"}), content_type="application/json"
    )
    assert rv.status_code == 201
    cat = rv.get_json()

    # create place
    rv = client.post(
        "/api/places",
        data=json.dumps({"name": "API Place", "category_id": cat["id"], "description": "d"}),
        content_type="application/json",
    )
    assert rv.status_code == 201
    place = rv.get_json()
    pid = place["id"]

    # list
    rv = client.get("/api/places")
    assert rv.status_code == 200

    # get
    rv = client.get(f"/api/places/{pid}")
    assert rv.status_code == 200

    # update
    rv = client.patch(
        f"/api/places/{pid}", data=json.dumps({"name": "API-Updated"}), content_type="application/json"
    )
    assert rv.status_code == 200

    # delete
    rv = client.delete(f"/api/places/{pid}")
    assert rv.status_code == 204
