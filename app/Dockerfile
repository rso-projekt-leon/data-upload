FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

COPY ./main/. /flask-app/
COPY ./requirements.txt /flask-app/requirements.txt
WORKDIR /flask-app
RUN pip install -r requirements.txt
RUN ls -la /flask-app*

EXPOSE 5000

ENTRYPOINT ["python"]
CMD ["manage.py"]