FROM python:3.6

ADD requirements.txt /

RUN pip install -r requirements.txt

ADD ./manual_testing.py /

CMD ['python', manual_testing.py]