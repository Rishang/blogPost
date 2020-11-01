FROM ubuntu:latest
RUN apt update && apt install -y python3 python3-pip && apt clean && pip3 install -U pip && mkdir /blogproject
ENV PYTHONUNBUFFERED 1
WORKDIR /blogproject
COPY requirements.txt /blogproject
RUN pip3 install -r requirements.txt
COPY . /blogproject/
EXPOSE 8000/tcp
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
