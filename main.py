from fastapi import FastAPI
import model 
from config import engine
import router

model.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
async def Home():
    return "Hello World"

app.include_router(router.router, prefix="/eventos_esportivos", tags=["eventos_esportivos"])