import boto3

def lambda_handler(event, context):
    # Check if the event is from S3 and has relevant information
    if 'Records' in event:
        s3_record = event['Records'][0]['s3']
        bucket_name = s3_record['bucket']['name']
        object_key = s3_record['object']['key']

        # Check if the object key matches the desired path
        if object_key == 'raw_data_dynamic_logs/purchase_online_log.csv':
            glue_client = boto3.client('glue')
            
            # Trigger the AWS Glue Crawler
            crawler_name = 'purchase_data_logs'
            glue_client.start_crawler(Name=crawler_name)
            
            # Wait for the crawler to finish running
            while True:
                response = glue_client.get_crawler(Name=crawler_name)
                crawler_state = response['Crawler']['State']
                if crawler_state == 'READY':
                    break

            # Trigger the AWS Glue ETL Job
            etl_job_name = 'ETL Job'
            glue_client.start_job_run(JobName=etl_job_name)
            
            return {
                'statusCode': 200,
                'body': 'Crawler and ETL Job execution started.'
            }
        else:
            return {
                'statusCode': 400,
                'body': 'Object key does not match the desired path.'
            }
    else:
        return {
            'statusCode': 400,
            'body': 'Event is not from S3.'
        }

