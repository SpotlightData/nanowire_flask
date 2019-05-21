#!/usr/bin/env bash

echo "RUNNING NANOWIRE_FLASK UNIT TESTS"

docker build -t nanowire_flask_unit_tests .

#python3 text_server.py &

docker run -e "PYTHON_DEBUG"="True" \
-p 5000:5000 \
-p 8001:8001 \
nanowire_flask_unit_tests
