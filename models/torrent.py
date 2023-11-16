from datetime import datetime

from sqlalchemy import Column, ForeignKey, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship

from database import Base


class Torrent(Base):
    __tablename__ = 'torrents'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    image = Column(String, nullable=True)
    file = Column(String)
    times_downloaded = Column(Integer, default=0)
    user_id = Column(Integer, ForeignKey('users.id'))
    sub_category_id = Column(Integer, ForeignKey('sub_categories.id', ondelete='CASCADE'), index=True, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.now())
    updated_at = Column(TIMESTAMP, default=datetime.now())

    user = relationship('User')
    sub_category = relationship('SubCategory', back_populates='torrents')
