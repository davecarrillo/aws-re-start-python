import boto3

class S3Manager:
    def __init__(self, access_key, secret_key, region_name):
        # Inicializar el cliente de S3
        self.s3 = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key, region_name=region_name)

    def create_bucket(self, bucket_name):
        # Crear un nuevo bucket
        self.s3.create_bucket(Bucket=bucket_name)

    def upload_file(self, bucket_name, file_path, object_name):
        # Subir un archivo a un bucket de S3
        self.s3.upload_file(file_path, bucket_name, object_name)

    def read_file(self, bucket_name, object_name):
        # Leer el contenido de un archivo de S3
        response = self.s3.get_object(Bucket=bucket_name, Key=object_name)
        return response['Body'].read()

    def update_file(self, bucket_name, object_name, new_content):
        # Actualizar el contenido de un archivo en S3
        self.s3.put_object(Bucket=bucket_name, Key=object_name, Body=new_content)

    def delete_file(self, bucket_name, object_name):
        # Eliminar un archivo de S3
        self.s3.delete_object(Bucket=bucket_name, Key=object_name)

    def delete_bucket(self, bucket_name):
        # Eliminar un bucket de S3
        self.s3.delete_bucket(Bucket=bucket_name)
