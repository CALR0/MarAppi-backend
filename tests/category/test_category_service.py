import pytest


def test_category_crud(app):
    from app.services.category_service import (
        create_category,
        get_all_categories,
        get_category,
        update_category,
        delete_category,
    )
    from app.errors import NotFoundError

    # create
    c = create_category({"name": "Test"})
    assert c.id is not None
    assert c.name == "Test"

    # list
    allcats = get_all_categories()
    assert len(allcats) == 1

    # get
    fetched = get_category(c.id)
    assert fetched.id == c.id

    # update
    updated = update_category(c.id, {"name": "NewName"})
    assert updated.name == "NewName"

    # delete
    delete_category(c.id)

    with pytest.raises(NotFoundError):
        get_category(c.id)
