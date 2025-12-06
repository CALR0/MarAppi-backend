
from ..extensions import db
from ..models.place import Place
from ..models.category import Category
from ..errors import NotFoundError


def create_place(data):
    name = data.get('name')
    category_id = data.get('category_id')
    if not name or not category_id:
        raise ValueError('name and category_id are required')

    # Basic check that category exists
    cat = Category.query.get(category_id)
    if not cat:
        raise NotFoundError('Category not found')

    place = Place(name=name, description=data.get('description'), category_id=category_id)
    db.session.add(place)
    db.session.commit()
    return place


def get_all_places():
    return Place.query.all()


def get_place(place_id):
    p = Place.query.get(place_id)
    if not p:
        raise NotFoundError('Place not found')
    return p


def update_place(place_id, data):
    p = Place.query.get(place_id)
    if not p:
        raise NotFoundError('Place not found')

    name = data.get('name')
    if name is not None:
        p.name = name

    if 'description' in data:
        p.description = data.get('description')

    if 'category_id' in data:
        # validate category exists
        cat = Category.query.get(data.get('category_id'))
        if not cat:
            raise NotFoundError('Category not found')
        p.category_id = data.get('category_id')

    db.session.commit()
    return p


def delete_place(place_id):
    p = Place.query.get(place_id)
    if not p:
        raise NotFoundError('Place not found')

    db.session.delete(p)
    db.session.commit()
    return True