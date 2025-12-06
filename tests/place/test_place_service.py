import pytest


def test_place_crud(app):
    from app.services.category_service import create_category
    from app.services.place_service import (
        create_place,
        get_all_places,
        get_place,
        update_place,
        delete_place,
    )
    from app.errors import NotFoundError

    cat = create_category({"name": "PlacesCat"})

    # create
    p = create_place({"name": "My Place", "category_id": cat.id, "description": "desc"})
    assert p.id is not None

    # list
    allp = get_all_places()
    assert len(allp) == 1

    # get
    fetched = get_place(p.id)
    assert fetched.id == p.id

    # update
    updated = update_place(p.id, {"name": "NewPlace"})
    assert updated.name == "NewPlace"

    # change category
    newcat = create_category({"name": "OtherCat"})
    updated = update_place(p.id, {"category_id": newcat.id})
    assert updated.category_id == newcat.id

    # delete
    delete_place(p.id)

    with pytest.raises(NotFoundError):
        get_place(p.id)
