from pathlib import Path

from json_manager import JSONManager
from models import Estudiante
from views import Vista
from herramientas import titulo


class SistemaEstudiantes:
    def __init__(self):
        carpeta_proyecto = Path(__file__).resolve().parent.parent
        ruta_json = carpeta_proyecto / "data" / "estudiantes.json"

        self.json_manager = JSONManager(ruta_json)
        self.vista = Vista(self)



    def crear(self, datos):
        registros = self.json_manager.leer()

        email = datos["email"].strip().lower()
        carnet = datos["carnet"].strip().lower()

        if any(r["email"].strip().lower() == email for r in registros):
            return False, "Ese email ya está registrado."

        if any(r["carnet"].strip().lower() == carnet for r in registros):
            return False, "Ese carnet ya está registrado."

        nuevo_id = max((r["id"] for r in registros), default=0) + 1

        estudiante = Estudiante(
            nuevo_id,
            datos["nombre"].strip(),
            datos["apellido"].strip(),
            datos["email"].strip(),
            datos["carnet"].strip(),
        )

        registros.append(estudiante.to_dict())

        if self.json_manager.guardar(registros):
            return True, f"Estudiante creado con ID {nuevo_id}."

        return False, "No se pudo guardar el estudiante."

    def listar(self):
        return [
            Estudiante.from_dict(r)
            for r in self.json_manager.leer()
        ]

    def buscar(self, termino):
        termino = termino.strip().lower()
        encontrados = []

        for estudiante in self.listar():
            valores = (
                estudiante.nombre,
                estudiante.apellido,
                estudiante.email,
                estudiante.carnet,
            )

            if any(termino in str(v).lower() for v in valores):
                encontrados.append(estudiante)

        return encontrados

    def obtener_por_id(self, id_estudiante):
        for estudiante in self.listar():
            if estudiante.id == id_estudiante:
                return estudiante
        return None

    def actualizar(self, id_estudiante, cambios):
        registros = self.json_manager.leer()

        posicion = None
        for i, registro in enumerate(registros):
            if registro["id"] == id_estudiante:
                posicion = i
                break

        if posicion is None:
            return False, "No existe ese estudiante."

        if "email" in cambios:
            email = cambios["email"].strip().lower()
            if any(
                r["id"] != id_estudiante
                and r["email"].strip().lower() == email
                for r in registros
            ):
                return False, "Ese email ya pertenece a otro estudiante."

        if "carnet" in cambios:
            carnet = cambios["carnet"].strip().lower()
            if any(
                r["id"] != id_estudiante
                and r["carnet"].strip().lower() == carnet
                for r in registros
            ):
                return False, "Ese carnet ya pertenece a otro estudiante."

        for campo, valor in cambios.items():
            registros[posicion][campo] = valor.strip()

        if self.json_manager.guardar(registros):
            return True, "Estudiante actualizado."

        return False, "No se pudo guardar la actualización."

    def eliminar(self, id_estudiante):
        registros = self.json_manager.leer()
        nuevos = [
            r for r in registros
            if r["id"] != id_estudiante
        ]

        if len(nuevos) == len(registros):
            return False, "No existe ese estudiante."

        if self.json_manager.guardar(nuevos):
            return True, "Estudiante eliminado."

        return False, "No se pudo eliminar."



    def agregar_nota(self, id_estudiante, materia, nota):
        try:
            nota = float(nota)
        except ValueError:
            return False, "La nota debe ser numérica."

        if not 0 <= nota <= 20:
            return False, "La nota debe estar entre 0 y 20."

        registros = self.json_manager.leer()

        for i, registro in enumerate(registros):
            if registro["id"] == id_estudiante:
                estudiante = Estudiante.from_dict(registro)
                estudiante.agregar_nota(materia, nota)
                registros[i] = estudiante.to_dict()

                if self.json_manager.guardar(registros):
                    return True, "Nota agregada correctamente."

                return False, "No se pudo guardar la nota."

        return False, "No existe ese estudiante."

    def materias_ofertadas(self):
        materias = set()

        for estudiante in self.listar():
            materias.update(estudiante.materias)

        return materias

    def materias_en_comun(self, id_a, id_b):
        a = self.obtener_por_id(id_a)
        b = self.obtener_por_id(id_b)

        if a is None or b is None:
            return None

        return a.materias_en_comun(b)

    def ejecutar(self):
        titulo("SISTEMA DE GESTIÓN DE ESTUDIANTES")
        self.vista.menu()


if __name__ == "__main__":
    SistemaEstudiantes().ejecutar()
