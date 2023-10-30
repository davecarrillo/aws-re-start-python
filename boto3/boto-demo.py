import boto3

# Let's use Amazon S3
s3 = boto3.resource('s3')

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)
    
# Crea un nuevo bucket
s3.create_bucket(Bucket="test-boto3-d")

print(f"Bucket '{bucket_name}' creado exitosamente en la región '{region}'.")