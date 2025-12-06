import pytest


def test_review_crud(app):
    from app.services.category_service import create_category
    from app.services.place_service import create_place
    from app.services.review_service import (
        create_review,
        get_reviews_for_place,
        get_review,
        update_review,
        delete_review,
    )
    from app.errors import NotFoundError

    cat = create_category({"name": "RevCat"})
    p = create_place({"name": "PlaceForRev", "category_id": cat.id})

    # create
    r = create_review({"content": "Good", "rating": 5, "place_id": p.id})
    assert r.id is not None

    # list for place
    reviews = get_reviews_for_place(p.id)
    assert len(reviews) == 1

    # get
    fetched = get_review(r.id)
    assert fetched.id == r.id

    # update
    updated = update_review(r.id, {"content": "Better", "rating": 4})
    assert updated.content == "Better"

    # delete
    delete_review(r.id)

    with pytest.raises(NotFoundError):
        get_review(r.id)
