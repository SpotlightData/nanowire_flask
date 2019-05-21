FROM python:3.6

RUN apt-get update

RUN apt-get install libzbar-dev -y

ADD requirements.txt /

RUN pip install -r requirements.txt

ADD ./manual_testing.py /
ADD ./text_server.py /
ADD ./image_server.py /
ADD ./json_server.py /
ADD ./csv_server.py /
ADD ./test_text1.txt /

CMD ["python", "manual_testing.py"]
