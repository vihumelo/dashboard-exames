from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Obtém o diretório raiz do projeto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define o caminho para o arquivo do banco de dados na raiz do projeto
DB_FILE_PATH = os.path.join(BASE_DIR, "banco.db")

# Cria a URL de conexão para o banco de dados SQLite na raiz do projeto
SQLALCHEMY_DATABASE_URL = f'sqlite:///{DB_FILE_PATH}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        

