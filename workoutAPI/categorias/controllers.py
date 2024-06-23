from fastapi import APIRouter, status, HTTPException
from workoutAPI.categorias.schemas import CategoriaIn, CategoriaOut, CategoriasDB


CATEGORIAS = [] #fake database 

router = APIRouter()


@router.post(
  "/", 
  summary='Criar uma nova Categoria', 
  status_code=status.HTTP_201_CREATED, 
  response_model=CategoriaOut
)
def post(categoria: CategoriaIn):
  '''Criar uma nova Categoria'''
  nova_categoria = CategoriaOut(id=len(CATEGORIAS) + 1, **categoria.model_dump())
  CATEGORIAS.append(nova_categoria)
  return nova_categoria



@router.get(
  "/", 
  summary='Consultar todas as categorias', 
  response_model=CategoriasDB
)
def get():
  '''Consultar todos as categorias'''
  return { "categorias": CATEGORIAS }



@router.get(
  "/{id}", 
  summary='Consultar categoria pelo id', 
  response_model=CategoriaOut
)
def getID(id: int):
  '''Consultar categoria pelo id'''
  for categoria in CATEGORIAS:
    if categoria.id == id:
      return categoria

  raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND, 
      detail=f'Categoria não encontrada no id: {id}'
  )
      