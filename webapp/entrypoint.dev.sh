#!/bin/bash

function _django_config {
  
 # migrate db and django
  echo "migrate django , postgres"
  python3 manage.py makemigrations
  python3 manage.py migrate

  # create superuser
  echo "creating superuser"
  python3 manage.py shell -c "exec(open('./django_blog/create_admin.py','r').read())"

}

if [ "$DATABASE" = "postgres" ]
then

  echo "Waiting for postgres..."

  while ! nc -z $POSTGRES_HOSTNAME $DATABASE_PORT; do
    sleep 0.1
  done

  echo "PostgreSQL started"
  # migrate db and django
  echo "migrate django , postgres"
  python3 manage.py makemigrations --noinput
  python3 manage.py migrate --noinput

  _django_config
   
fi

exec "$@"