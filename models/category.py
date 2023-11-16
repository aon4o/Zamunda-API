from datetime import datetime

from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship

from database import Base


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    order = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.now())
    updated_at = Column(TIMESTAMP, default=datetime.now())

    sub_categories = relationship('SubCategory', back_populates='category')
