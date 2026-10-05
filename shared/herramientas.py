import os


def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")


def pausa():
    input("\nPresione Enter para continuar...")


def titulo(texto):
    print("\n" + "=" * 70)
    print(texto.center(70))
    print("=" * 70 + "\n")


def exito(mensaje):
    print(f"[OK] {mensaje}")


def error(mensaje):
    print(f"[ERROR] {mensaje}")


def info(mensaje):
    print(f"[INFO] {mensaje}")


def confirmar(pregunta):
    respuesta = input(f"{pregunta} (si/no): ").strip().lower()
    return respuesta in ("si", "sí", "s")


def email_valido(email):
    email = email.strip()

    if email.count("@") != 1:
        return False

    usuario, dominio = email.split("@")

    return (
        bool(usuario)
        and "." in dominio
        and not dominio.endswith(".")
    )


def practicar_colecciones():
    """
    Ejemplos básicos de list, tuple, set y dict.
    """

    print("\n--- LISTA ---")
    clientes = ["Ana", "Luis", "Sol"]
    clientes.append("Marco")
    clientes.insert(1, "Beto")
    clientes.extend(["Iván", "Ruth"])
    clientes.remove("Beto")

    print("Clientes:", clientes)
    print("Cantidad:", len(clientes))
    print("¿Ana está?:", "Ana" in clientes)

    print("\n--- TUPLA ---")
    campos = ("nombre", "apellido", "email", "carnet")
    print("Campos:", campos)
    print("Primer campo:", campos[0])

    print("\n--- SET ---")
    ciudades = {"Quito", "Guayaquil", "Quito", "Cuenca"}
    print("Ciudades sin repetirse:", ciudades)

    print("\n--- DICCIONARIO ---")
    estudiante = {
        "nombre": "Ana",
        "apellido": "Torres",
        "email": "ana@example.com"
    }
    print("Estudiante:", estudiante)
    print("Nombre:", estudiante["nombre"])

    print("\n--- COMPREHENSIONS ---")
    numeros = [1, 2, 3, 4, 5]
    cuadrados = [n * n for n in numeros]
    pares = [n for n in numeros if n % 2 == 0]

    print("Cuadrados:", cuadrados)
    print("Pares:", pares)


COLORES = {
    "ROJO": "\033[91m",
    "VERDE": "\033[92m",
    "AZUL": "\033[94m",
    "AMARILLO": "\033[93m",
    "CYAN": "\033[96m",
    "BLANCO": "\033[97m",
    "RESET": "\033[0m",
}


RESPUESTAS_SI = ("si", "sí", "s", "yes", "y")


def limpiar_pantalla():
    os.system("clear" if os.name == "posix" else "cls")


def imprimir_color(texto, color):
    codigo = COLORES.get(color, COLORES["BLANCO"])   # .get evita el error si el color no existe
    print(f"{codigo}{texto}{COLORES['RESET']}")


def imprimir_titulo(texto):
    limpiar_pantalla()
    imprimir_color("=" * 60, "AZUL")
    print(f"  {texto}".center(60))
    imprimir_color("=" * 60, "AZUL")
    print()


def imprimir_exito(mensaje):
    imprimir_color(f"✓ {mensaje}", "VERDE")


def imprimir_error(mensaje):
    imprimir_color(f"✗ {mensaje}", "ROJO")


def imprimir_info(mensaje):
    imprimir_color(f"ℹ {mensaje}", "CYAN")


def confirmar(pregunta):
    respuesta = input(f"{pregunta} (si/no): ").strip().lower()
    return respuesta in RESPUESTAS_SI


def es_email_valido(texto):
    texto = texto.strip()
    if texto.count("@") != 1:
        return False
    usuario, dominio = texto.split("@")
    return len(usuario) > 0 and "." in dominio and not dominio.endswith(".")