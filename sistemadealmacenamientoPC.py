import json
from linkedlist import Node, SingleLink
from pokemoncito import agregar_al_equipo,pokemoncito,guardarpokemonesenlasbuckets,equipo_principal
pc_lista = SingleLink()

def guardar_en_pc(pokemon):
    nuevo_nodo = Node(pokemon)
    pc_lista.link_nodes(nuevo_nodo)
    print(f"{pokemon.nombre} fue enviado a la PC.")

def mostrar_equipo():
    print("Equipo principal actual:")
    for p in equipo_principal:
        print(f"- {p.nombre} (Tipo: {p.tipo}, CP: {p.pc})")

def mostrar_pc():
    print("Pokémon almacenados en la PC:")
    current = pc_lista.head
    while current is not None:
        p = current.data
        print(f"- {p.nombre} (Tipo: {p.tipo}, CP: {p.pc})")
        current = current.next

def cargar_pokemones_desde_json():
    with open("jansooon/minipokedex.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)

    for dato in datos:
        nuevo_pokemon = pokemoncito(dato["id"], dato["nombre"], dato["tipo"], dato["cp"])
        agregar_al_equipo(nuevo_pokemon)

def cargar_pokemones_desdejson(datos):
    for dato in datos:
        nuevo_pokemon = pokemoncito(dato["id"], dato["nombre"], dato["tipo"], dato["cp"])
        agregar_al_equipo(nuevo_pokemon)

    mostrar_equipo()
    mostrar_pc()

    datos = guardarpokemonesenlasbuckets()
    cargar_pokemones_desdejson(datos)