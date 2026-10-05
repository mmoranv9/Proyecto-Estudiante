class Estudiante:
    def __init__(
        self,
        id_estudiante,
        nombre,
        apellido,
        email,
        carnet,
        notas=None,
        materias=None,
    ):
        self.id = id_estudiante
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.carnet = carnet
        self.notas = notas if notas is not None else {}
        self.materias = set(materias) if materias is not None else set()

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    def agregar_nota(self, materia, nota):
        materia = materia.strip()
        self.materias.add(materia)
        self.notas.setdefault(materia, []).append(nota)

    def promedio(self):
        notas = []
        for lista in self.notas.values():
            notas.extend(lista)

        if not notas:
            return 0

        return round(sum(notas) / len(notas), 2)

    def materias_en_comun(self, otro):
        return self.materias & otro.materias

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "email": self.email,
            "carnet": self.carnet,
            "notas": self.notas,
            "materias": sorted(self.materias),
        }

    @classmethod
    def from_dict(cls, datos):
        return cls(
            datos["id"],
            datos["nombre"],
            datos["apellido"],
            datos["email"],
            datos["carnet"],
            datos.get("notas", {}),
            datos.get("materias", []),
        )

    def __str__(self):
        return (
            f"[{self.carnet}] {self.nombre_completo()} "
            f"- Promedio: {self.promedio()}"
        )
