FROM python:alpine
ENV APP_HOME=/testscripts
ENV PYTHONUNBUFFERED 1
WORKDIR ${APP_HOME}
COPY ui_test/requirements.txt .
RUN pip install -r requirements.txt
COPY ui_test .