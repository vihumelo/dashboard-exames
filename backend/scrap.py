import os
import csv
from datetime import datetime
import time
import requests
from database import globals

#### arquivo
pasta_downloads = os.path.join(os.path.expanduser('~'), 'Downloads')
nome_arquivo = 'Dash_Exames_nao_liberados.csv'
file = os.path.join(pasta_downloads, nome_arquivo)
#######

#### endpoints

URL = "http://localhost:8000"  # Substitua pela URL da sua aplicação
UPDATE_ENDPOINT = "/update/"
INSERT_ENDPOINT = "/insert/"

#######

def to_timestamp(data_string, formato="%d/%m/%Y %H:%M"):
    """
    Converte uma string de data para um timestamp.
    """
    data_datetime = datetime.strptime(data_string, formato)
    timestamp = data_datetime.isoformat()
    
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
    
    if dict_from_csv != globals.memory_data:

        try: 
            mudancas = [novo_dado for novo_dado in globals.memory_data if novo_dado not in dict_from_csv]
            post_update_list = []
            for dados in mudancas:
                registro = dados.get('Número_do_Registro')
                exame = dados.get('Exame')
                resultado = dados.get('Resultado')      

                data_update = {"exame": exame, "registro": registro, "resultado": resultado}
                post_update_list.append(data_update)
                
            
            if post_update_list:    
                response = requests.post(URL + UPDATE_ENDPOINT, json=post_update_list)
                if response.status_code == 200: pass
                else:
                    print(f'Erro na função update: {response.json()} - registro: {registro}')
                
        except Exception as rr: 
            print(rr)
            

        globals.memory_data = dict_from_csv
        

        postlist = []
        for dados in dict_from_csv:
            registro = dados.get('Número_do_Registro')
            hora_execucao = datetime.now().isoformat()
            hora_coleta = to_timestamp(dados.get('Data_Coleta'))
            exame = dados.get('Exame')
            resultado = dados.get('Resultado')
            comunicacao = 0
            setor = "MOR-Hematologia"
            
            data = {"comunicacao": comunicacao, "registro": registro,
                    "hora_execucao": hora_execucao, "hora_coleta": hora_coleta,
                    "hora_coleta": hora_coleta, "exame": exame, 
                    "resultado": resultado, "setor": setor}
            
            postlist.append(data)
            

        response = requests.post(URL + INSERT_ENDPOINT, json=postlist)
        print(f'{response.json()} - registro: {registro}')

    # os.remove(file)
                


while True:
    time.sleep(1)
    insert_database()
    x = input('?')
    if x == "S": break
            

