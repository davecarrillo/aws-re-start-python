
import logging
import boto3
from botocore.exceptions import ClientError
import os

def list_buckets():
    # Retrieve the list of existing buckets
    s3 = boto3.client('s3')
    response = s3.list_buckets()

    # Output the bucket names
    print('Existing buckets:')
    for bucket in response['Buckets']:
        print(f'  {bucket["Name"]}')

def create_bucket(bucket_name, region=None):
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
    return True

def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True
    
def read_file_from_s3(bucket_name, s3_object_key):
    """
    Read a file from an S3 bucket.

    :param bucket_name: The name of the S3 bucket.
    :param s3_object_key: The key (path) to the S3 object.
    :return: The content of the file as a string, or None if the file doesn't exist.
    """
    try:
        s3 = boto3.client('s3')
        response = s3.get_object(Bucket=bucket_name, Key=s3_object_key)
        content = response['Body'].read().decode('utf-8')
        return content
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "NoSuchKey":
            print(f"The object with key '{s3_object_key}' does not exist in the bucket '{bucket_name}'.")
        else:
            print(f"Error reading the object: {e}")
        return None
    
def main():
    bucket_name = 'test-boto3-d'
    object_key = 'test.txt'
    
    list_buckets()
    # create_bucket("test-boto3-da", "us-west-2")
    upload_file("aws-re-start-python/boto3/test.txt", "test-boto3-d")
    
    file_content = read_file_from_s3(bucket_name, object_key)
    if file_content is not None:
        print(f'File content:\n{file_content}')

if __name__ == '__main__':
    main()