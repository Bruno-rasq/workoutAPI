from workoutAPI.contrib.schema import BaseSchema
from typing import Annotated
from pydantic import Field

class Categoria(BaseSchema):
  nome:   Annotated[str, Field(description='Nome da categoria', examples='scale', max_length=10)]