from datetime import datetime

from sqlalchemy import Column, ForeignKey, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship

from database import Base


class SubCategory(Base):
    __tablename__ = 'sub_categories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    order = Column(Integer, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'))
    created_at = Column(TIMESTAMP, default=datetime.now())
    updated_at = Column(TIMESTAMP, default=datetime.now())

    category = relationship('Category', back_populates='sub_categories')
    torrents = relationship('Torrent', back_populates='sub_category')
