#!/usr/bin/env bash

docker build -t test_nanowire_flask:0.0.0 .

docker run --rm -it test_nanowire_flask:0.0.0
