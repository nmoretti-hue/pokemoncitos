import json
import random
from hashmap import HashMap
from hashset import HashSet


class pokemoncito:
    def __init__(self,id,nombre,tipo,pc):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.pc = pc

def guardarpokemonesenlasbuckets():
    minipokedex = HashMap()
    with open("minipokedex.json", "r") as archivo:
        datos = json.load(archivo)
        for pokemoncito in datos:
            minipokedex.agregar(pokemoncito["id"], pokemoncito)
        minipokedex.mostrar()

def guardarmedallasenlasbuckets():
    medallas = HashSet()
    with open("medallas.json", "r") as archivo:
        datos = json.load(archivo)
    medallas.agregar(datos)
    


