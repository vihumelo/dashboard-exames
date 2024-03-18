from sqlalchemy import Column, Integer, String, TIMESTAMP
from database import Base


class Dashboard(Base):
    __tablename__ = 'panicos'
    id = Column(Integer, primary_key=True, index=True)
    registro = Column(String(100))
    hora_execucao = Column(TIMESTAMP)
    hora_coleta = Column(TIMESTAMP)
    exame = Column(String(100))
    resultado = Column(String(100))
    setor = Column(String(100))
    comunicacao = Column(Integer)

    
    
