from fastapi import APIRouter

router = APIRouter()

@router.post("/", summary='Cadastrar um novo centro de treinamentos')
def post():
  pass


@router.get("/", summary='Consultar todos os centros de treinamento')
def get():
  pass


@router.get("/{id}", summary='Consultar um centro de treinamento pelo id')
def getID(id: int):
  pass