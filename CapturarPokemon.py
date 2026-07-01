import json
import random
from pokemoncito import agregar_al_equipo, pokemoncito
from sistemadealmacenamientoPC import guardar_en_pc

def capturar_pokemon():
    with open("jansooon/minipokedex.json", "r", encoding="utf-8") as archivo:
        pokedex = json.load(archivo)

    dato = random.choice(pokedex)

    nuevo_pokemon = pokemoncito(dato["id"], dato["nombre"], dato["tipo"], dato["cp"])

    print(f"¡Un {nuevo_pokemon.nombre} salvaje apareció!")

    entro_al_equipo = agregar_al_equipo(nuevo_pokemon)

    if entro_al_equipo == False:
        guardar_en_pc(nuevo_pokemon)