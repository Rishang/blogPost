

resource "aws_alb_target_group" "webapp" {
  name        = "backend"
  port        = 80
  protocol    = "HTTP"
  vpc_id      = data.aws_vpc.default.id
  target_type = "ip"

  health_check {
    healthy_threshold   = "3"
    interval            = "30"
    protocol            = "HTTP"
    matcher             = "200"
    timeout             = "3"
    path                = "/"
    unhealthy_threshold = "2"
  }
}

# -------------- ALB for ECS ----------------

resource "aws_alb" "main" {
  name            = "app-load-balancer"
  subnets         = [ for s in data.aws_subnet.ecs_app : s.id ]
  security_groups = [
      aws_security_group.ecs_app.id,
    	aws_security_group.rds.id
		]
}

# Redirect all traffic from the ALB to the target group
resource "aws_alb_listener" "front_end" {
  load_balancer_arn = aws_alb.main.id
  port              = 80
  protocol          = "HTTP"

  default_action {
    target_group_arn = aws_alb_target_group.webapp.id
    type             = "forward"
  }
}