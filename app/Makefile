IMAGE_NAME = tremplin-image


.PHONY: all build test cst-test 

all: build test

build:
	docker build -t $(IMAGE_NAME) .

cst-test: build
	container-structure-test test --image $(IMAGE_NAME):latest --config tests/cst-tests.yaml

test: cst-test 

run: build
	docker run --name python_app -ti -p  5001:5000  --rm tremplin-image:latest