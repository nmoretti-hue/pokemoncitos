
import sys
import time
sys.path.append("extras")
from Búsquedas import menu_busquedas
from sistemadealmacenamientoPC import cargar_pokemones_desde_json,mostrar_equipo,mostrar_pc
from pokemoncito import equipo_principal,pokedex_hashmap
from desafioaliderdegimnasio import elegir_gimnasio, medallas_entrenador, precargar_medallas
from sanarequipo import sanar_equipo
from desahcertranferencia import transferir_a_oak, deshacer_transferencia, mostrar_transferencias, transferir_pokemon_de_pc
from OrganizacióndelAlmacenamiento import menu_organizacion
from CapturarPokemon import capturar_pokemon

print("   SISTEMA DE GESTIÓN: POKÉMON HUERGO   ")
print("Inicializando motor de base de datos... OK.")
print("Cargando Pokédex Nacional (15 registros)... OK.")
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
    print("9. Ver Pokedex")
    print("10. Buscar Pokémon")
    print("11. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        time.sleep(1)
        mostrar_equipo()
        time.sleep(1)

    elif opcion == "2":
        time.sleep(1)
        mostrar_pc()
        time.sleep(1)

    elif opcion == "3":
        time.sleep(1)
        medallas_entrenador.mostrar()
        time.sleep(1)

    elif opcion == "4":
        time.sleep(1)
        capturar_pokemon()
        time.sleep(1)

    elif opcion == "5":
        time.sleep(1)
        elegir_gimnasio()
        time.sleep(1)

    elif opcion == "6":
        time.sleep(1)
        menu_organizacion()
        time.sleep(1)

    elif opcion == "7":
        time.sleep(1)
        print("1. Transferir Pokémon")
        print("2. Deshacer última transferencia")
        print("3. Ver transferencias")
        sub_opcion = input("Elegí una opción: ")
        if sub_opcion == "1":
            transferir_pokemon_de_pc()
        elif sub_opcion == "2":
            deshacer_transferencia()
        elif sub_opcion == "3":
            mostrar_transferencias()
        else:
            print("Opción inválida.")

    elif opcion == "8":
        time.sleep(1)
        sanar_equipo(equipo_principal)
        time.sleep(1)
    elif opcion == "9":
        time.sleep(1)
        pokedex_hashmap.mostrar()
        time.sleep(1)
    elif opcion == "10":
        time.sleep(1)
        menu_busquedas()
        time.sleep(1)
    elif opcion == "11":
        print("Saliendo del sistema...")
        time.sleep(1)
        break
    else:
        print("Opción inválida, probá de nuevo.")
  