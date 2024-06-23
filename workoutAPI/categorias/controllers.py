from fastapi import APIRouter

router = APIRouter()

@router.post("/", summary='Criar uma nova Categoria')
def post():
  pass


@router.get("/", summary='Consultar todas as categorias')
def get():
  pass


@router.get("/{id}", summary='Consultar categoria pelo id')
def getID(id: int):
  pass