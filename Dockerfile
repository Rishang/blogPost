FROM ubuntu:latest
ENV APP_HOME=/blogproject
ENV PYTHONUNBUFFERED 1
WORKDIR ${APP_HOME}
RUN apt update \
    && apt install -y python3 python3-pip netcat \
    && apt clean \
    && pip3 install -U pip
ADD requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 8000/tcp
ENTRYPOINT [ "/blogproject/entrypoint.dev.sh" ]