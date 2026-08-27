from Archivos import inicializar_archivos

from equipos import registrar_equipo, listar_equipos
from estudiante import registrar_estudiante, listar_estudiantes
from prestamos import (
    registrar_prestamo,
    registrar_devolucion,
    listar_prestamos
)


def mostrar_menu():
    print("\n" + "=" * 45)
    print("     SISTEMA DE PRÉSTAMO DE EQUIPOS")
    print("=" * 45)

    print("1. Registrar equipo")
    print("2. Listar equipos")
    print("3. Registrar estudiante")
    print("4. Listar estudiantes")
    print("5. Registrar préstamo")
    print("6. Registrar devolución")
    print("7. Listar préstamos")
    print("0. Salir")

    print("=" * 45)


def main():
   
    inicializar_archivos()

    while True:
        mostrar_menu()

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_equipo()

        elif opcion == "2":
            listar_equipos()

        elif opcion == "3":
            registrar_estudiante()

        elif opcion == "4":
            listar_estudiantes()

        elif opcion == "5":
            registrar_prestamo()

        elif opcion == "6":
            registrar_devolucion()

        elif opcion == "7":
            listar_prestamos()

        elif opcion == "0":
            print("\n¡Gracias por utilizar el sistema!")
            break

        else:
            print("Opción no válida.")

        input("\nPresione ENTER para continuar...")


if __name__ == "__main__":
    main()