install:
	@pip install -r requiriments.txt

revision:
	alembic revision --autogenerate -m "$(message)"

upgrade:
	alembic upgrade head

run:
	@uvicorn workoutAPI.main:app --host 0.0.0.0 --port 8080 --reload 