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

def buscar_equipo(codigo):
    equipos = cargar_datos(ARCHIVO_EQUIPOS)

    for equipo in equipos:
        if equipo["codigo"].lower() == codigo.lower():
            return equipo

    return None


def actualizar_estado_equipo(codigo, nuevo_estado):
    equipos = cargar_datos(ARCHIVO_EQUIPOS)

    for equipo in equipos:
        if equipo["codigo"].lower() == codigo.lower():
            equipo["estado"] = nuevo_estado
            guardar_datos(ARCHIVO_EQUIPOS, equipos)
            return True

    return False

def listar_equipos():
    equipos = cargar_datos(ARCHIVO_EQUIPOS)

    print("\n--- LISTA DE EQUIPOS ---")

    if not equipos:
        print("No hay equipos registrados.")
        return

    for equipo in equipos:
        print(
            f"Código: {equipo['codigo']} | "
            f"Tipo: {equipo['tipo']} | "
            f"Marca: {equipo['marca']} | "
            f"Modelo: {equipo['modelo']} | "
            f"Estado: {equipo['estado']}"
        )
