
import sys
sys.path.append("extras")
from sistemadealmacenamientoPC import cargar_pokemones_desde_json,mostrar_equipo,mostrar_pc
from pokemoncito import equipo_principal
from desafioaliderdegimnasio import elegir_gimnasio, medallas_entrenador, precargar_medallas
from sanarequipo import sanar_equipo
from desahcertranferencia import transferir_a_oak, deshacer_transferencia, mostrar_transferencias
from OrganizacióndelAlmacenamiento import menu_organizacion

print("   SISTEMA DE GESTIÓN: POKÉMON HUERGO   ")
print("Inicializando motor de base de datos... OK.")
print("Cargando Pokédex Nacional (15 registros)... OK.")
cargar_pokemones_desde_json()
print("Validando registros de medallas... OK.")
precargar_medallas()


print("   SISTEMA DE GESTIÓN: POKÉMON HUERGO   ")
print("Inicializando motor de base de datos... OK.")
print("Cargando Pokédex Nacional (15 registros)... OK.")
print("Validando registros de medallas... OK.")

while True:
    print("MENÚ PRINCIPAL")
    print("1. Ver Equipo Principal")
    print("2. Ver Almacenamiento (PC)")
    print("3. Ver Medallas")
    print("4. Capturar Pokémon")
    print("5. Desafiar Líder de Gimnasio")
    print("6. Ordenar PC")
    print("7. Transferencias (Profesor Oak)")
    print("8. Ir al Centro Pokémon")
    print("9. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        mostrar_equipo()

    elif opcion == "2":
        mostrar_pc()

    elif opcion == "3":
        medallas_entrenador.mostrar()

    elif opcion == "4":
        print("xd")

    elif opcion == "5":
        elegir_gimnasio()

    elif opcion == "6":
        menu_organizacion()

    elif opcion == "7":
        print("1. Transferir Pokémon")
        print("2. Deshacer última transferencia")
        print("3. Ver transferencias")
        sub_opcion = input("Elegí una opción: ")
        if sub_opcion == "1":
            print("FALTA")
        elif sub_opcion == "2":
            deshacer_transferencia()
        elif sub_opcion == "3":
            mostrar_transferencias()
        else:
            print("Opción inválida.")

    elif opcion == "8":
        sanar_equipo(equipo_principal)

    elif opcion == "9":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción inválida, probá de nuevo.")   