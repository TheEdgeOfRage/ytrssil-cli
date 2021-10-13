NAME = ytrssil
TESTS = tests

FILES_PY = $(shell find $(CURDIR)/$(NAME) $(CURDIR)/$(TESTS) -type f -name "*.py")
TEST_PY = $(shell find $(CURDIR)/$(TESTS) -type f -name "*.py")

setup-dev:
	pip install -r requirements-dev.txt
	pip install -e .

test:
	python -m pytest --cov $(CURDIR)/$(NAME)

flake8:
	@flake8 $(FILES_PY)

mypy:
	@mypy --strict $(FILES_PY)

isort:
	@isort -c $(FILES_PY)

validate: flake8 mypy isort

coverage:
	python -m pytest --cov $(CURDIR)/$(NAME) --cov-report html

build:
	python setup.py sdist bdist_wheel

clean:
	rm -rf $(CURDIR)/build
	rm -rf $(CURDIR)/dist
	rm -rf $(CURDIR)/htmlcov
	rm -rf $(CURDIR)/.coverage
	rm -rf $(CURDIR)/$(NAME).egg-info
