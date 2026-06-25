from stack import Stack

stack_transferencias = Stack()

def transferir_a_oak(pokemon):
    if stack_transferencias.size() >= 5:
        stack_transferencias.items.pop(0)
        print("El stack ya tenía 5 transferencias, se elimino la mas antigua.")

    stack_transferencias.push(pokemon)
    print(f"{pokemon.nombre} fue transferido al Profesor Oak.")

def deshacer_transferencia():
    if stack_transferencias.is_empty():
        print("No hay transferencias para deshacer.")
        return None

    pokemon_recuperado = stack_transferencias.pop()
    print(f"Se deshizo la transferencia de {pokemon_recuperado.nombre}. Vuelve a la PC.")
    return pokemon_recuperado

def mostrar_transferencias():
    print("Ultimos Pokemon transferidos al Profesor Oak:")
    stack_transferencias.mostrar()