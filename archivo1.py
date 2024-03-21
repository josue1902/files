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

class Archivos:
    def __init__(self, crear, leer, sobrescribir, eliminar, salir):
        self.crear = crear
        self.leer = leer
        self.sobrescribir = sobrescribir
        self.eliminar = eliminar
        self.salir = salir

    def crear_archivo(self,nombre, tipo):
        file = open(nombre, tipo)
        print("se ha creado el archivo correctamen")

        


archivo_prueba = Archivos()

archivo_prueba.crear("prueba.txt", "w")

