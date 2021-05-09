
# django app deployment to aws by terraform

## Required aws resource

1. aws vpc (default vpc)
2. ecsTaskExecution iam role

## Recources created on aws by `terraform apply`

1. RDS Database (postgres)
2. S3 Bucket
3. ECS cluster / service
4. CloudWatch log group for ECS logs
5. Application Load Balencer for ECS

## Variables for configuring terrafrom deployment

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
| GIT_COMMIT   | string | Git commit id
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
