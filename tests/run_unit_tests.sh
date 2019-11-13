#!/usr/bin/env bash

echo "RUNNING NANOWIRE_FLASK UNIT TESTS"

cd ..

docker build -t nanowire_flask_unit_tests --file ./tests.Dockerfile .

#python3 text_server.py &

#docker run -e "PYTHON_DEBUG"="True" \
#-p 5003:5003 \
#nanowire_flask_unit_tests

docker run -e "PYTHON_DEBUG"="True" \
nanowire_flask_unit_tests
