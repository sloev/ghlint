init:
	pip install -r requirements.txt

start:
	python ghlint/main.py

test:
	pytest
