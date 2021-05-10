# Blog app with CI/CD

Details about blog web application ([Click here](https://github.com/Rishang/blogPost/tree/master/webapp))

Details about delpoyment ([Click here](https://github.com/Rishang/blogPost/tree/master/deploy))

## Setup on jenkins

Install required packages

- [python3](https://www.python.org/downloads/)
- [docker](https://docs.docker.com/engine/install/)
- [terraform](https://www.terraform.io/downloads.html)
- `pip install -U awscli boto3`

Initially you have to setup jenkins credentials required running the pipeline

| Credential_id   | Type    | Description
| -------------   | ----    | ------
| aws-account-id  | text    | aws account id
| env_dev         | file    | dev environment vars file, [Example](https://github.com/Rishang/blogPost/blob/master/webapp/env.dev.example)
| aws_credentials | file    | [aws credentials](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html) for aws cli
| tfvars | file | terraform secrets vars file, [Example](https://github.com/Rishang/blogPost/blob/master/deploy/terraform/tfvars.example)

## Setting up pipeline

- Open blueoceans in jenkins

- Add new pipline (Github), and provide the access token of github there

- Done the pipeline will automatically start

- For continuous pipeline you can configure sheduled fetch updates from the github repo
