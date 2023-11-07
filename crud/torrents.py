from sqlalchemy.orm import Session

from models import torrent as models
from schemas import torrent as schemas


def get_torrents(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Torrent).offset(skip).limit(limit).all()


def create_user_torrent(db: Session, torrent: schemas.TorrentCreate, user_id: int):
    db_torrent = models.Torrent(**torrent.dict(), owner_id=user_id)
    db.add(db_torrent)
    db.commit()
    db.refresh(db_torrent)
    return db_torrent
