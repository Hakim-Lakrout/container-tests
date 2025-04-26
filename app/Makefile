IMAGE_NAME = tremplin-image
BATS_LIB_PATH = ~/tests/test/test_helper

.PHONY: all build test cst-test bats-test

all: build test

build:
	docker build -t $(IMAGE_NAME) .

cst-test:
	container-structure-test test --image $(IMAGE_NAME):latest --config tests/cst-tests.yaml

bats-test:
	BATS_LIB_PATH=$(BATS_LIB_PATH) bats tests/test.bats.sh

test: cst-test bats-test
