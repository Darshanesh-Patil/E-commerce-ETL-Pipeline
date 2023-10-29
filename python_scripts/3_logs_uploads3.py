# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 23:24:44 2023

@author: darsh
"""

import boto3

AWS_S3_BUCKET_NAME = 'bucketname'
AWS_REGION = 'ap-south-1'
AWS_ACCESS_KEY = 'accesskey'
AWS_SECRET_KEY = 'key'

LOCAL_FILE = r'localpath'
NAME_FOR_S3 = 'raw_data_dynamic_logs/purchase_online_log.csv'

def main():
    print('in main method')

    s3_client = boto3.client(
        service_name='s3',
        region_name=AWS_REGION,
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY
    )

    try:
        s3_client.upload_file(LOCAL_FILE, AWS_S3_BUCKET_NAME, NAME_FOR_S3)
        print('File uploaded successfully.')
    except Exception as e:
        print(f'Error uploading the file to AWS S3: {e}')

if __name__ == '__main__':
    main()
