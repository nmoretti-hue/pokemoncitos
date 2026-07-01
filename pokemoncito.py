import json
from sanarequipo import sanar_equipo
from desafioaliderdegimnasio import elegir_gimnasio, medallas_entrenador
from hashtable.hashmap import HashMap
from hashtable.hashset import HashSet

class pokemoncito:
    def __init__(self,id,nombre,tipo,pc):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.pc = pc

def guardarpokemonesenlasbuckets():
    minipokedex = HashMap()
    with open("minipokedex.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
        for pokemoncito in datos:
            minipokedex.agregar(pokemoncito["id"], pokemoncito)
        minipokedex.mostrar()
    return datos

def abrirjansonmedalls():
    with open("medallas.json", "r") as archivo:
        medallas_json = json.load(archivo)
    nombres_medallas = [m["nombre"] for m in medallas_json]
    medallas_entrenador = set()

    return medallas_entrenador, nombres_medallas

def precargarmedallas(medallas_entrenador, nombres_medallas):
    medallas_entrenador.add(nombres_medallas[0])
    medallas_entrenador.add(nombres_medallas[1])
    print("Medallas precargadas:")
    print(medallas_entrenador)
    print()

def agregar_medalla(medallas_entrenador,nombre_medalla):
    if nombre_medalla in medallas_entrenador:
        print(f"La '{nombre_medalla}' ya está en el registro.")
    else:
        medallas_entrenador.add(nombre_medalla)
        print(f"Se agrego la '{nombre_medalla}' correctamente.")


    print()
    print("Estado final del registro de medallas:")
    print(medallas_entrenador)

entrenador, nombres = abrirjansonmedalls()
precargarmedallas(entrenador, nombres)


"///////////////////////////////////////////////////////////////"


equipo_principal = []
Pc = []

def agregar_al_equipo(pokemon):
    if len(equipo_principal) < 6:
        equipo_principal.append(pokemon)
        print(f"{pokemon.nombre} se agregó al equipo principal.")
    else:
        Pc.append(pokemon)
        print(f"El equipo ya tiene 6 Pokemon. {pokemon.nombre} fue enviado a la PC automaticamente.")

def mostrar_equipo():
    print("Equipo principal actual:")
    for p in equipo_principal:
        print(f"- {p.nombre} (Tipo: {p.tipo}, CP: {p.pc})")

def mostrar_pc():
    print("Pokemon en la PC:")
    for p in Pc:
        print(f"- {p.nombre} (Tipo: {p.tipo}, CP: {p.pc})")
def cargar_pokemones_desde_json(datos):
    for dato in datos:
        nuevo_pokemon = pokemoncito(dato["id"], dato["nombre"], dato["tipo"], dato["cp"])
        agregar_al_equipo(nuevo_pokemon)

    mostrar_equipo()
    mostrar_pc()

datos = guardarpokemonesenlasbuckets()
cargar_pokemones_desde_json(datos)


"///////////////////////////////////////////////////////////////"


sanar_equipo(equipo_principal)


"///////////////////////////////////////////////////////////////"

def pruebasinmenu():
    for intento in range(3):
        print(f" INTENTO {intento + 1}")
        elegir_gimnasio()

    print(" MEDALLAS FINALES ")
    medallas_entrenador.mostrar()
pruebasinmenu()

"///////////////////////////////////////////////////////////////"

