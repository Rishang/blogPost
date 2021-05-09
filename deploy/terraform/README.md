
# terraform variables

| variable | type | description |
|----------|-----|---------------------|
| rds_db_name   | string | rds database name
| rds_db_username   | string | username for rds db
| rds_db_password   | string | password for rds db
| log_group_prefix   | string | log group prefix for webapp
| app_cluster  | string | ecs cluster name
| ecs_iam_role_name   | string | IAM execution role for ecs
| task_defiantion_family  | string | task defination family for ecs tasks
| REPO_NAME   | string | ECR repo name
| GIT_COMMIT   | string | Git commit version
| app_state  | string | stage of app, dev/prod
| DATABASE  | string | database type (postgres)
| DATABASE_PORT  | string | port for the database
| DATABASE_ENGINE  | string | Configs for django app settings
| DJANGO_SECRET_KEY   | string | Configs for django app settings
| DJANGO_ADMIN_USERNAME   | string | Configs for django app settings
| DJNGO_ADMIN_EMAIL   | string | Configs for django app settings
| DJNGO_ADMIN_PASSWORD   | string | Configs for django app settings
| DJANGO_ALLOWED_HOST   | string | Configs for django app settings
| DJANGO_DEBUG_MODE   | string | Configs for django app settings, 0 | False, 1 | True
| webapp_bucket   | string | S3 bucket for  webapp, ECS taks roles
