# E-commerce-ETL-Pipeline

## **Abstract**:

This ETL (Extract, Transform, Load) pipeline project leverages Amazon Web Services (AWS) to manage and process simulated user purchase data. The project focuses on generating, storing, processing, and visualizing data to provide insights. It employs various AWS services, including Amazon S3, AWS Glue, AWS Lambda, AWS Quicksight, and AWS Athena, along with Identity and Access Management (IAM) for secure access control. The pipeline automates the ingestion of data, its transformation, and the creation of dynamic dashboards for data analysis, ensuring the efficient and effective use of cloud resources.

## **Architecture Diagram**:

![alt text](https://github.com/Darshanesh-Patil/E-commerce-ETL-Pipeline/blob/7a49f2edd2fc30501206b921e5385ae3e609d269/Architecture-Diagram.jpg?raw=true)

## **Scope**:

The scope of this project encompasses the following key components:

1. **Data Generation and Storage**: Simulated user purchase data is generated and stored in an Amazon S3 bucket. This includes periodic updates to the data through a Python script.

2. **Data Extraction and Transformation**: AWS Glue is used to extract data from the S3 bucket via a crawler, and an ETL job is executed for data transformation. The transformation process includes cleaning, filtering, and aggregating the data.

3. **Incremental Processing**: Job bookmarks are employed to optimize the ETL process by selectively processing newly updated data, minimizing resource usage.

4. **Trigger Mechanism**: An AWS Lambda function is responsible for automatically triggering the AWS Glue Crawler and ETL job when updates to the purchase log occur in the S3 bucket.

5. **Data Visualization**: AWS Quicksight is utilized to create interactive dashboards and visualizations for data analysis and reporting.

6. **Access Control**: IAM roles are used to ensure secure and controlled access to AWS resources, safeguarding sensitive data and operations.

## **Objectives**:

The main objectives of this ETL pipeline project are:

1. **Efficient Data Management**: Enable efficient storage, retrieval, and processing of simulated user purchase data using Amazon S3, AWS Glue, and AWS Lambda.

2. **Data Transformation**: Transform raw data into a structured format that is suitable for analysis and reporting using AWS Glue's ETL capabilities.

3. **Incremental Updates**: Optimize the processing of newly updated data by implementing job bookmarks in the ETL process.

4. **Automation**: Automate the entire data pipeline by triggering the AWS Glue Crawler and ETL job using an AWS Lambda function when data changes occur.

5. **Data Visualization**: Create dynamic and interactive dashboards and visualizations with AWS Quicksight for stakeholders and team members to gain insights and perform data analysis.

6. **Security and Access Control**: Implement secure and controlled access to AWS resources using IAM roles, ensuring data integrity and compliance.

By achieving these objectives, the project aims to provide a robust, automated, and secure solution for managing and deriving insights from user purchase data in an AWS environment.
