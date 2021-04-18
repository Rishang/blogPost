output "vpc" {
  value = {
    "id"               = data.aws_vpc.default.id,
    "cidr_block"       = data.aws_vpc.default.cidr_block
    "owner_id"         = data.aws_vpc.default.owner_id
    "instance_tenancy" = data.aws_vpc.default.instance_tenancy
  }
}

output "rds_endpoint" {
  value = module.rds.rds_endpoint
}

output "alb_dns" {
  value = "${aws_alb.main.dns_name}:${aws_alb_listener.front_end.port}"
}