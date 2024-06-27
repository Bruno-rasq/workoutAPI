from fastapi import APIRouter, status, HTTPException, Depends
from workoutAPI.categorias.schemas import CategoriaIn, CategoriaOut, CategoriasDB
from sqlalchemy.orm import Session
from workoutAPI.config.database import get_session
from workoutAPI.categorias.models import Categorias


router = APIRouter()


@router.post(
  "/", 
  summary='Criar uma nova Categoria', 
  status_code=status.HTTP_201_CREATED, 
  response_model=CategoriaOut
)
def post(categoria: CategoriaIn, db: Session = Depends(get_session)):
  '''Criar uma nova Categoria'''
  nova_categoria = Categorias(nome=categoria.nome)
  db.add(nova_categoria)
  db.commit()
  db.refresh(nova_categoria)
  return nova_categoria



@router.get(
  "/", 
  summary='Consultar todas as categorias', 
  response_model=CategoriasDB
)
def get(db: Session = Depends(get_session)):
  '''Consultar todos as categorias'''
  categorias = db.query(Categorias).all()
  return { "categorias": categorias }



@router.get(
  "/{id}", 
  summary='Consultar categoria pelo id', 
  response_model=CategoriaOut
)
def getID(id: int, db: Session = Depends(get_session)):
  '''Consultar categoria pelo id'''
  categoria = db.query(Categorias).filter(Categorias.id == id).first()

  if categoria is None:
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail=f'Categoria não encontrada no id: {id}'
    )

  return categoria