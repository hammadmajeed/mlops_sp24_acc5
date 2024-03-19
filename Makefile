install:
	pip install --upgrade pip&\
	pip install -r requirements.txt
lint:
	pylint --disable=C,R hello.py
test:
	python -m pytest -vv --cov=hello test_hello.py