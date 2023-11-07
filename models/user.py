from datetime import datetime

from sqlalchemy import Boolean, Column, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP, default=datetime.now())
    updated_at = Column(TIMESTAMP, default=datetime.now())

    torrents = relationship('Torrent', back_populates='user')
