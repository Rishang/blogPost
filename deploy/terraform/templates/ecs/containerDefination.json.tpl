[
    {
        "name": "${container_name}",
        "logConfiguration": {
            "logDriver": "awslogs",
            "options": {
                "awslogs-group": "${logs}",
                "awslogs-region": "us-east-1",
                "awslogs-stream-prefix": "ecs"
            }
        },

        "portMappings": [
            {
                "hostPort": ${RUN_PORT},
                "protocol": "tcp",
                "containerPort": ${RUN_PORT}
            }
        ],
        "memoryReservation": 200,
        "image": "${image}",
        "essential": true,
        "environment": [
            {
                "name": "STAGE",
                "value": "${STATE}"
            },
            {
                "name": "AWS_STORAGE_BUCKET_NAME",
                "value": "${AWS_STORAGE_BUCKET_NAME}"
            },
            {
                "name": "DATABASE",
                "value": "${DATABASE}"
            },
            {
                "name": "DATABASE_PORT",
                "value": "${DATABASE_PORT}"
            },
            {
                "name": "POSTGRES_USER",
                "value": "${DATABASE_USER}"
            },
            {
                "name": "POSTGRES_PASSWORD",
                "value": "${DATABASE_PASSWORD}"
            },
            {
                "name": "POSTGRES_DB",
                "value": "${DATABASE_NAME}"
            },
            {
                "name": "DATABASE_ENGINE",
                "value": "${DATABASE_ENGINE}"
            },
            {
                "name": "DJANGO_ALLOWED_HOST",
                "value": "${DJANGO_ALLOWED_HOST}"
            },
            {
                "name": "DJNGO_ADMIN_PASSWORD",
                "value": "${DJNGO_ADMIN_PASSWORD}"
            },
            {
                "name": "DJNGO_ADMIN_EMAIL",
                "value": "${DJNGO_ADMIN_EMAIL}"
            },
            {
                "name": "DJANGO_ADMIN_USERNAME",
                "value": "${DJANGO_ADMIN_USERNAME}"
            },
            {
                "name": "DJANGO_SECRET_KEY",
                "value": "${DJANGO_SECRET_KEY}"
            },
            {
                "name": "POSTGRES_HOSTNAME",
                "value": "${POSTGRES_HOSTNAME}"
            },
            {
                "name": "DJANGO_DEBUG_MODE",
                "value": "${DJANGO_DEBUG_MODE}"
            }
        ],
        "command": [
            "gunicorn", "django_blog.wsgi:application", "--bind", "0.0.0.0:${RUN_PORT}"
        ]
    }
]
