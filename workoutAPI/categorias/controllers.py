from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import Annotated

from workoutAPI.categorias.schemas import CategoriaIn, CategoriaOut, CategoriasDB
from workoutAPI.config.database import get_session
from workoutAPI.categorias.models import Categorias


router = APIRouter()

BDSESSION = Annotated[Session, Depends(get_session)]


@router.post(
  "/", 
  summary='Criar uma nova Categoria', 
  status_code=status.HTTP_201_CREATED, 
  response_model=CategoriaOut
)
def post(categoria: CategoriaIn, db: BDSESSION):
  '''Criar uma nova Categoria'''

  categoria_db = db.scalar(select(Categorias).where(Categorias.nome == categoria.nome))

  if categoria_db:
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST,
      detail="categoria já cadastrada."
    )
  
  nova_categoria = Categorias(**categoria.model_dump())
  db.add(nova_categoria)
  db.commit()
  db.refresh(nova_categoria)
  
  return nova_categoria



@router.get(
  "/", 
  summary='Consultar todas as categorias', 
  response_model=CategoriasDB
)
def get(db: BDSESSION):
  '''Consultar todos as categorias'''
  
  categorias = db.scalars(select(Categorias)).all()
  return { "categorias": categorias }



@router.get(
  "/{id}", 
  summary='Consultar categoria pelo id', 
  response_model=CategoriaOut
)
def getID(id: int, db: BDSESSION):
  '''Consultar categoria pelo id'''
 
  categoria = db.scalar(select(Categorias).where(Categorias.id == id))

  if categoria is None:
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail=f'Categoria não encontrada no id: {id}'
    )

  return categoria