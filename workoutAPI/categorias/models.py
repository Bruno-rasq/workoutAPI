from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from workoutAPI.config.database import table_registry


@table_registry.mapped_as_dataclass
class Categorias:
  __tablename__ = 'categorias'

  id    : Mapped[int] = mapped_column(Integer, primary_key=True, index=True, init=False)
  nome  : Mapped[str] = mapped_column(String(50), unique=True, nullable=False)

  # atleta: Mapped['AtletaModel'] = relationship(back_populates="categoria")