import os
import subprocess

"""
Ejercicio 1: Creación de un Directorio
Enunciado: Crea un programa en Python que permita al usuario ingresar un nombre 
y, a continuación, cree un directorio con ese nombre en el directorio actual. 
Asegúrate de manejar posibles errores, como si el directorio ya existe.
"""
def crear_directorio():
    while True:
        nombre_directorio = input("Ingresa el nombre del directorio a crear: ")
        if os.path.exists(nombre_directorio):
            print(f"El directorio '{nombre_directorio}' ya existe.")
        else:
            try:
                # Intenta crear el directorio utilizando el comando mkdir
                comando = f"mkdir {nombre_directorio}"
                proceso = subprocess.Popen(comando, shell=True)
                proceso.wait()
        
                if proceso.returncode == 0:
                    print(f"Directorio '{nombre_directorio}' creado exitosamente.")
                    return
                else:
                    print(f"No se pudo crear el directorio '{nombre_directorio}'.")
            except Exception as e:
                print(f"Error al crear el directorio: {e}")
        
def main():
    crear_directorio()

if __name__ == "__main__":
    main()