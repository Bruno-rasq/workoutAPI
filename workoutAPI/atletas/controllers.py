from fastapi import APIRouter

router = APIRouter()

@router.post("/", summary='Criar um novo atleta')
def post():
  pass


@router.get("/", summary='Consultar todos os atletas')
def get():
  pass


@router.get("/{id}", summary='Consultar atleta pelo id')
def getID(id: int):
  pass


@router.patch("/{id}", summary='Atualizar dados do atleta')
def patch(id: int):
  pass


@router.delete("/{id}", summary='Deleter um atleta')
def delete(id: int):
  pass