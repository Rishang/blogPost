resource "aws_s3_bucket" "ecsBucket" {
  bucket = var.webapp_bucket

  # force_destroy = true
  cors_rule {
    allowed_headers = ["*"]
    allowed_methods = ["GET","PUT", "POST", "DELETE"]
    allowed_origins = ["*"]
    expose_headers  = ["x-amz-request-id","x-amz-id-2"]
    max_age_seconds = 3000
  }

}

resource "aws_s3_bucket_policy" "ecsBucket" {
  bucket = aws_s3_bucket.ecsBucket.id

  policy = <<POLICY
{
  "Version": "2012-10-17",
  "Id": "s3PublicPolicy",
  "Statement": [
    {
      "Sid": "IPAllow",
      "Effect": "Allow",
      "Principal": {
              "AWS":"*"
          },
      "Action":"s3:GetObject",
      "Resource": "${aws_s3_bucket.ecsBucket.arn}/*"
    }
  ]
}
POLICY
}