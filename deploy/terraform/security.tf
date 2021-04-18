# --------------- SECURITY GROUPS -------------


resource "aws_security_group" "ecs_app" {
  name        = "ecs_app"
  description = "Allow webapp ECS inbound traffic"
  vpc_id      = data.aws_vpc.default.id

  ingress {
    description = "for http , nginx"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "for django"
    from_port   = 8000
    to_port     = 8000
    protocol    = "tcp"
    cidr_blocks = [data.aws_vpc.default.cidr_block]
  }

  egress {
    description = "for http"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "ecs app"
  }
}

resource "aws_security_group" "rds" {
  name        = "rds_ecs_app"
  description = "Allow webapp ECS inbound traffic"
  vpc_id      = data.aws_vpc.default.id

  ingress {
    description = "TLS from RDS"
    from_port   = 5432
    to_port     = 5432
    protocol    = "tcp"
    cidr_blocks = [data.aws_vpc.default.cidr_block]
  }

  egress {
    description = "for http"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = [data.aws_vpc.default.cidr_block]
  }
  tags = {
      Name = "RDS ecs app"
  }
}
