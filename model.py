from sqlalchemy import Column, Integer, String
from config import Base


class EventoEsportivo(Base):
    __tablename__ = "eventos_esportivos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    date = Column(String)
    location = Column(String)
    sport = Column(String)
    participants = Column(Integer)
    price = Column(Integer)
    
