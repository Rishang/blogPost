# blogPost

django blog app

## For running app locally

### Step 1

Install requirements

`pip install -r blogPost/webapp/requirements.txt`

### Step 2

Create file `.env.local` at directory path `blogPost/webapp/`

### Inside `.env.local`

    DJANGO_ALLOWED_HOST=*
    DJANGO_SECRET_KEY=        // random_secret_key
    DJANGO_DEBUG_MODE=        // (True || False)

### Step 3

The `manage.py` file is stored at `blogPost/webapp` follow the below steps

- Make migrations

        python manage.py makemigrations
        python manage.py migrate

- Create admin user

        python manage.py createsuperuser

- Run server

        python manage.py runserver

## Starting app using docker

Create a `blogPost/webapp/.env.dev` file where we will keep all the config details for hosting the webapp.

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

After the `env.dev` has been created as the above needed requirements, perform following command.

    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
