from sqlalchemy.orm import Session
from database import get_db, crud, schemas
from fastapi import Depends, FastAPI, HTTPException
from http import HTTPStatus
from typing import List
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# origins = [
#     "http://localhost:3000", #frontend host
# ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],  
)

@app.get("/dashboard", response_model=List[schemas.Dashboard])
def read_dashboard(skip: int = 0, limit:int = 100, db: Session = Depends(get_db)):
    items = crud.get_dashboard(db, skip, limit)
    
    return items


@app.post("/insert/", response_model=List[schemas.DashboardBase])
def insert_database(dash_list: List[schemas.DashboardBase], db: Session = Depends(get_db)):
    inserted_dashboards = []
    for dash in dash_list:
        if dash.exame == 'Neutrófilo - Parcial':
            raise HTTPException(HTTPStatus.BAD_REQUEST, detail="Exame descartado")
        
        db_check = crud.checking(db, exame=dash.exame, registro=dash.registro)
        if db_check:
            raise HTTPException(HTTPStatus.BAD_REQUEST, detail="Já Registrado")
        
        inserted_dashboards.append(crud.insert_dashboard(db=db, dash=dash))
    
    return inserted_dashboards

@app.post("/update/", response_model=schemas.DashboardUpdate)
def update_database(dash: schemas.DashboardUpdate, db: Session = Depends(get_db)):
    
    update_comunicacao = crud.update_comunicacao(db, exame=dash.exame, registro=dash.registro, resultado=dash.resultado)
    if update_comunicacao:
        
        return update_comunicacao

    else:
        
        raise HTTPException(HTTPStatus.BAD_REQUEST, detail="Erro ao atualizar a comunicação")

@app.post("/notify/", response_model=schemas.DashboardID)
def notify(dash: schemas.DashboardID, db: Session = Depends(get_db)):
    update = crud.notifica_comunicacao(db=db, id=dash.id)
    if update:
        return update  # Retorna o objeto atualizado
    else:
        raise HTTPException(HTTPStatus.BAD_REQUEST, detail="ID Não encontrado")