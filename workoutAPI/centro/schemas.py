from workoutAPI.contrib.schema import BaseSchema
from typing import Annotated
from pydantic import Field

class CentroTreinamento(BaseSchema):
  nome         : Annotated[str, Field(description='Nome do centro',       examples='CT_KIng',        max_length=20)]
  endereco     : Annotated[str, Field(description='Enderenco do CT',      examples='Rua X quadra 2', max_length=60)]
  proprietario : Annotated[str, Field(description='Nome do proprietario', examples='Marcos',         max_length=30)]