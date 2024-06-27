from typing import Annotated, Optional, List
from pydantic import Field, PositiveFloat, BaseModel
from workoutAPI.contrib.schema import BaseSchema
from datetime import datetime


class AtletaIN(BaseSchema):
  nome   : Annotated[str,           Field(description='Nome do atleta',   example='Joao',        max_length=50)]
  cpf    : Annotated[str,           Field(description='CPF do atleta',    example='12345678900', max_length=11)]
  sexo   : Annotated[str,           Field(description='Sexo do atleta',   example='M',           max_length=1)]
  idade  : Annotated[int,           Field(description='Idade do atleta',  example='25')]
  peso   : Annotated[PositiveFloat, Field(description='Peso do atleta',   example='75.5')]
  altura : Annotated[PositiveFloat, Field(description='Altura do atleta', example='1.80')]


class AtletaOUT(AtletaIN, BaseModel):
  id         : Annotated[int, Field(description='Identificador do Atleta')]
  created_at : Annotated[datetime, Field(description="data de criacao do atleta")]


class AtletaUpdate(BaseSchema):
  nome  : Annotated[Optional[str], Field(None, description='Nome do atleta',  example='Joao', max_length=50)]
  idade : Annotated[Optional[int], Field(None, description='Idade do atleta', example=25)]


class AtletasDB(BaseModel):
  atletas: List[AtletaOUT]