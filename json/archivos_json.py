import json 
with open("files/json/personas.json", 'r') as archivo:
    dato = json.load(archivo)

print(dato['personas'])