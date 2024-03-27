import os
import sys
"""
Ejercicio: Manejo de archivos con excepciones

Crea un programa en el que el usuario pueda realizar operaciones básicas de manejo de archivos, como crear, leer, escribir y eliminar archivos. 
El programa debe implementar el manejo de excepciones para manejar situaciones como archivos que no existen, errores de lectura o escritura, entre otros.
La consigna detallada del ejercicio es la siguiente:

Menú de opciones: El programa debe presentar al usuario un menú con las siguientes opciones:

Crear un nuevo archivo.
Leer el contenido de un archivo existente.
Escribir en un archivo existente.
Eliminar un archivo existente.
Salir del programa.

"""


def crear_archivo(nombre, tipo_lectura):
    try:
        file = open(nombre, tipo_lectura)
        print("El archivo se ha creado correctamente")
        return file
    

    except FileExistsError:
        print("El archivo ya existe en el directorio")


def escribir_archivo(nombre_archivo, tipo_lectura, texto):
    file = nombre_archivo
    if os.path.exists(file):
        with open (nombre_archivo, tipo_lectura) as file:
            file.write(texto)


def eliminar_archivo(archivo_a_eliminar):
    try:
        eliminar = archivo_a_eliminar
        if os.path.exists(eliminar):
            os.remove(eliminar)
            print("el archivo se ha eliminado")
        else:
            raise FileNotFoundError("El archivo que queres eliminar no existe")
        
    except FileNotFoundError as error:
        print(error)
        
    except FileExistsError:
        print("El archivo que queres eliminar no existe")


#res = crear_archivo("texto.txt", "x")
#resultado = eliminar_archivo("texto.txt")
resultado = escribir_archivo("texto.txt", "w", "estoy escribiendo un archivo")
