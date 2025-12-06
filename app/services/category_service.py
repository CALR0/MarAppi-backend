from ..extensions import db
from ..models.category import Category
from ..errors import NotFoundError


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
    cat = Category.query.get(category_id)
    if not cat:
        raise NotFoundError('Category not found')
    return cat


def update_category(category_id, data):
    cat = Category.query.get(category_id)
    if not cat:
        raise NotFoundError('Category not found')

    name = data.get('name')
    if name is not None:
        cat.name = name

    db.session.commit()
    return cat


def delete_category(category_id):
    cat = Category.query.get(category_id)
    if not cat:
        raise NotFoundError('Category not found')

    db.session.delete(cat)
    db.session.commit()
    return True