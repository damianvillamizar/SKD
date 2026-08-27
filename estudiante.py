from Archivos import cargar_datos, guardar_datos


ARCHIVO_ESTUDIANTES = "estudiantes.json"


def registrar_estudiante():
    estudiantes = cargar_datos(ARCHIVO_ESTUDIANTES)

    print("\n--- REGISTRAR ESTUDIANTE ---")

    documento = input("Documento: ").strip()

    
    for estudiante in estudiantes:
        if estudiante["documento"] == documento:
            print("Ya existe un estudiante con ese documento.")
            return

    nombre = input("Nombre completo: ").strip()
    correo = input("Correo: ").strip()
    programa = input("Programa académico: ").strip()

    estudiante = {
        "documento": documento,
        "nombre": nombre,
        "correo": correo,
        "programa": programa
    }

    estudiantes.append(estudiante)
    guardar_datos(ARCHIVO_ESTUDIANTES, estudiantes)

    print("Estudiante registrado correctamente.")


def buscar_estudiante(documento):
    estudiantes = cargar_datos(ARCHIVO_ESTUDIANTES)

    for estudiante in estudiantes:
        if estudiante["documento"] == documento:
            return estudiante

    return None


def listar_estudiantes():
    estudiantes = cargar_datos(ARCHIVO_ESTUDIANTES)

    print("\n--- LISTA DE ESTUDIANTES ---")

    if not estudiantes:
        print("No hay estudiantes registrados.")
        return

    for estudiante in estudiantes:
        print(
            f"Documento: {estudiante['documento']} | "
            f"Nombre: {estudiante['nombre']} | "
            f"Correo: {estudiante['correo']} | "
            f"Programa: {estudiante['programa']}"
        )