from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import Annotated

from workoutAPI.atletas.schemas import AtletaIN, AtletaOUT, AtletasDB, AtletaUpdate
from workoutAPI.atletas.models import Atleta
from workoutAPI.config.database import get_session


router = APIRouter()

BDSESSION = Annotated[Session, Depends(get_session)]


@router.post(
  "/", 
  summary='Criar um novo atleta', 
  status_code=status.HTTP_201_CREATED, 
  response_model=AtletaOUT
)
def post(atleta: AtletaIN, db: BDSESSION):
  '''Cadastrar um novo atleta'''
  
  atleta_db = db.scalar(select(Atleta).where(Atleta.cpf == atleta.cpf))

  if atleta_db:
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST,
      detail="atleta com este cpf já cadastrado."
    )
    
  novo_atleta = Atleta(**atleta.model_dump())
  db.add(novo_atleta)
  db.commit()
  db.refresh(novo_atleta)
  
  return novo_atleta



@router.get(
  "/", 
  summary='Consultar todos os atletas', 
  response_model=AtletasDB
)
def get(db: BDSESSION, skip: int = 0, limit: int = 3):
  '''Consultar lista de atletas'''
  
  atletas = db.scalars(select(Atleta).offset(skip).limit(limit)).all()
  return { "atletas": atletas }



@router.get(
  "/{id}", 
  summary='Consultar atleta pelo id', 
  response_model=AtletaOUT
)
def getID(id: int, db: BDSESSION):
  '''Consultar um atleta pelo id'''
  
  atleta = db.scalar(select(Atleta).where(Atleta.id == id))

  if atleta is None:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND, 
      detail="atleta não encontrado."
    )
  return atleta



@router.patch(
  "/{id}", 
  summary='Atualizar dados do atleta'
)
def patch(id: int, update: AtletaUpdate, db: BDSESSION):
  '''Atualizar campos de nome e idade'''
  
  atleta_db = db.scalar(select(Atleta).where(Atleta.id == id))

  if atleta_db is None:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND, 
      detail="atleta não encontrado."
    )

  atleta_db.nome = update.nome
  atleta_db.idade = update.idade
  db.commit()
  db.refresh(atleta_db)
  
  return atleta_db



@router.delete(
  "/{id}", 
  summary='Deleter um atleta', 
  status_code=status.HTTP_204_NO_CONTENT
)
def delete(id: int, db: BDSESSION):
  '''Deletar um Atleta pelo seu identificador'''
  
  atleta = db.scalar(select(Atleta).where(Atleta.id == id))

  if atleta is None:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND, 
      detail="atleta não encontrado."
    )

  db.delete(atleta)
  db.commit()
  return None



@router.get(
  "/{nome}", 
  summary="Consultar atleta pelo nome",
  response_model=AtletaOUT
)
def getByNome(nome: str, db: BDSESSION):
  atleta = db.scalar(select(Atleta).where(Atleta.nome == nome))

  if atleta:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail="Nenhum atleta com este nome cadastrado"
    )

  return atleta
  
  

@router.get(
  "/{cpf}", 
  summary="Consultar atleta pelo cpf", 
  response_model=AtletaOUT
)
def getByCPF(cpf: str, db: BDSESSION):
  ...