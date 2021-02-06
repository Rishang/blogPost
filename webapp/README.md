# blogPost
django app for blog

## Starting app using docker

Create a `blogPost/.env.dev` file where we will keep all the config details for hosting the webapp.

### Inside `env.dev` file

    DJANGO_ALLOWED_HOST=        // (ALLOWED HOST IP)
    DJANGO_SECRET_KEY=          // (DJANGO SETTINGS SECRET KEY)
    DJANGO_DEBUG_MODE=          // (True || False)

    DJANGO_ADMIN_USERNAME=      // (ADMIN USERNAME)
    DJNGO_ADMIN_EMAIL=          // (ADMIN EMAIL)
    DJNGO_ADMIN_PASSWORD=       // (ADMIN PASSWORD)

    DATABASE=                   // (DATABASE TYPE)
    DATABASE_ENGINE=            // (DJANGO DB BACKENDS DATABASE TYPE)
    DATABASE_PORT=              // (DATABASE PORT)

    POSTGRES_HOSTNAME=          // (POSTGRES HOST NAME)
    POSTGRES_USER=              // (POSTGRES USER)
    POSTGRES_PASSWORD=          // (POSTGRES PASSWORD)
    POSTGRES_DB=                // (POSTGRES DB-NAME)

After the `env.dev` has been created as the above needed requirements, perform following command.

    docker-compose build && docker-compose up

## For running app locally,

For running application locally following are the things you need to have

- postgres sql installed

- postgres user and database for the app should be already present

- Optional to have pg-admin for monitering postgres databse

After having above needs fulfilled create `.env.local`  file at `blogPost/.env.local`

### Inside `.env.local`

    DJANGO_ALLOWED_HOST=        // (ALLOWED HOST IP)
    DJANGO_SECRET_KEY=          // (DJANGO SETTINGS SECRET KEY)
    DJANGO_DEBUG_MODE=          // (True || False)

    DATABASE=                   // (DATABASE TYPE)
    DATABASE_ENGINE=            // (DJANGO DB BACKENDS DATABASE TYPE)
    DATABASE_PORT=              // (DATABASE PORT)

    POSTGRES_HOSTNAME=          // (POSTGRES HOST NAME)
    POSTGRES_USER=              // (POSTGRES USER)
    POSTGRES_PASSWORD=          // (POSTGRES PASSWORD)
    POSTGRES_DB=                // (POSTGRES DB-NAME)

After the `env.dev` has been created as the above needed requirements, perform following command.

    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
