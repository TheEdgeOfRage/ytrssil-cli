NAME = ytrssil
TESTS = tests

FILES_PY = $(shell find $(CURDIR)/$(NAME) $(CURDIR)/$(TESTS) -type f -name "*.py")
TEST_PY = $(shell find $(CURDIR)/$(TESTS) -type f -name "*.py")

setup-dev:
	pip install -r requirements-dev.txt
	pip install -e .

test:
	python -m unittest discover $(CURDIR)/$(TESTS)

flake8:
	@flake8 $(FILES_PY)

mypy:
	@mypy --strict $(FILES_PY)

isort:
	@isort -c $(FILES_PY)

validate: flake8 mypy isort

coverage:
	python -m coverage run -m unittest discover $(CURDIR)/$(TESTS)
	python -m coverage html
