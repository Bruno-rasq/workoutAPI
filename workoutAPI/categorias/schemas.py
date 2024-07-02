from pydantic import Field, BaseModel
from typing import Annotated, List
from workoutAPI.contrib.schema import BaseSchema


class CategoriaIn(BaseSchema):
  nome: Annotated[str, Field(description='Nome da categoria', example='scale', max_length=20)]

class CategoriaOut(CategoriaIn):
  id: Annotated[int, Field(description='Identificador da categoria')]

class CategoriasDB(BaseModel):
  categorias: List[CategoriaOut]