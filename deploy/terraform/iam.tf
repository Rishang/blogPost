
resource "aws_iam_role" "ECS_TASK_ROLE" {

  name = var.ecs_iam_role_name
  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "ecs-tasks.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF

  tags = {
    tag-key = "tag-value"
  }

}

resource "aws_iam_role_policy" "s3BucketEcs" {
	name = var.ecs_iam_role_name
  role = aws_iam_role.ECS_TASK_ROLE.id

  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AccessS3Console",
      "Effect": "Allow",
      "Action": [
        "s3:GetBucketLocation",
        "s3:ListBucket"
      ],
     "Resource": [
        "${aws_s3_bucket.ecsBucket.arn}"
      ]
    },
    {
      "Sid": "ModifyBucketPolicy",
      "Effect": "Allow",
      "Action": [
        "s3:PutObject",
        "s3:GetObjectAcl",
        "s3:GetObject",
        "s3:ListBucket",
        "s3:DeleteObject",
        "s3:PutObjectAcl"
      ],
      "Resource": [
         "${aws_s3_bucket.ecsBucket.arn}/*"
      ]
    }
  ]
}
EOF
}
