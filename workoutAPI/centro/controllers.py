from fastapi import APIRouter, status, HTTPException
from workoutAPI.centro.schemas import CentroTreinamento, CTDB, CTOUT


router = APIRouter()

CENTROS = [] #fake database


@router.post(
  "/", 
  summary='Cadastrar um novo centro de treinamentos',
  status_code=status.HTTP_201_CREATED,
  response_model=CTOUT
)
def post(CT: CentroTreinamento):
  '''Gravar um novo Centro de Treinamento'''
  novo_ct = CTOUT(id=len(CENTROS) + 1, **CT.model_dump())
  CENTROS.append(novo_ct)
  return novo_ct



@router.get(
  "/", 
  summary='Consultar todos os centros de treinamento',
  response_model=CTDB
)
def get():
  '''Consultar todos os Centros de Treinamentos'''
  return { "centros": CENTROS }



@router.get(
  "/{id}", 
  summary='Consultar um centro de treinamento pelo id',
  response_model=CTOUT
)
def getID(id: int):
  '''Consultar um Centro de Treinamento pelo identificador'''
  for centro in CENTROS:
    if centro.id == id:
      return centro

  raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND, 
      detail=f'Centro não encontrada no id: {id}'
  )