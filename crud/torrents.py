from sqlalchemy.orm import Session

from models import torrent as torrent_model
from schemas import torrent as torrent_schema

def list_all(db: Session, skip: int = 0, limit: int = 100):
    return (db.query(torrent_model.Torrent)
            .offset(skip)
            .limit(limit)
            .all())


def get(db: Session, torrent_id: int):
    return (db.query(torrent_model.Torrent)
            .get({'id': torrent_id}))


def create(db: Session, torrent: torrent_schema.TorrentCreate):
    db_torrent = torrent_model.Torrent(name=torrent.name, description=torrent.description)
    db.add(db_torrent)
    db.commit()
    db.refresh(db_torrent)
    return db_torrent


def update(db: Session, torrent_id: int, torrent: torrent_schema.TorrentCreate):
    db_torrent = get(db, torrent_id)
    db_torrent.name = torrent.name
    db_torrent.description = torrent.description
    db_torrent.updated_at = datetime.now()
    db.commit()
    db.refresh(db_torrent)
    return db_torrent


def delete(db: Session, torrent_id: int):
    db_torrent = get(db, torrent_id)
    db.delete(db_torrent)
    db.commit()
    return None
