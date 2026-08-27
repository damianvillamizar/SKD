from Archivos import cargar_datos, guardar_datos


ARCHIVO_EQUIPOS = "equipos.json"


def registrar_equipo():
    equipos = cargar_datos(ARCHIVO_EQUIPOS)

    print("\n--- REGISTRAR EQUIPO ---")

    codigo = input("Código del equipo: ").strip()

    # Validar que el código no exista
    for equipo in equipos:
        if equipo["codigo"].lower() == codigo.lower():
            print("Ya existe un equipo con ese código.")
            return

    tipo = input("Tipo de equipo: ").strip()
    marca = input("Marca: ").strip()
    modelo = input("Modelo: ").strip()

    equipo = {
        "codigo": codigo,
        "tipo": tipo,
        "marca": marca,
        "modelo": modelo,
        "estado": "Disponible"
    }

    equipos.append(equipo)
    guardar_datos(ARCHIVO_EQUIPOS, equipos)

    print("Equipo registrado correctamente.")

