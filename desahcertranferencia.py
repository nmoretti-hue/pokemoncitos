from extras.stack import Stack
from sistemadealmacenamientoPC import pc_lista, mostrar_pc, guardar_en_pc

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
    guardar_en_pc(pokemon_recuperado)
    print(f"Se deshizo la transferencia de {pokemon_recuperado.nombre}. Vuelve a la PC.")
    return pokemon_recuperado

def mostrar_transferencias():
    print("Ultimos Pokemon transferidos al Profesor Oak:")
    for pokemon in stack_transferencias.items:
        print(f"- {pokemon.nombre} (Tipo: {pokemon.tipo}, CP: {pokemon.pc})")

def transferir_pokemon_de_pc():
    mostrar_pc()

    if pc_lista.is_empty():
        print("No hay Pokemon en la PC para transferir.")
        return

    nombre = input("Nombre del Pokemon a transferir al Profesor Oak: ")

    current = pc_lista.head
    while current is not None:
        if current.data.nombre.lower() == nombre.lower():
            if current.prev is not None:
                current.prev.next = current.next
            else:
                pc_lista.head = current.next

            if current.next is not None:
                current.next.prev = current.prev
            else:
                pc_lista.tail = current.prev

            transferir_a_oak(current.data)
            return

        current = current.next

    print(f"{nombre} no esta en la PC.")