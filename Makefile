install:
	@pip install -r requiriments.txt

run:
	@uvicorn workoutAPI.main:app --host 0.0.0.0 --port 8080 --reload 