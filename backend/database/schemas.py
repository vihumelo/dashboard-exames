from pydantic import BaseModel
from datetime import datetime
from typing import List


class DashboardUpdate(BaseModel):
    
    exame: str
    registro: str
    resultado: str

class DashboardBase(BaseModel):

    comunicacao: int
    registro: str
    hora_execucao: datetime
    hora_coleta: datetime
    exame: str
    resultado: str
    setor: str
    
class Dashboard(DashboardBase):
    
    id: int
    
class DashboardID(BaseModel):
    
    id: int

class DashboardList(BaseModel):
    dashboards: List[DashboardBase]


