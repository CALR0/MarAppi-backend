import json


def test_review_endpoints(client):
    # create category
    rv = client.post(
        "/api/categories", data=json.dumps({"name": "RevCat"}), content_type="application/json"
    )
    cat = rv.get_json()

    # create place
    rv = client.post(
        "/api/places",
        data=json.dumps({"name": "PlaceRev", "category_id": cat["id"]}),
        content_type="application/json",
    )
    place = rv.get_json()

    # create review
    rv = client.post(
        "/api/reviews",
        data=json.dumps({"content": "Nice", "rating": 5, "place_id": place["id"]}),
        content_type="application/json",
    )
    assert rv.status_code == 201
    review = rv.get_json()

    rid = review["id"]

    # list for place
    rv = client.get(f"/api/reviews/place/{place['id']}")
    assert rv.status_code == 200

    # get
    rv = client.get(f"/api/reviews/{rid}")
    assert rv.status_code == 200

    # update
    rv = client.patch(f"/api/reviews/{rid}", data=json.dumps({"rating": 4}), content_type="application/json")
    assert rv.status_code == 200

    # delete
    rv = client.delete(f"/api/reviews/{rid}")
    assert rv.status_code == 204
