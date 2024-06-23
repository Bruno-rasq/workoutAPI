from fastapi import APIRouter

from workoutAPI.atletas.controllers import router as atletas
from workoutAPI.categorias.controllers import router as categorias
from workoutAPI.centro.controllers import router as centro

api_router = APIRouter()

api_router.include_router(atletas,    prefix='/atletas',             tags=['atletas'])
api_router.include_router(categorias, prefix='/categorias',          tags=['categorias'])
api_router.include_router(centro,     prefix='/centros_treinamento', tags=['centros_treinamento'])