import boto3

s3 = boto3.resource('s3')
my_bucket = s3.Bucket('test-boto3-d')

for my_bucket_object in my_bucket.objects.all():
    print(my_bucket_object.key)