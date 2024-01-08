DOCKER_IMAGE := python-project-example
VERSION := $(shell git describe --always --dirty --long)

setup:
	pyenv local 3.11.7
	pip install -U pip
	python -m venv venv
	./venv/bin/pip install -r requirements.txt

test:
	pytest

lint:
	pylint src/python_project_example

build-image:
	    docker build . -t $(DOCKER_IMAGE):$(VERSION)