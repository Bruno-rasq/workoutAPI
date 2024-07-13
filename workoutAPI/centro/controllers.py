from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import Annotated

from workoutAPI.centro.schemas import CentroTreinamento, CTDB, CTOUT
from workoutAPI.centro.models import Centro
from workoutAPI.config.database import get_session


router = APIRouter()

BDSESSION = Annotated[Session, Depends(get_session)]


@router.post(
  "/", 
  summary='Cadastrar um novo centro de treinamentos',
  status_code=status.HTTP_201_CREATED,
  response_model=CTOUT
)
def post(CT: CentroTreinamento, db: BDSESSION):
  '''Gravar um novo Centro de Treinamento'''

  ct_db = db.scalar(
    select(Centro).where(Centro.nome == CT.nome)
  )

  if ct_db:
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST,
      detail="Centro já cadastrado."
    )
    
  novo_ct = Centro(**CT.model_dump())
  db.add(novo_ct)
  db.commit()
  db.refresh(novo_ct)
  
  return novo_ct



@router.get(
  "/", 
  summary='Consultar todos os centros de treinamento',
  response_model=CTDB
)
def get(db: BDSESSION):
  '''Consultar todos os Centros de Treinamentos'''
  
  centros = db.scalars(select(Centro)).all()
  return { "centros": centros }



@router.get(
  "/{id}", 
  summary='Consultar um centro de treinamento pelo id',
  response_model=CTOUT
)
def getID(id: int, db: BDSESSION):
  '''Consultar um Centro de Treinamento pelo identificador'''
  
  centro = db.scalar(select(Centro).where(Centro.id == id))

  if centro is None:
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail=f'Centro não encontrada no id: {id}'
    )

  return centro