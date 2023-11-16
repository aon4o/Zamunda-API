from datetime import datetime

from sqlalchemy.orm import Session

from models import category as category_model
from schemas import category as category_schema


def list_all(db: Session, skip: int = 0, limit: int = 100):
    return (db.query(category_model.Category)
            .offset(skip)
            .limit(limit)
            .all())


def get(db: Session, category_id: int):
    return (db.query(category_model.Category)
            .get({'id': category_id}))


def create(db: Session, category: category_schema.CreateCategory):
    db_category = category_model.Category(name=category.name, order=category.order)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def update(db: Session, category_id: int, category: category_schema.CreateCategory):
    db_category = get(db, category_id)
    db_category.name = category.name
    db_category.order = category.order
    db_category.updated_at = datetime.now()
    db.commit()
    db.refresh(db_category)
    return db_category


def delete(db: Session, category_id: int):
    db_category = get(db, category_id)
    db.delete(db_category)
    db.commit()
    return None
