import json
from pathlib import Path


class JSONManager:
    def __init__(self, ruta):
        self.ruta = Path(ruta)
        self.ruta.parent.mkdir(parents=True, exist_ok=True)

    def leer(self):
        if not self.ruta.exists():
            return []

        try:
            with self.ruta.open("r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
                return datos if isinstance(datos, list) else []
        except (json.JSONDecodeError, OSError):
            return []

    def guardar(self, datos):
        try:
            with self.ruta.open("w", encoding="utf-8") as archivo:
                json.dump(
                    datos,
                    archivo,
                    ensure_ascii=False,
                    indent=4
                )
            return True
        except OSError:
            return False
