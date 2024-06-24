from fastapi import APIRouter, HTTPException, Path, Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schema import EventoEsportivoSchema, RequestEventoEsportivo, Response
import crud

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
async def get_all(db: Session = Depends(get_db)):
    eventos = crud.get_evento_esportivo(db, skip=0, limit=100)
    return Response(code="200", status="Ok", message="Eventos esportivos retornados com sucesso", result=eventos).dict(exclude_none=True)

@router.get("/{id}")
async def get_by_id(id: int, db: Session = Depends(get_db)):
    evento = crud.get_envento_esportivo_by_id(db, evento_esportivo_id=id)
    return Response(code="200", status="Ok", message="Evento esportivo retornado com sucesso", result=evento).dict(exclude_none=True)

@router.post("/create")
async def create(request: RequestEventoEsportivo,db: Session = Depends(get_db)):
    evento = crud.create_evento_esportivo(db, request.parameter)
    return Response(code="200", status="Ok", message="Evento esportivo criado com sucesso", result=evento).dict(exclude_none=True)

@router.post("/update")
async def update(request: RequestEventoEsportivo, db: Session = Depends(get_db)):
    evento = crud.update_evento_esportivo(db, evento_esportivo_id=request.parameter.id, evento_esportivo=request.parameter)
    return Response(code="200", status="Ok", message="Evento esportivo atualizado com sucesso", result=evento).dict(exclude_none=True)

@router.delete("/{id}")
async def deleter(id: int, db: Session = Depends(get_db)):
    evento = crud.remove_evento_esportivo(db, evento_esportivo_id=id)
    return Response(code="200", status="Ok", message="Evento esportivo deletado com sucesso", result=evento).dict(exclude_none=True)