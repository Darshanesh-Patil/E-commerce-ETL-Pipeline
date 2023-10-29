# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 15:14:32 2023

@author: darsh
"""

import boto3
import PySimpleGUI as sg
from botocore.exceptions import NoCredentialsError

def upload_to_s3(AWS_REGION, AWS_ACCESS_KEY, AWS_SECRET_KEY, LOCAL_FILE, NAME_FOR_S3):
    s3_client = boto3.client(
        service_name='s3',
        region_name=AWS_REGION,
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY
    )

    try:
        s3_client.upload_file(LOCAL_FILE, AWS_S3_BUCKET_NAME, NAME_FOR_S3)
        return True, 'File uploaded successfully.'
    except NoCredentialsError:
        return False, 'AWS credentials are missing or incorrect.'
    except Exception as e:
        return False, f'Error uploading the file to AWS S3: {str(e)}'

AWS_S3_BUCKET_NAME = 'bucketstoragedata'

layout = [
    [sg.Text("AWS Region:"), sg.InputText(key='-REGION-')],
    [sg.Text("AWS Access Key:"), sg.InputText(key='-ACCESS-')],
    [sg.Text("AWS Secret Key:"), sg.InputText(key='-SECRET-', password_char='*')],
    [sg.Text("Local File Path:"), sg.InputText(key='-LOCAL-'), sg.FileBrowse("Browse")],
    [sg.Text("Name for S3:"), sg.InputText(key='-S3_NAME-')],
    [sg.Button("Upload to S3"), sg.Text('', size=(30, 1), key='-RESULT-', text_color='red')],
]

window = sg.Window("AWS S3 Uploader", layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break
    if event == "Upload to S3":
        AWS_REGION = values['-REGION-']
        AWS_ACCESS_KEY = values['-ACCESS-']
        AWS_SECRET_KEY = values['-SECRET-']
        LOCAL_FILE = values['-LOCAL-']
        NAME_FOR_S3 = values['-S3_NAME-']

        success, message = upload_to_s3(AWS_REGION, AWS_ACCESS_KEY, AWS_SECRET_KEY, LOCAL_FILE, NAME_FOR_S3)
        
        if success:
            window['-RESULT-'].update(message, text_color='green')
        else:
            window['-RESULT-'].update(message, text_color='red')

window.close()


