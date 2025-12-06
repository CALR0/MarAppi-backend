
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
    return Place.query.get(place_id)