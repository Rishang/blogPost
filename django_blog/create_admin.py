# Create admin user for django app in Docker

# get the env_file_name file
# Check if there is any admin user present, if not create
# user credentials will be take from env_file_name

import os
import environ
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

env_file_name='.env.dev'

if os.path.isfile(env_file_name):
    
    env = environ.Env()
    environ.Env.read_env(env_file_name)
    
    admin_username=env('DJANGO_ADMIN_USERNAME')
    admin_email=env('DJNGO_ADMIN_EMAIL')
    admin_password=env('DJNGO_ADMIN_PASSWORD')

else:
    print("ENV File not found")
    exit
    
try:
    User.objects.get(username=admin_username)

except ObjectDoesNotExist:
    User.objects.create_superuser(admin_username, email=admin_email, password=admin_password)
