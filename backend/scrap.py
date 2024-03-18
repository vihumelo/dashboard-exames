import os
import csv
from datetime import datetime
import time
from sqlalchemy.orm import Session
from database import get_db, crud, schemas, globals


#### arquivo
pasta_downloads = os.path.join(os.path.expanduser('~'), 'Downloads')
nome_arquivo = 'Dash_Exames_nao_liberados.csv'
file = os.path.join(pasta_downloads, nome_arquivo)
#######

def crud_update_session(dash: schemas.DashboardBase):
   

    db_session = next(get_db())
    crud.update_comunicacao(db_session, exame=dash.exame, registro=dash.registro, resultado=dash.resultado)
    
    return True

def crud_session(dash: schemas.DashboardBase):

    if dash.exame == 'Neutrófilo - Parcial':

        return False
    
    db_session = next(get_db())
    
    db_check = crud.checking(db_session, exame=dash.exame, registro=dash.registro)
    
    if db_check:

        return False

    crud.insert_dashboard(db=db_session, dash=dash)
    return True

def to_timestamp(data_string, formato="%d/%m/%Y %H:%M"):
    """
    Converte uma string de data para um timestamp.
    """
    data_datetime = datetime.strptime(data_string, formato)
    timestamp = int(data_datetime.timestamp())
    
    return timestamp

 


def csv_to_dict(csv_file):
    with open(csv_file, 'r', newline='', encoding='utf-8-sig') as file:
        csv_reader = csv.DictReader(file)
        data = []
        for row in csv_reader:
            data.append(row)
    return data


def insert_database():
    
    dict_from_csv = csv_to_dict(file)

    try: 
        mudancas = [novo_dado for novo_dado in globals.memory_data if novo_dado not in dict_from_csv]
        for dados in mudancas:
            registro = dados.get('Número_do_Registro')
            exame = dados.get('Exame')
            resultado = dados.get('Resultado')      
            dashboard_data = schemas.DashboardUpdate(
            registro=registro,
            exame=exame,
            resultado=resultado,
            setor = "MOR-Hematologia")
            
            crud_update_session(dash=dashboard_data)
            
    except Exception as rr: 
        print(rr)
        

    globals.memory_data = dict_from_csv
    

    
    for dados in dict_from_csv:
        registro = dados.get('Número_do_Registro')
        hora_execucao = datetime.now()
        hora_coleta = to_timestamp(dados.get('Data_Coleta'))
        exame = dados.get('Exame')
        resultado = dados.get('Resultado')
        comunicacao = 0
    
        dashboard_data = schemas.DashboardBase(
            comunicacao=comunicacao,
            registro=registro,
            hora_execucao=hora_execucao,
            hora_coleta=hora_coleta,
            exame=exame,
            resultado=resultado,
            setor="MOR-Hematologia"
        )

                
        crud_session(dashboard_data)


while True:
    time.sleep(3)
    insert_database()
    x = input('?')
    if x == "S": break
            

