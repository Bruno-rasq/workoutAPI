from workoutAPI.contrib.schema import BaseSchema
from typing import Annotated, List
from pydantic import Field, BaseModel

class CentroTreinamento(BaseSchema):
  nome         : Annotated[str, Field(description='Nome do centro',       example='CT_KIng',        max_length=20)]
  endereco     : Annotated[str, Field(description='Enderenco do CT',      example='Rua X quadra 2', max_length=60)]
  proprietario : Annotated[str, Field(description='Nome do proprietario', example='Marcos',         max_length=30)]


class CTOUT(CentroTreinamento):
  id : Annotated[int, Field(description='Identificador do centro de treinamentos')]


class CTDB(BaseModel):
  centros : List[CentroTreinamento] 