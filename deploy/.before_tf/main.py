"""
This script will create s3 bucket on aws which can be used for storing tf states of terrafrom, initially

following env vars are required to be set

ACCOUNT_ID: your aws account id
S3_TFSTATE_BACKEND: name you want to give to your s3 bucket
"""


import logging
import boto3
from botocore.exceptions import ClientError
import os

# require
account_id = os.environ.get("ACCOUNT_ID")
tf_backent_name = os.environ.get("S3_TFSTATE_BACKEND")

if not account_id:
    raise EnvironmentError("ACCOUNT_ID, no account id specified")
elif not tf_backent_name:
    raise EnvironmentError("S3_TFSTATE_BACKEND, no tf_state backup bucket name found")


# Code for AWS TERRAFORM S# BACKEND
def create_bucket(bucket_name:str,bucket_owner_id:str,versioning=False, encrypt=False, region=None):
    
    """Create an S3 bucket in a specified region

    If a region is not specified, the bucket is created in the S3 default
    region (us-east-1).

    :param bucket_name: Bucket to create
    :param region: String region to create bucket in, e.g., 'us-west-2'
    :return: True if bucket created, else False
    """

    # Create bucket
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    
    if versioning == True:
        response = s3_client.put_bucket_versioning(
            Bucket=bucket_name,
            VersioningConfiguration={
                'Status': 'Enabled'
            },
            ExpectedBucketOwner=bucket_owner_id
        )
    if encrypt == True:
        response = s3_client.put_bucket_encryption(
            Bucket=bucket_name,
            ServerSideEncryptionConfiguration={
                'Rules': [
                    {
                        'ApplyServerSideEncryptionByDefault': {
                            'SSEAlgorithm': 'AES256'
                        },
                        'BucketKeyEnabled': True
                    },
                ]
            },
            ExpectedBucketOwner=bucket_owner_id
        )
    
    for i in response:
        print(i)
    return True


# Output the bucket names
# print('Existing buckets:')
s3 = boto3.client('s3')
response = s3.list_buckets()


b=[]
for buckets in response['Buckets']:
    print(buckets["Name"])
    b.append(buckets["Name"])

if tf_backent_name in b:
    print(f"\nbucket {tf_backent_name} Exists")
else:
    print(f"creating {tf_backent_name}")
    create_bucket(
        bucket_name=f"{tf_backent_name}",
        versioning=True,
        encrypt=True,
        bucket_owner_id=f"{account_id}"
    )
