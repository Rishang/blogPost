# ---------------- network ------------------

# current using default vpc , subnets

# --------------------- RDS --------------------

variable "rds_db_name" {
  type      = string
  sensitive = true
}
variable "rds_db_username" {
  type      = string
  sensitive = true
}
variable "rds_db_password" {
  type      = string
  sensitive = true
}

# ------------------- LOG GROUP ---------------

variable "log_group_prefix" {
  type    = string
  default = "/ecs/terraform"
}

# ------------------- ECS ---------------------

variable "app_cluster" {
  type = string
  description = "ecs cluster name"
}

variable "ecs_iam_role_name" {
  type        = string
  description = "IAM execution role for ecs"
  default     = "s3ForEcs"
}

# ----------------------- ECS TASK-Defination----------------

variable "task_defiantion_family" {
  type     = string
  default  = "testHello" 
}

variable "REPO_NAME" {
  type        = string
  description = "ECR repo name"
}

variable "GIT_COMMIT" {
  type        = string
  description = "Git commit version"
}

# ------------- ECS TASK -> CONTAINER DEFINATIONS -----------------

variable "app_state" {
  type = string
  description = "stage of app, dev/prog"
  default = "PRODUCTION"
}

variable "DATABASE" {
  type = string
  default  = "postgres"
}       

variable "DATABASE_PORT" {
  type = string
  default = "5432"
}   
  
variable "DATABASE_ENGINE" {
  type = string
}

variable "DJANGO_SECRET_KEY" {
  type        = string
  description = "Configs for django app settings"
  sensitive = true
}   

variable "DJANGO_ADMIN_USERNAME" {
  type        = string
  description = "Configs for django app settings"
  sensitive = true
} 

variable "DJNGO_ADMIN_EMAIL" {
  type        = string
  description = "Configs for django app settings"
  sensitive = true
}

variable "DJNGO_ADMIN_PASSWORD" {
  type        = string
  description = "Configs for django app settings"
  sensitive = true
}

variable "DJANGO_ALLOWED_HOST" {
  type        = string
  description = "Configs for django app settings"
  sensitive = true
}

variable "DJANGO_DEBUG_MODE" {
  type        = string
  description = "Configs for django app settings, 0 = False, 1 = True"
}


# -------------------- S3 bucket  -------------------------

variable "webapp_bucket" {
  type        =   string
  description = "S3 bucket for  webapp, ECS taks roles"
}
