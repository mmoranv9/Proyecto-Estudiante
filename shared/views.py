from herramientas import (
    titulo,
    exito,
    error,
    info,
    pausa,
    confirmar,
    email_valido,
    practicar_colecciones,
)


class Vista:
    def __init__(self, sistema):
        self.sistema = sistema

    def menu(self):
        while True:
            titulo("MENÚ PRINCIPAL")

            print("1. Crear estudiante")
            print("2. Ver todos")
            print("3. Buscar")
            print("4. Ver por ID")
            print("5. Actualizar")
            print("6. Eliminar")
            print("7. Agregar nota")
            print("8. Ver promedio")
            print("9. Ver materias ofertadas")
            print("10. Materias en común")
            print("11. Práctica de colecciones")
            print("0. Salir")

            opcion = input("\nSeleccione una opción: ").strip()

            if opcion == "1":
                self.crear()
            elif opcion == "2":
                self.listar()
            elif opcion == "3":
                self.buscar()
            elif opcion == "4":
                self.ver_por_id()
            elif opcion == "5":
                self.actualizar()
            elif opcion == "6":
                self.eliminar()
            elif opcion == "7":
                self.agregar_nota()
            elif opcion == "8":
                self.promedio()
            elif opcion == "9":
                self.materias()
            elif opcion == "10":
                self.comunes()
            elif opcion == "11":
                practicar_colecciones()
                pausa()
            elif opcion == "0":
                print("\nPrograma finalizado.")
                break
            else:
                error("Opción no válida.")
                pausa()

    def crear(self):
        titulo("CREAR ESTUDIANTE")

        datos = {
            "nombre": input("Nombre: ").strip(),
            "apellido": input("Apellido: ").strip(),
            "email": input("Email: ").strip(),
            "carnet": input("Carnet: ").strip(),
        }

        if not all(datos.values()):
            error("Todos los campos son obligatorios.")
            pausa()
            return

        if not email_valido(datos["email"]):
            error("El email no es válido.")
            pausa()
            return

        ok, mensaje = self.sistema.crear(datos)

        exito(mensaje) if ok else error(mensaje)
        pausa()

    def listar(self):
        titulo("LISTA DE ESTUDIANTES")

        estudiantes = self.sistema.listar()

        if not estudiantes:
            info("No hay estudiantes registrados.")
        else:
            for e in estudiantes:
                print(
                    f"ID: {e.id} | "
                    f"{e.nombre_completo()} | "
                    f"{e.email} | "
                    f"Carnet: {e.carnet} | "
                    f"Promedio: {e.promedio()}"
                )

        pausa()

    def buscar(self):
        titulo("BUSCAR")

        termino = input(
            "Ingrese nombre, apellido, email o carnet: "
        )

        encontrados = self.sistema.buscar(termino)

        if not encontrados:
            info("No se encontraron resultados.")
        else:
            for e in encontrados:
                print(e)

        pausa()

    def ver_por_id(self):
        titulo("VER POR ID")

        try:
            id_estudiante = int(input("ID: "))
        except ValueError:
            error("El ID debe ser un número.")
            pausa()
            return

        estudiante = self.sistema.obtener_por_id(id_estudiante)

        if estudiante is None:
            error("No existe ese estudiante.")
        else:
            print("ID:", estudiante.id)
            print("Nombre:", estudiante.nombre)
            print("Apellido:", estudiante.apellido)
            print("Email:", estudiante.email)
            print("Carnet:", estudiante.carnet)
            print("Notas:", estudiante.notas)
            print("Materias:", sorted(estudiante.materias))
            print("Promedio:", estudiante.promedio())

        pausa()

    def actualizar(self):
        titulo("ACTUALIZAR")

        try:
            id_estudiante = int(input("ID: "))
        except ValueError:
            error("El ID debe ser un número.")
            pausa()
            return

        estudiante = self.sistema.obtener_por_id(id_estudiante)

        if estudiante is None:
            error("No existe ese estudiante.")
            pausa()
            return

        print("Deje vacío un campo si no desea cambiarlo.")

        cambios = {}

        for campo in ("nombre", "apellido", "email", "carnet"):
            actual = getattr(estudiante, campo)
            nuevo = input(
                f"{campo.capitalize()} [{actual}]: "
            ).strip()

            if nuevo:
                cambios[campo] = nuevo

        if not cambios:
            info("No se realizaron cambios.")
            pausa()
            return

        if "email" in cambios and not email_valido(cambios["email"]):
            error("El nuevo email no es válido.")
            pausa()
            return

        ok, mensaje = self.sistema.actualizar(
            id_estudiante,
            cambios
        )

        exito(mensaje) if ok else error(mensaje)
        pausa()

    def eliminar(self):
        titulo("ELIMINAR")

        try:
            id_estudiante = int(input("ID: "))
        except ValueError:
            error("El ID debe ser un número.")
            pausa()
            return

        estudiante = self.sistema.obtener_por_id(id_estudiante)

        if estudiante is None:
            error("No existe ese estudiante.")
            pausa()
            return

        print("Se eliminará:", estudiante)

        if confirmar("¿Desea continuar?"):
            ok, mensaje = self.sistema.eliminar(id_estudiante)
            exito(mensaje) if ok else error(mensaje)
        else:
            info("Operación cancelada.")

        pausa()

    def agregar_nota(self):
        titulo("AGREGAR NOTA")

        try:
            id_estudiante = int(input("ID: "))
        except ValueError:
            error("El ID debe ser un número.")
            pausa()
            return

        materia = input("Materia: ").strip()
        nota = input("Nota (0-20): ").strip()

        ok, mensaje = self.sistema.agregar_nota(
            id_estudiante,
            materia,
            nota
        )

        exito(mensaje) if ok else error(mensaje)
        pausa()

    def promedio(self):
        titulo("PROMEDIO")

        try:
            id_estudiante = int(input("ID: "))
        except ValueError:
            error("El ID debe ser un número.")
            pausa()
            return

        estudiante = self.sistema.obtener_por_id(id_estudiante)

        if estudiante is None:
            error("No existe ese estudiante.")
        else:
            exito(
                f"El promedio de {estudiante.nombre_completo()} "
                f"es {estudiante.promedio()}"
            )

        pausa()

    def materias(self):
        titulo("MATERIAS OFERTADAS")

        materias = self.sistema.materias_ofertadas()

        if not materias:
            info("No hay materias registradas.")
        else:
            for materia in sorted(materias):
                print("-", materia)

        pausa()

    def comunes(self):
        titulo("MATERIAS EN COMÚN")

        try:
            id_a = int(input("ID del primer estudiante: "))
            id_b = int(input("ID del segundo estudiante: "))
        except ValueError:
            error("Los IDs deben ser números.")
            pausa()
            return

        comunes = self.sistema.materias_en_comun(id_a, id_b)

        if comunes is None:
            error("Uno o ambos estudiantes no existen.")
        elif comunes:
            print("Materias en común:")
            for materia in sorted(comunes):
                print("-", materia)
        else:
            info("No tienen materias en común.")

        pausa()
