import json
from hashtable.hashmap import HashMap

class pokemoncito:
    def __init__(self,id,nombre,tipo,pc):
            self.id = id
            self.nombre = nombre
            self.tipo = tipo
            self.pc = pc

def guardarpokemonesenlasbuckets():
    minipokedex = HashMap()
    with open("jansooon/minipokedex.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
        for pokemoncito in datos:
            minipokedex.agregar(pokemoncito["id"], pokemoncito)
        minipokedex.mostrar()
    return datos

equipo_principal = []
Pc = []

def agregar_al_equipo(pokemon):
    if len(equipo_principal) < 6:
            equipo_principal.append(pokemon)
            print(f"{pokemon.nombre} se agregó al equipo principal.")
    else:
            Pc.append(pokemon)
            print(f"El equipo ya tiene 6 Pokemon. {pokemon.nombre} fue enviado a la PC automaticamente.")


