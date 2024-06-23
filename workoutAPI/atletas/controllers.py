from fastapi import APIRouter, status, HTTPException
from workoutAPI.atletas.schemas import AtletaIN, AtletaOUT, AtletasDB


router = APIRouter()

ATLETAS = [] #fake database



@router.post(
  "/", 
  summary='Criar um novo atleta',
  status_code=status.HTTP_201_CREATED,
  response_model=AtletaOUT
)
def post(atleta: AtletaIN):
  '''Cadastrar um novo atleta'''
  novo_atleta = AtletaOUT(id=len(ATLETAS) + 1, **atleta.model_dump())
  ATLETAS.append(novo_atleta)
  return novo_atleta


@router.get("/", summary='Consultar todos os atletas', response_model=AtletasDB)
def get():
  '''Consultar lista de atletas'''
  return { "atletas": ATLETAS }


@router.get("/{id}", summary='Consultar atleta pelo id', response_model=AtletaOUT)
def getID(id: int):
  '''Consultar um atleta pelo id'''
  for atleta in ATLETAS:
    if atleta.id == id:
      return atleta

  raise HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, 
    detail="atleta não encontrado."
  )


@router.patch("/{id}", summary='Atualizar dados do atleta')
def patch(id: int):
  pass


@router.delete("/{id}", summary='Deleter um atleta', status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int):
  for atleta in ATLETAS:
    if atleta.id == id:
      del ATLETAS[id - 1]
      return

  raise HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, 
    detail="atleta não encontrado."
  )