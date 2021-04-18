variable "database_type" {
  type        = map
  description = "Database type and version config"
  default     = {
        "name"                 = ""
        "engine_version"       = ""
        "port"                 = null
        "parameter_group_name" = ""
      }
}

variable "rds_db_storage" {
  type        = map
  description = "Min / Max storage for RDS database"
  default     = {
    "min_storage" = null
    "max_storage" = null
  }
}

variable "rds_identifier" {
  type        = string
  description = "RDS instance name"
  default     = ""
}

variable "rds_db_name" {
  type         = string
  description  = "RDS database name"
}

variable "rds_db_username" {
  type         = string
  description  = "RDS database master user"
}

variable "rds_db_password" {
  type         = string
  description  = "RDS database master password"
}

variable "subnet_group_name" {
  type        = string
  description = "Subnet group name"
  default     = ""
}

variable "security_group_names" {
  type        = list
  description = "Subnet group name"
  default     = []
}

variable "tags" {
  description  =  "Tags for RDS instance"
  type         = map
  default      = {}
}