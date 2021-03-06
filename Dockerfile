FROM python:3.7

RUN apt-get update

RUN apt-get install libzbar-dev -y

RUN mkdir /tests

ADD ./tests/requirements.txt /tests

RUN pip install -r /tests/requirements.txt

#ADD ./nanowire_flask /nanowire_flask

ADD ./ .

#ADD setup.py /

RUN python setup.py install

CMD ["python", "/tests/unit_tests.py"]
#CMD ["python", "json_server.py"]
