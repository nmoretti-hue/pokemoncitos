import json
from extras.sorts import bubble_sort
from pokemoncito import equipo_principal


def buscar_en_equipo(nombre):
    for pokemon in equipo_principal:
        if pokemon.nombre.lower() == nombre.lower():
            return pokemon
    return None


def buscar_por_id(pokedex, ids_ordenados, id_buscado):
    low = 0
    high = len(ids_ordenados) - 1

    while low <= high:
        medio = (low + high) // 2

        if ids_ordenados[medio] == id_buscado:
            for pokemon in pokedex:
                if pokemon["id"] == id_buscado:
                    return pokemon
        elif ids_ordenados[medio] < id_buscado:
            low = medio + 1
        else:
            high = medio - 1

    return None


def buscar_pokemon_en_equipo():
    nombre = input("Ingresa el nombre del Pokemon a buscar en el equipo: ")
    resultado_equipo = buscar_en_equipo(nombre)

    if resultado_equipo != None:
        print(f"{resultado_equipo.nombre} esta en el equipo (Tipo: {resultado_equipo.tipo}, CP: {resultado_equipo.pc})")
    else:
        print(f"{nombre} no esta en el equipo.")

def buscar_pokemon_por_id():
    with open("jansooon/minipokedex.json", "r") as archivo:
        pokedex = json.load(archivo)

    ids = [pokemon["id"] for pokemon in pokedex]
    ids = bubble_sort(ids)

    id_buscado = int(input("Ingresá el ID del Pokémon a buscar: "))
    resultado_pokedex = buscar_por_id(pokedex, ids, id_buscado)

    if resultado_pokedex != None:
        print(f"ID {id_buscado} encontrado: {resultado_pokedex['nombre']} (Tipo: {resultado_pokedex['tipo']}, CP: {resultado_pokedex['cp']})")
    else:
        print(f"No existe ningún Pokemon con el ID {id_buscado}.")

def menu_busquedas():
    while True:
        print("BÚSQUEDAS")
        print("1. Buscar Pokémon en el equipo (por nombre)")
        print("2. Buscar Pokémon en la Pokédex (por ID)")
        print("3. Volver")

        opcion = input("Elegí una opción: ")

        if opcion == "1":
            buscar_pokemon_en_equipo()
        elif opcion == "2":
            buscar_pokemon_por_id()
        elif opcion == "3":
            break
        else:
            print("Opción inválida.")
