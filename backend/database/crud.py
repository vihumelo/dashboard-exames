from sqlalchemy.orm import Session
from database import models, schemas


def get_dashboard(db: Session, skip: int = 0, limit: int = 100):

    return db.query(models.Dashboard).offset(skip).limit(limit).all()

def insert_dashboard(db: Session, dash: schemas.DashboardBase):

    db_user = models.Dashboard(
        comunicacao=dash.comunicacao,
        registro=dash.registro,
        hora_execucao=dash.hora_execucao,
        hora_coleta=dash.hora_coleta,
        exame=dash.exame,
        setor=dash.setor,
        resultado=dash.resultado)
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_comunicacao(db: Session, registro: str, exame: str, resultado: str, comunicacao: int = 1):
    db_dashboard = db.query(models.Dashboard).filter(
        models.Dashboard.exame == exame,
        models.Dashboard.registro == registro,
        models.Dashboard.resultado == resultado
    ).first()
    if db_dashboard:
        db_dashboard.comunicacao = comunicacao
        db.commit()
        db.refresh(db_dashboard)
        return db_dashboard
    
def notifica_comunicacao(db: Session, id: int, comunicacao: int = 1):
    db_dashboard = db.query(models.Dashboard).filter(
        models.Dashboard.id == id,
    ).first()
    if db_dashboard:
        db_dashboard.comunicacao = comunicacao
        db.commit()
        db.refresh(db_dashboard)
        return db_dashboard
    


def checking(db: Session, exame: str, registro: str):
    return db.query(models.Dashboard).filter(
        models.Dashboard.exame == exame,
        models.Dashboard.registro == registro
    ).first()
    

