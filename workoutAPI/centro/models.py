from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from workoutAPI.config.database import table_registry



@table_registry.mapped_as_dataclass
class Centro:
  __tablename__ = 'centro_de_treinamentos'

  id           : Mapped[int] = mapped_column(Integer, primary_key=True, index=True, init=False)
  nome         : Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
  endereco     : Mapped[str] = mapped_column(String(60), nullable=False)
  proprietario : Mapped[str] = mapped_column(String(30), nullable=False)

  # atleta: Mapped['AtletaModel'] = relationship(back_populates='centro_treinamento')