from datetime import datetime

from Archivos import cargar_datos, guardar_datos
from estudiante import buscar_estudiante
from equipos import buscar_equipo, actualizar_estado_equipo


ARCHIVO_PRESTAMOS = "prestamos.json"


def registrar_prestamo():
    prestamos = cargar_datos(ARCHIVO_PRESTAMOS)

    print("\n--- REGISTRAR PRÉSTAMO ---")

    documento = input("Documento del estudiante: ").strip()

    
    estudiante = buscar_estudiante(documento)

    if estudiante is None:
        print("El estudiante no está registrado.")
        return

    codigo_equipo = input("Código del equipo: ").strip()

    
    equipo = buscar_equipo(codigo_equipo)

    if equipo is None:
        print("El equipo no está registrado.")
        return

    
    if equipo["estado"].lower() != "disponible":
        print("El equipo no está disponible.")
        return

    
    prestamo = {
        "id": generar_id_prestamo(prestamos),
        "documento_estudiante": documento,
        "codigo_equipo": codigo_equipo,
        "fecha_prestamo": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "fecha_devolucion": None,
        "estado": "Activo"
    }

    prestamos.append(prestamo)

    
    actualizar_estado_equipo(codigo_equipo, "Prestado")

    guardar_datos(ARCHIVO_PRESTAMOS, prestamos)

    print("Préstamo registrado correctamente.")
    print(f"ID del préstamo: {prestamo['id']}")

    def registrar_devolucion():
    prestamos = cargar_datos(ARCHIVO_PRESTAMOS)

    print("\n--- REGISTRAR DEVOLUCIÓN ---")

    try:
        id_prestamo = int(input("ID del préstamo: ").strip())
    except ValueError:
        print("El ID debe ser un número.")
        return

    prestamo_encontrado = None

    for prestamo in prestamos:
        if prestamo["id"] == id_prestamo:
            prestamo_encontrado = prestamo
            break

    
    if prestamo_encontrado is None:
        print("No existe un préstamo con ese ID.")
        return

    
    if prestamo_encontrado["estado"] != "Activo":
        print("Este préstamo ya fue devuelto.")
        return

    codigo_equipo = prestamo_encontrado["codigo_equipo"]

    
    prestamo_encontrado["estado"] = "Devuelto"
    prestamo_encontrado["fecha_devolucion"] = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    
    actualizar_estado_equipo(codigo_equipo, "Disponible")

    guardar_datos(ARCHIVO_PRESTAMOS, prestamos)

    print("Devolución registrada correctamente.")
    print(f"Equipo {codigo_equipo} ahora está disponible.")

    def generar_id_prestamo(prestamos):
    if not prestamos:
        return 1

    ids = [prestamo["id"] for prestamo in prestamos]

    return max(ids) + 1


