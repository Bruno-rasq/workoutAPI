import os
from fastapi import FastAPI
from workoutAPI.routers import api_router
from workoutAPI.config.database import engine, table_registry
from workoutAPI.config.settings import settings


if not os.path.exists(settings.DB_URL):
  table_registry.metadata.create_all(bind=engine)


app = FastAPI(title='WorkoutApi')
app.include_router(api_router)

@app.get("/")
def root():
  return {"messagem": "ok"}