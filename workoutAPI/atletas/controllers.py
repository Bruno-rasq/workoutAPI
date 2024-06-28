from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select

from workoutAPI.atletas.schemas import AtletaIN, AtletaOUT, AtletasDB, AtletaUpdate
from workoutAPI.atletas.models import Atleta
from workoutAPI.config.database import get_session


router = APIRouter()


@router.post("/", summary='Criar um novo atleta', status_code=status.HTTP_201_CREATED, response_model=AtletaOUT)
def post(atleta: AtletaIN, db: Session = Depends(get_session)):
  '''Cadastrar um novo atleta'''
  novo_atleta = Atleta(**atleta.model_dump())
  db.add(novo_atleta)
  db.commit()
  db.refresh(novo_atleta)
  return novo_atleta



@router.get("/", summary='Consultar todos os atletas', response_model=AtletasDB)
def get(skip: int = 0, limit: int = 3, db: Session = Depends(get_session)):
  '''Consultar lista de atletas'''
  
  atletas = db.scalars(select(Atleta).offset(skip).limit(limit)).all()
  return { "atletas": atletas }



@router.get("/{id}", summary='Consultar atleta pelo id', response_model=AtletaOUT)
def getID(id: int, db: Session = Depends(get_session)):
  '''Consultar um atleta pelo id'''
  
  atleta = db.scalar(select(Atleta).where(Atleta.id == id))

  if atleta is None:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND, 
      detail="atleta não encontrado."
    )
  return atleta



# @router.get("/{nome}", summary="Consultar atleta pelo nome", response_model=AtletaOUT)
# def getByNome(nome: str, db: Session = Depends(get_session)):
#   atleta = db.scalar(select(Atleta).where(Atleta.nome == nome))

#   if atleta is None:
#     raise HTTPException(
#       status_code=status.HTTP_404_NOT_FOUND, 
#       detail="atleta não encontrado."
#     )
#   return atleta
  


# @router.get("/{cpf}", summary="Consultar atleta pelo cpf", response_model=AtletaOUT)
# def getByCPF(cpf: str, db: Session = Depends(get_session)):
#   atleta = db.scalar(select(Atleta).where(Atleta.cpf == cpf))

#   if atleta is None:
#     raise HTTPException(
#       status_code=status.HTTP_404_NOT_FOUND, 
#       detail="atleta não encontrado."
#     )
#   return atleta



@router.patch("/{id}", summary='Atualizar dados do atleta')
def patch(id: int, update: AtletaUpdate, db: Session = Depends(get_session)):
  
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



@router.delete("/{id}", summary='Deleter um atleta', status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session = Depends(get_session)):
  
  atleta = db.scalar(select(Atleta).where(Atleta.id == id))

  if atleta is None:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND, 
      detail="atleta não encontrado."
    )

  db.delete(atleta)
  db.commit()
  return None