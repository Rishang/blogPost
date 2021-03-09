FROM ubuntu:latest
ENV APP_HOME=/blogproject
ENV PYTHONUNBUFFERED 1
RUN apt update \
    && apt install -y python3-minimal \
                python3-distutils \
                curl netcat \
    && curl -fsS https://bootstrap.pypa.io/get-pip.py -o get-pip.py \
    && python3 get-pip.py \
    && pip install -U pip
WORKDIR ${APP_HOME}
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000/tcp
ENTRYPOINT [ "/blogproject/entrypoint.dev.sh" ]
