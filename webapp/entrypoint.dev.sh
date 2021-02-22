#!/bin/sh

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

    # create superuser
    echo "creating superuser"
    python3 manage.py shell -c "exec(open('./django_blog/create_admin.py','r').read())"
fi

exec "$@"