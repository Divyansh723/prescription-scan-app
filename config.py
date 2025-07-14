import os

class Config:
    UPLOAD_FOLDER = 'static/uploads/'
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
    AWS_ACCESS_KEY_ID = '<your_aws_access_key_id>'
    AWS_SECRET_ACCESS_KEY = '<your_aws_secret_access_key>'
    AWS_REGION_NAME = '<your_aws_region>'