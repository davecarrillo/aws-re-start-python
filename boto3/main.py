def main():
    # Configura tus credenciales y región de AWS
    # access_key = 'YOUR_ACCESS_KEY'
    # secret_key = 'YOUR_SECRET_KEY'
    # region_name = 'us-east-1'  # Reemplaza con tu región

    # Crea una instancia de S3Manager
    s3_manager = S3Manager(access_key, secret_key, region_name)

    # Nombre de tu bucket y objeto de prueba
    bucket_name = 'my-test-bucket'
    object_name = 'test.txt'

    # Crea un bucket
    if s3_manager.create_bucket(bucket_name):
        print(f'Bucket {bucket_name} creado exitosamente.')
    else:
        print(f'Error al crear el bucket {bucket_name}.')

    # Sube un archivo
    file_content = 'Hello, AWS S3!'
    if s3_manager.upload_file(bucket_name, 'test.txt', object_name):
        print(f'Archivo {object_name} subido al bucket {bucket_name} exitosamente.')
    else:
        print(f'Error al subir el archivo {object_name} al bucket {bucket_name}.')

    # Lee el archivo
    retrieved_content = s3_manager.read_file(bucket_name, object_name)
    if retrieved_content:
        print(f'Contenido del archivo: {retrieved_content.decode()}')
    else:
        print(f'Error al leer el archivo {object_name}.')

    # Actualiza el archivo
    new_content = 'Updated content'
    if s3_manager.update_file(bucket_name, object_name, new_content.encode()):
        print(f'Archivo {object_name} actualizado exitosamente.')
    else:
        print(f'Error al actualizar el archivo {object_name}.')

    # Lee el archivo actualizado
    retrieved_content = s3_manager.read_file(bucket_name, object_name)
    if retrieved_content:
        print(f'Contenido del archivo actualizado: {retrieved_content.decode()}')
    else:
        print(f'Error al leer el archivo actualizado {object_name}.')

    # Elimina el archivo
    if s3_manager.delete_file(bucket_name, object_name):
        print(f'Archivo {object_name} eliminado exitosamente.')
    else:
        print(f'Error al eliminar el archivo {object_name}.')

    # Elimina el bucket
    if s3_manager.delete_bucket(bucket_name):
        print(f'Bucket {bucket_name} eliminado exitosamente.')
    else:
        print(f'Error al eliminar el bucket {bucket_name}.')

if __name__ == '__main__':
    main()
