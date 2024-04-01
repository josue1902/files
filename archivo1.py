import os
import datetime


def crear_archivo(nombre, tipo_lectura):
    try:
        file = open(nombre, tipo_lectura)
        print("El archivo se ha creado correctamente")
        return file
    

    except FileExistsError as error:
        with open("errores.txt", "a") as archivo:
            fecha_actual = datetime.datetime.now()
            fecha = fecha_actual.strftime("%d-%m-%Y %H:%M")
            archivo.write(str(fecha) + str(error) + "\n")

                
        print("El archivo ya existe en el directorio")


def escribir_archivo(nombre_archivo, tipo_lectura, texto):
    try:
        file = nombre_archivo
        if os.path.exists(file):
            with open (nombre_archivo, tipo_lectura) as file:
                file.write(texto)

        else:
            raise ValueError("El modo de lectura es incorrecto.")


    except ValueError as error:
        with open("errores.txt", "a") as archivo:
            fecha_actual = datetime.datetime.now()
            fecha = fecha_actual.strftime("%d-%m-%Y %H:%M")
            archivo.write(str(fecha) + str(error) + "\n")
        print(error)

def eliminar_archivo(archivo_a_eliminar):
    try:
        eliminar = archivo_a_eliminar
        if os.path.exists(eliminar):
            os.remove(eliminar)
            print("el archivo se ha eliminado")
        else:
            raise FileNotFoundError("El archivo que queres eliminar no existe")
        
    except FileNotFoundError as error:
        with open("errores.txt", "a") as archivo:
            fecha_actual = datetime.datetime.now()
            fecha = fecha_actual.strftime("%d-%m-%Y %H:%M")
            archivo.write(str(fecha) + str(error) + "\n")
        print(error)
        
    #except FileExistsError:
        #print("El archivo que queres eliminar no existe")



#res = crear_archivo("texto.txt", "w")


#resultado = eliminar_archivo("texto.txt")
#resultado = escribir_archivo("texto.txt", "josue", "estoy escribiendo un archivo")
#resultado = escribir_archivo("texto.txt", "j", "agregando contenido al archivo")



#tupla = ()
variable = True

while variable:

    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido: ")
    tupla = (nombre, apellido)

    salir = input("Desea salir?: (y/n): ")
    if salir == "y":
        variable = False

    print(tupla)


    resultado = escribir_archivo("texto.txt", "a", str(tupla))


"""
ACTIVIDAD
Ya tenemos métodos (funciones) que interactúan con archivos txt
Ahora vamos a usar la consola para cargar datos y eliminar, por ahora solo vamos a almacenar nombre y apellido, de modo tupla
es decir (nombre, apellido)
('luis', 'perez')
por cada ingreso se debe guardar una tupla en mi txt, por ahora no vamos a eliminar nada que se guarde
Vamos a generar un bucle while para hacer funcionar nuestro menú
"""
