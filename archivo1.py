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



#res = crear_archivo("texto.txt", "x")


resultado = eliminar_archivo("josueee.txt")
#resultado = escribir_archivo("texto.txt", "josue", "estoy escribiendo un archivo")
#resultado = escribir_archivo("texto.txt", "j", "agregando contenido al archivo")


