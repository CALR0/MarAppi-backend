from ..extensions import db
from ..models.category import Category


def create_category(data):
    name = data.get('name')
    if not name:
        raise ValueError('name is required')

    category = Category(name=name)
    db.session.add(category)
    db.session.commit()
    return category


def get_all_categories():
    return Category.query.all()


def get_category(category_id):
    return Category.query.get(category_id)