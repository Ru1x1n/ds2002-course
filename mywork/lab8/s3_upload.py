import boto3

s3 = boto3.client('s3', region_name='us-east-1')

bucket = 'ds2002-ama8us'
local_file = 'cloud.jpg'
key = 'cloud.jpg'

s3.upload_file(local_file, bucket, key)

print("success")