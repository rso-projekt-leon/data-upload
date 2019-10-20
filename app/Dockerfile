FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

ADD ./main /flask-app
ADD ./main/api /flask-app/api
ADD ./requirements.txt /flask-app/requirements.txt
WORKDIR /flask-app
RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["manage.py"]