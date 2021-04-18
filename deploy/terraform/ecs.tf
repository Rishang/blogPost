# ------------- TASK DEFINATION ----------------------

data "template_file" "cd_ecs_app" {
  
  template = file("./templates/ecs/containerDefination.json.tpl")

  vars = {
    # django container vars
    app_port       = 80
    logs           = aws_cloudwatch_log_group.ECS_APP.name
    image          = "${data.aws_ecr_repository.ECS_APP.repository_url}:${var.GIT_COMMIT}"
    container_name = "backend"
    
    # state
    STATE = var.app_state

    # db

    DATABASE        = var.DATABASE  
    DATABASE_PORT   = var.DATABASE_PORT
    DATABASE_ENGINE = var.DATABASE_ENGINE
    DATABASE_NAME   = var.rds_db_name
    DATABASE_USER   = var.rds_db_username
    DATABASE_PASSWORD  = var.rds_db_password

    # django

    POSTGRES_HOSTNAME     = module.rds.rds_endpoint
    DJANGO_SECRET_KEY     = var.DJANGO_SECRET_KEY
    DJANGO_ADMIN_USERNAME = var.DJANGO_ADMIN_USERNAME
    DJNGO_ADMIN_EMAIL     = var.DJNGO_ADMIN_EMAIL
    DJNGO_ADMIN_PASSWORD  = var.DJNGO_ADMIN_PASSWORD
    DJANGO_ALLOWED_HOST   = var.DJANGO_ALLOWED_HOST
    DJANGO_DEBUG_MODE     = var.DJANGO_DEBUG_MODE
    
    # s3
    AWS_STORAGE_BUCKET_NAME = var.bucket_name
  }
}

resource "aws_ecs_task_definition" "ECS_APP" {
  
  family = var.task_defiantion_family

  container_definitions    = data.template_file.cd_ecs_app.rendered
  execution_role_arn       = data.aws_iam_role.ECS_EXECUTION_ROLE.arn
  task_role_arn            = aws_iam_role.ECS_TASK_ROLE.arn
  requires_compatibilities = [
        "FARGATE"
    ]
  network_mode = "awsvpc"
  
  memory = 2048
  cpu    = 1024

}


# ------------- ECS ----------------------

resource "aws_ecs_cluster" "ECS_APP_CLUSTER" {
  name = var.app_cluster
}


resource "aws_ecs_service" "ECS_APP_SERVICE" {
  
  cluster          = aws_ecs_cluster.ECS_APP_CLUSTER.name
  depends_on       = [
      aws_alb_target_group.webapp,
      aws_iam_role.ECS_TASK_ROLE,
      module.rds.rds_endpoint,
      aws_s3_bucket.ecsBucket
    ]

  name             = "blog_app"
  desired_count    = 1
  task_definition  = aws_ecs_task_definition.ECS_APP.arn
  launch_type      = "FARGATE"
  platform_version = "1.4.0"

  network_configuration {
    
    subnets          = [for s in data.aws_subnet.ecs_app : s.id]
    security_groups  = [aws_security_group.ecs_app.id]
    assign_public_ip = true
  }

  load_balancer {
    
    target_group_arn = aws_alb_target_group.webapp.id
    container_name   = "backend"
    container_port   = 80
  }
}

