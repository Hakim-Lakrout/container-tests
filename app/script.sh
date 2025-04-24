#!/bin/bash
docker build -t tremplin-image .
container-structure-test test --image tremplin-image:latest --config tests/cst-tests.yaml