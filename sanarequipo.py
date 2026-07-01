import time
from extras.Queue import Queue

def sanar_equipo(equipo_principal):
    cola_centro = Queue()
    for pokemon in equipo_principal:
        cola_centro.enqueue(pokemon)

    print("Centro Pokemon: iniciando curación del equipo")
    print(f"Pokémon en espera: {cola_centro.size()}\n")

    while not cola_centro.is_empty():
        pokemon_actual = cola_centro.dequeue()
        print(f"Curando a {pokemon_actual.nombre}")
        time.sleep(1)
        print(f"{pokemon_actual.nombre} está totalmente curado.")

    print("Todo el equipo fue curado con exito.")