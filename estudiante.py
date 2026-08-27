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
