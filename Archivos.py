import json
import os


CARPETA_DATOS = "datos"


def inicializar_archivos():
    if not os.path.exists(CARPETA_DATOS):
        os.makedirs(CARPETA_DATOS)

    archivos = [
        "equipos.json",
        "estudiantes.json",
        "prestamos.json"
    ]

    for archivo in archivos:
        ruta = os.path.join(CARPETA_DATOS, archivo)

        if not os.path.exists(ruta):
            with open(ruta, "w", encoding="utf-8") as f:
                json.dump([], f, indent=4, ensure_ascii=False)


def cargar_datos(nombre_archivo):
    """Carga y devuelve los datos de un archivo JSON."""
    ruta = os.path.join(CARPETA_DATOS, nombre_archivo)

    try:
        with open(ruta, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def guardar_datos(nombre_archivo, datos):
    """Guarda los datos en un archivo JSON."""
    ruta = os.path.join(CARPETA_DATOS, nombre_archivo)

    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)