from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    torrents = relationship('Torrent', back_populates='user')

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    sub_categories = relationship('SubCategory', back_populates='category')

class SubCategory(Base):
    __tablename__ = 'sub_categories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    category_id = Column(Integer, ForeignKey('categories.id'))

    torrents = relationship('Torrent', back_populates='sub_category')

class Torrent(Base):
    __tablename__ = 'torrents'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    sub_category_id = Column(Integer, ForeignKey('sub_categories.id'))

    user = relationship('User', back_populates='torrents')
    sub_category = relationship('SubCategory', back_populates='torrents')
