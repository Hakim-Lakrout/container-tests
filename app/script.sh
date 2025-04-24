#!/bin/bash
docker build -t tremplin-image .
container-structure-test test --image tremplin-image:latest --config tests/cst-tests.yaml

# bats tests
export BATS_LIB_PATH=~/tests/test/test_helper
bats tests/test.bats.sh