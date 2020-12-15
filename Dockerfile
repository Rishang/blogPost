FROM ubuntu:latest
ENV APP_HOME=/blogproject
ENV PYTHONUNBUFFERED 1
WORKDIR ${APP_HOME}
RUN apt update \
    && apt install -y python3-minimal \
                python3-distutils \
                curl netcat \
    && curl -fsS https://bootstrap.pypa.io/get-pip.py -o get-pip.py \
    && python3 get-pip.py \
    && pip install -U pip
# COPY code .
COPY . .
# install requirements
RUN pip install -r requirements.txt
EXPOSE 8000/tcp
ENTRYPOINT [ "/blogproject/entrypoint.dev.sh" ]