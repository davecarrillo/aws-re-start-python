import subprocess

"""
Ejercicio 2: Listar el Contenido de un Directorio
Enunciado: Crea un programa en Python que liste el contenido de un directorio 
específico proporcionado por el usuario. Debe mostrar los archivos y 
subdirectorios presentes en el directorio especificado.
"""

def listar_contenido_directorio(ruta_directorio):
    try:
        comando = f"ls {ruta_directorio}"
        contenido = subprocess.check_output(comando, shell=True, text=True)
        print(f"Contenido del directorio '{ruta_directorio}':")
        print(contenido)
    except subprocess.CalledProcessError as e:
        print(f"Error al listar el contenido del directorio: {e}")
    except Exception as e:
        print(f"Otro error inesperado: {e}")

def main():
    subprocess.run(["pwd"])
    subprocess.run(["ls"])
    ruta_directorio = input("Ingresa la ruta del directorio que deseas listar: ")

    listar_contenido_directorio(ruta_directorio)

if __name__ == "__main__":
    main()