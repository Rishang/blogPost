terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
    }
  }
}

# ------------ TF State Backup ----------

terraform {
  backend "s3" {
    bucket  = "170770106047-terraform-tfstate"
    key     = "global/s3/terraform.tfstate"
    encrypt = true
    region  = "us-east-1"
  }
}

# ----------- DATA SOURCES --------------

data "aws_vpc" "default" {
  default = true
}

data "aws_subnet_ids" "ecs_app" {
  vpc_id = data.aws_vpc.default.id
}

data "aws_subnet" "ecs_app" {
  for_each = data.aws_subnet_ids.ecs_app.ids
  id       = each.value
}


data "aws_ecr_repository" "ECS_APP" {
  name = var.REPO_NAME
}


data "aws_iam_role" "ECS_EXECUTION_ROLE" {
  name = "ecsTaskExecutionRole"
}

# data "aws_iam_role" "ECS_TASK_ROLE" {
#   name = var.ecs_iam_role_name
# }

# ------------- LOG GROUPS -----------------

resource "aws_cloudwatch_log_group" "ECS_APP" {
  
  name = "${var.log_group_prefix}/django"
  tags = {
    Terraform   = "true"
    Environment = "dev"
    Application = "service"
  }
}
