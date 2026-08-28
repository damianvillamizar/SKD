#  Sistema de Préstamo de Equipos

Sistema desarrollado en **Python** para gestionar el préstamo y devolución de equipos a estudiantes. El proyecto utiliza una estructura modular y archivos **JSON** para almacenar la información.

# Descripción

El sistema permite administrar equipos disponibles para préstamo, registrar estudiantes y controlar los préstamos y devoluciones.

El objetivo del proyecto es aplicar conceptos de **Scrum y metodologías ágiles**, desarrollando un incremento funcional utilizando Python.

# Tecnologías utilizadas

* **Python 3**
* **JSON** para almacenamiento de datos
* **Programación modular**
* Librerías estándar:

  * `json`
  * `os`
  * `datetime`

# Estructura del proyecto

```text
proyecto/
│
├── main.py
├── equipos.py
├── estudiantes.py
├── prestamos.py
├── archivos.py
│
└── datos/
    ├── equipos.json
    ├── estudiantes.json
    └── prestamos.json
```

# Descripción de los archivos

| Archivo            | Función                                                          |
| ------------------ | ---------------------------------------------------------------- |
| `main.py`          | Contiene el menú principal y controla la ejecución del programa. |
| `equipos.py`       | Permite registrar, listar y actualizar el estado de los equipos. |
| `estudiantes.py`   | Permite registrar y consultar estudiantes.                       |
| `prestamos.py`     | Gestiona los préstamos, devoluciones y validaciones.             |
| `archivos.py`      | Se encarga de leer y guardar información en los archivos JSON.   |
| `equipos.json`     | Almacena la información de los equipos.                          |
| `estudiantes.json` | Almacena la información de los estudiantes.                      |
| `prestamos.json`   | Almacena la información de los préstamos.                        |

# Funcionalidades

# 1. Registrar equipo

Permite registrar un equipo ingresando:

* Código
* Tipo
* Marca
* Modelo
* Estado

El estado inicial del equipo se establece automáticamente como **Disponible**.

# 2. Listar equipos

Muestra todos los equipos registrados junto con su información y disponibilidad.

Ejemplo:

```text
Código: CAM001 | Tipo: Cámara | Marca: Canon | Modelo: EOS R50 | Estado: Disponible
```

# 3. Registrar estudiante

Permite registrar:

* Documento
* Nombre
* Correo electrónico
* Programa académico

El sistema verifica que el documento no esté registrado previamente.

# 4. Registrar préstamo

Para realizar un préstamo, el sistema valida:

1. Que el estudiante esté registrado.
2. Que el equipo exista.
3. Que el equipo esté disponible.

Si todas las condiciones se cumplen, se registra el préstamo y el estado del equipo cambia automáticamente:

```text
Disponible → Prestado
```

Cada préstamo recibe un ID único y registra la fecha y hora del préstamo.

# 5. Registrar devolución

Permite registrar la devolución utilizando el ID del préstamo.

El sistema verifica que:

* El préstamo exista.
* El préstamo se encuentre activo.
* El equipo asociado sea actualizado.

Después de realizar la devolución:

```text
Prestado → Disponible
```

También se registra automáticamente la fecha y hora de devolución.

# 6. Listar préstamos

Permite consultar todos los préstamos registrados, mostrando:

* ID
* Documento del estudiante
* Código del equipo
* Fecha del préstamo
* Fecha de devolución
* Estado del préstamo

# Instalación y ejecución

# Requisitos

Tener instalado **Python 3** en el equipo.

Puedes comprobar la instalación ejecutando:

```bash
python --version
```

o:

```bash
python3 --version
```

# Ejecución

1. Descargar o clonar el repositorio.

2. Abrir una terminal dentro de la carpeta del proyecto.

3. Ejecutar:

```bash
python main.py
```

En caso de utilizar `python3`:

```bash
python3 main.py
```

# Uso del sistema

Al iniciar el programa aparecerá el siguiente menú:

```text
=============================================
     SISTEMA DE PRÉSTAMO DE EQUIPOS
=============================================
1. Registrar equipo
2. Listar equipos
3. Registrar estudiante
4. Listar estudiantes
5. Registrar préstamo
6. Registrar devolución
7. Listar préstamos
0. Salir
=============================================
Seleccione una opción:
```

El usuario puede seleccionar la operación que desea realizar ingresando el número correspondiente.

# Almacenamiento de datos

La información se almacena localmente en archivos `.json` dentro de la carpeta `datos/`.

Los archivos utilizados son:

```text
datos/
├── equipos.json
├── estudiantes.json
└── prestamos.json
```

El programa crea automáticamente la carpeta y los archivos si no existen.

# Validaciones

El sistema cuenta con diferentes validaciones para evitar errores:

* No permite registrar dos equipos con el mismo código.
* No permite registrar dos estudiantes con el mismo documento.
* No permite prestar un equipo que no exista.
* No permite prestar un equipo que ya esté prestado.
* No permite realizar un préstamo a un estudiante no registrado.
* No permite devolver un préstamo inexistente.
* No permite devolver un préstamo que ya fue cerrado.
* Valida que el ID del préstamo sea numérico.

# Requisitos funcionales cumplidos

| Requisito                            | Estado |
| ------------------------------------ | ------ |
| Registrar equipo                     | ✅      |
| Listar equipos                       | ✅      |
| Registrar estudiante                 | ✅      |
| Registrar préstamo                   | ✅      |
| Validar estudiante                   | ✅      |
| Validar equipo                       | ✅      |
| Validar disponibilidad               | ✅      |
| Registrar devolución                 | ✅      |
| Actualizar disponibilidad del equipo | ✅      |
| Almacenar información en JSON        | ✅      |

# Metodología

El proyecto se desarrolla siguiendo principios de **Scrum**, trabajando sobre un incremento funcional que permite gestionar el ciclo básico de préstamo de equipos.

# Incremento desarrollado

El incremento permite completar el flujo:

```text
Registrar estudiante
        ↓
Registrar equipo
        ↓
Solicitar préstamo
        ↓
Validar información
        ↓
Equipo prestado
        ↓
Registrar devolución
        ↓
Equipo disponible
```

Proyecto académico desarrollado para la aplicación de **Scrum y Metodologías Ágiles**.
