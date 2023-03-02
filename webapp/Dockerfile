FROM python:3.10-slim
ENV APP_HOME=/blogproject
ENV PYTHONUNBUFFERED 1
RUN apt update && apt install -y netcat libmagic1 && pip install -U pip
WORKDIR ${APP_HOME}
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000/tcp
ENV RUN_PORT=8000
ENTRYPOINT [ "/blogproject/entrypoint.dev.sh" ]
