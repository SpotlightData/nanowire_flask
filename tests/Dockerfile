FROM python:3.6

RUN apt-get update

RUN apt-get install libzbar-dev -y

ADD requirements.txt /

RUN pip install -r requirements.txt

ADD ./unit_tests.py /
ADD ./text_server.py /
ADD ./image_server.py /
ADD ./json_server.py /
ADD ./csv_server.py /
ADD ./test_text1.txt /

CMD ["python", "unit_tests.py"]
#CMD ["python", "json_server.py"]
