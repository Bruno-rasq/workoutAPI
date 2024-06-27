from fastapi import APIRouter, status, HTTPException, Depends
from workoutAPI.centro.schemas import CentroTreinamento, CTDB, CTOUT
from sqlalchemy.orm import Session
from workoutAPI.centro.models import Centro
from workoutAPI.config.database import get_session


router = APIRouter()


@router.post(
  "/", 
  summary='Cadastrar um novo centro de treinamentos',
  status_code=status.HTTP_201_CREATED,
  response_model=CTOUT
)
def post(CT: CentroTreinamento, db: Session = Depends(get_session)):
  '''Gravar um novo Centro de Treinamento'''
  novo_ct = Centro(**CT.model_dump())
  db.add(novo_ct)
  db.commit()
  db.refresh(novo_ct)
  return novo_ct



@router.get(
  "/", 
  summary='Consultar todos os centros de treinamento',
  response_model=CTDB
)
def get(db: Session = Depends(get_session)):
  '''Consultar todos os Centros de Treinamentos'''
  centros = db.query(Centro).all()
  return { "centros": centros }



@router.get(
  "/{id}", 
  summary='Consultar um centro de treinamento pelo id',
  response_model=CTOUT
)
def getID(id: int, db: Session = Depends(get_session)):
  '''Consultar um Centro de Treinamento pelo identificador'''
  centro = db.query(Centro).filter(Centro.id == id).first()

  if centro is None:
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail=f'Centro não encontrada no id: {id}'
    )

  return centro