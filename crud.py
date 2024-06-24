from sqlalchemy.orm import Session
from model import EventoEsportivo
from schema import EventoEsportivoSchema

def get_evento_esportivo(db: Session, skip=0, limit=100):
    return db.query(EventoEsportivo).offset(skip).limit(limit).all()


def get_envento_esportivo_by_id(db: Session, evento_esportivo_id: int):
    return db.query(EventoEsportivo).filter(EventoEsportivo.id == evento_esportivo_id).first()


def create_evento_esportivo(db: Session, evento_esportivo: EventoEsportivoSchema):
    db_evento_esportivo = EventoEsportivo(
        title=evento_esportivo.title,
        description=evento_esportivo.description,
        date=evento_esportivo.date,
        location=evento_esportivo.location,
        sport=evento_esportivo.sport,
        participants=evento_esportivo.participants,
        price=evento_esportivo.price
    )
    db.add(db_evento_esportivo)
    db.commit()
    db.refresh(db_evento_esportivo)
    return db_evento_esportivo


def remove_evento_esportivo(db: Session, evento_esportivo_id: int):
    db_evento_esportivo = get_envento_esportivo_by_id(db=db, evento_esportivo_id=evento_esportivo_id)
    db.delete(db_evento_esportivo)
    db.commit()
    return db_evento_esportivo


def update_evento_esportivo(db: Session, evento_esportivo_id: int, evento_esportivo: EventoEsportivoSchema):
    db_evento_esportivo = get_envento_esportivo_by_id(db=db, evento_esportivo_id=evento_esportivo_id)
    db_evento_esportivo.title = evento_esportivo.title
    db_evento_esportivo.description = evento_esportivo.description
    db_evento_esportivo.date = evento_esportivo.date
    db_evento_esportivo.location = evento_esportivo.location
    db_evento_esportivo.sport = evento_esportivo.sport
    db_evento_esportivo.participants = evento_esportivo.participants
    db_evento_esportivo.price = evento_esportivo.price
    db.commit()
    db.refresh(db_evento_esportivo)
    return db_evento_esportivo

    