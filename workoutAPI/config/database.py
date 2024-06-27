from sqlalchemy import create_engine
from sqlalchemy.orm import Session, registry

from workoutAPI.config.settings import settings

engine = create_engine(settings.DB_URL)
table_registry = registry()

def get_session():
  with Session(engine) as session:
    yield session