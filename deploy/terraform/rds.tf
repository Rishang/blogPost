# ------------- DATABASE ----------------------

module "rds" {
  
  source        = "../modules/rds"
  database_type = {
    "name"                 = "postgres"
    "engine_version"       = "12.5"
    "port"                 = 5432
    "parameter_group_name" = "default.postgres12"
  }

  rds_db_storage = {
    "min_storage" = 21
    "max_storage" = 22
  }

  rds_identifier       = "ecs-app"
  rds_db_name          = var.rds_db_name
  rds_db_username      = var.rds_db_username
  rds_db_password      = var.rds_db_password
  subnet_group_name    = "${data.aws_vpc.default.instance_tenancy}-${data.aws_vpc.default.id}"
  security_group_names = [aws_security_group.rds.id]

  tags = {
    Terraform   = "true"
    Environment = "dev"
  }
}
