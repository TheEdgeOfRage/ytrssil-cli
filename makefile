.PHONY: setup-dev flake8 isort isort-fix mypy lint build clean

NAME = ytrssil

FILES_PY = $(shell find $(CURDIR)/$(NAME) -type f -name "*.py")

setup-dev:
	pip install -r requirements-dev.txt
	pip install -e .

flake8:
	@flake8 $(FILES_PY)

isort:
	@isort -c $(FILES_PY)

isort-fix:
	@isort $(FILES_PY)

mypy:
	@mypy --strict $(FILES_PY)

lint: flake8 isort mypy

build:
	python setup.py sdist bdist_wheel

clean:
	rm -rf $(CURDIR)/build
	rm -rf $(CURDIR)/dist
	rm -rf $(CURDIR)/$(NAME).egg-info

publish:
	@git checkout $(shell git tag | sort -V | tail -n1) >/dev/null 2>&1
	@$(MAKE) clean > /dev/null
	@$(MAKE) build > /dev/null
	@twine upload dist/*
	@$(MAKE) clean > /dev/null
	@git switch main >/dev/null 2>&1
