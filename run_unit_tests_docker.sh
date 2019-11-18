#!/usr/bin/env bash

docker build -t test_nanowire_flask:0.0.0 .

docker run -it test_nanowire_flask:0.0.0