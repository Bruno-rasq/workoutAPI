from fastapi import FastAPI
from workoutAPI.routers import api_router

app = FastAPI(title='WorkoutApi')
app.include_router(api_router)

@app.get("/")
def root():
  return {"messagem": "ok"}
