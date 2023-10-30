import logging
import boto3
from botocore.exceptions import ClientError
import os

def list_buckets():
    """
    List the existing buckets.
    """
    s3 = boto3.client('s3')
    response = s3.list_buckets()

    print('Existing buckets:')
    for bucket in response['Buckets']:
        print(f'  {bucket["Name"]}')
        
def list_bucket_content(bucket_name):
    """
    List the contents of a bucket.

    :param bucket_name: Bucket to create
    """
    s3 = boto3.resource('s3')
    my_bucket = s3.Bucket(bucket_name)
    print(f'Files in the bucket {bucket_name}:')
    for my_bucket_object in my_bucket.objects.all():
        print(f'    {my_bucket_object.key}')

def create_bucket(bucket_name, region=None):
    """
    Create an S3 bucket in a specified region.

    If a region is not specified, the bucket is created in the S3 default
    region (us-east-1).

    :param bucket_name: Bucket to create.
    :param region: String region to create bucket in, e.g., 'us-west-2'.
    :return: True if bucket created, else False.
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
    """
    Upload a file to an S3 bucket.

    :param file_name: File to upload.
    :param bucket: Bucket to upload to.
    :param object_name: S3 object name. If not specified then file_name is used.
    :return: True if file was uploaded, else False.
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
    except ClientError as e:
        if e.response['Error']['Code'] == "NoSuchKey":
            print(f"The object with key '{s3_object_key}' does not exist in the bucket '{bucket_name}'.")
        else:
            print(f"Error reading the object: {e}")
        return None

def delete_file_from_s3(bucket_name, s3_object_key):
    """
    Delete a file from an S3 bucket.

    :param bucket_name: The name of the S3 bucket.
    :param s3_object_key: The key (path) to the S3 object to delete.
    :return: True if the file was deleted successfully, False if it doesn't exist or an error occurred.
    """
    try:
        s3 = boto3.client('s3')
        s3.delete_object(Bucket=bucket_name, Key=s3_object_key)
        print(f"File with key '{s3_object_key}' has been deleted from the bucket '{bucket_name}'.")
        return True
    except ClientError as e:
        if e.response['Error']['Code'] == "NoSuchKey":
            print(f"The object with key '{s3_object_key}' does not exist in the bucket '{bucket_name}'.")
        else:
            print(f"Error deleting the object: {e}")
        return False
        
def delete_bucket(bucket_name):
    """
    Delete an S3 bucket and its contents.

    :param bucket_name: The name of the S3 bucket to delete.
    :return: True if the bucket was deleted successfully, False if it doesn't exist or an error occurred.
    """
    try:
        s3 = boto3.resource('s3')
        bucket = s3.Bucket(bucket_name)
        bucket.objects.all().delete()
        bucket.delete()
        print(f"Bucket '{bucket_name}' has been deleted.")
        return True
    except ClientError as e:
        if e.response['Error']['Code'] == 'NoSuchBucket':
            print(f"The bucket '{bucket_name}' does not exist.")
        else:
            print(f"Error deleting the bucket: {e}")
        return False
    
def main():
    bucket_name = 'test-boto3-d'
    object_key = 'test.txt'
    region = "us-west-2"
    
    list_buckets()
    
    create_bucket(bucket_name, region)
    
    list_buckets()
    
    upload_file("aws-re-start-python/boto3/test.txt", "test-boto3-d")
    
    list_bucket_content(bucket_name)
    
    file_content = read_file_from_s3(bucket_name, object_key)
    if file_content is not None:
        print(f'File content:\n{file_content}')
    
    
    # success = delete_file_from_s3(bucket_name, object_key)
    # if success:
    #     print('File has been deleted.')
        
    # success = delete_bucket(bucket_name)
    # if success:
    #     print('Bucket has been deleted.')
        
if __name__ == '__main__':
    main()