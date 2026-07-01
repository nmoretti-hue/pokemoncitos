from sorts import bubble_sort, selection_sort, quick_sort
from sistemadealmacenamientoPC import pc_lista

def obtener_lista_de_pc():
    lista_temporal = []
    current = pc_lista.head
    while current is not None:
        lista_temporal.append(current.data)
        current = current.next
    return lista_temporal

def mostrar_lista(lista, atributo):
    print(f"\nPokémon ordenados por {atributo}:")
    for tupla in lista:
        p = tupla[1]
        print(f"- {p.nombre} (Tipo: {p.tipo}, CP: {p.pc})")

def ordenar_por_nombre():
    lista = obtener_lista_de_pc()
    if not lista:
        print("La PC está vacía.")
        return

    tuplas = [(p.nombre, p) for p in lista]
    tuplas = bubble_sort(tuplas)

    mostrar_lista(tuplas, "nombre (A-Z)")

def ordenar_por_tipo():
    lista = obtener_lista_de_pc()
    if not lista:
        print("La PC está vacía.")
        return
    
    tuplas = [(p.tipo, p) for p in lista]
    tuplas = selection_sort(tuplas)

    mostrar_lista(tuplas, "tipo")

def ordenar_por_cp():
    lista = obtener_lista_de_pc()
    if not lista:
        print("La PC está vacía.")
        return

    tuplas = [(-p.pc, p) for p in lista]
    quick_sort(tuplas)

    mostrar_lista(tuplas, "CP (mayor a menor)")

def menu_organizacion():
    while True:
        print("ORGANIZACIÓN DE LA PC ")
        print("1. Ordenar por nombre (A-Z) - Bubble Sort")
        print("2. Ordenar por tipo - Selection Sort")
        print("3. Ordenar por CP (mayor a menor) - Quick Sort")
        print("4. Volver")

        opcion = input("Elegí una opción: ")

        if opcion == "1":
            ordenar_por_nombre()
        elif opcion == "2":
            ordenar_por_tipo()
        elif opcion == "3":
            ordenar_por_cp()
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")