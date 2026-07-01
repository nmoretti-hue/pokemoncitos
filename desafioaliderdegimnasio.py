import json
import random
from hashtable.hashset import HashSet
from pokemoncito import equipo_principal

def cargar_gimnasios():
    with open("jansooon/medallas.json", "r", encoding="utf-8") as archivo:
        medallas_json = json.load(archivo)

    nombres_medallas = [m["nombre"] for m in medallas_json]

    lideres = ["Brock", "Misty", "Lt. Surge", "Erika", "Sabrina", "Koga", "Blaine", "Giovanni"]

    gimnasios = []
    for i in range(len(lideres)):
        gimnasios.append({"lider": lideres[i], "medalla": nombres_medallas[i]})

    return gimnasios,nombres_medallas
gimnasios, nombres_medallas = cargar_gimnasios()
medallas_entrenador = HashSet()

def precargar_medallas():
    medallas_entrenador.agregar(nombres_medallas[0])
    medallas_entrenador.agregar(nombres_medallas[1])

def elegir_gimnasio():
    equipo_debilitado = True
    for pokemon in equipo_principal:
        if pokemon.vida > 0:
            equipo_debilitado = False

    if equipo_debilitado:
        print("Tu equipo está debilitado. Andá al Centro Pokémon antes de pelear.")
        return
    
    print("Elegí un gimnasio para desafiar:")
    for i, gym in enumerate(gimnasios):
        print(f"{i + 1}. Líder {gym['lider']} ({gym['medalla']})")

    opcion = int(input("Numero de gimnasio: "))

    if opcion < 1 or opcion > 8:
        print("Opcion invalida.")
        return

    gimnasio_elegido = gimnasios[opcion - 1]
    pelear_contra_lider(gimnasio_elegido)

def pelear_contra_lider(gimnasio):
    print(f"Estas peleando contra {gimnasio['lider']}...")
    gano = random.choice([True, False])

    if gano:
        print(f"¡Ganaste contra {gimnasio['lider']}!")
        medallas_entrenador.agregar(gimnasio["medalla"])
    else:
        print(f"Perdiste contra {gimnasio['lider']}. No conseguis la medalla.")
        for pokemon in equipo_principal:
            pokemon.vida = 0
        print("Tu equipo quedó debilitado. Andá al Centro Pokémon a curarlos.")
