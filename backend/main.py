from sqlalchemy.orm import Session
from database import get_db, crud, schemas
from fastapi import Depends, FastAPI, HTTPException
from http import HTTPStatus
from typing import List
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost:3000", #frontend host
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],  
)

@app.get("/dashboard", response_model=List[schemas.Dashboard])
def read_dashboard(skip: int = 0, limit:int = 100, db: Session = Depends(get_db)):
    items = crud.get_dashboard(db, skip, limit)
    
    return items

@app.post("/scraped/", response_model=schemas.DashboardBase)
def insert_database(dash: schemas.DashboardBase, db: Session = Depends(get_db)):
    
    if dash.exame == 'Neutrófilo - Parcial':
        raise HTTPException(HTTPStatus.BAD_REQUEST, detail="Exame descartado")
        
    db_check = crud.checking(db, exame=dash.exame, registro=dash.registro)
    if db_check:
        raise HTTPException(HTTPStatus.BAD_REQUEST, detail="Registrado")
    
    return crud.insert_dashboard(db=db, dash=dash)

@app.post("/notify/", response_model=schemas.DashboardID)
def notify(dash: schemas.DashboardID, db: Session = Depends(get_db)):
    update = crud.notifica_comunicacao(db=db, id=dash.id)
    if update:
        return update  # Retorna o objeto atualizado
    else:
        raise HTTPException(HTTPStatus.BAD_REQUEST, detail="ID Não encontrado")