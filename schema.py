from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar('T')

class EventoEsportivoSchema(BaseModel):
    id: Optional[int] = None
    title: Optional[str] = None
    description: Optional[str] = None
    date: Optional[str] = None
    location: Optional[str] = None
    sport: Optional[str] = None
    participants: Optional[int] = None
    price: Optional[int] = None

    class Config:
        orm_mode = True

class RequestEventoEsportivo(BaseModel):
    parameter: EventoEsportivoSchema = Field(EventoEsportivoSchema)


class Response (GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]

