init:
	pip install -r requirements.txt

start:
	python ghlint/main.py

test:
	pytest

site:
	cd docs; \
	python -m http.server 8000 # use SimpleHTTPServer for Python 2.x
