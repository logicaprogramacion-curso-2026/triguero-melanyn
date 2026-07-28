import csv
import json
import re
import os

from scr.entidad import Pregunta
from scr.dao import PreguntaDAO


class GestorPreguntas:
    """Lógica de negocio para cargar, guardar y exportar preguntas."""

    def __init__(self, dao: PreguntaDAO = None):
        self.dao = dao if dao is not None else PreguntaDAO()


    # ---------------------------------------------------------------
    # BUSCAR RUTA CORRECTA
    # ---------------------------------------------------------------
    def obtener_ruta(self, ruta):
        """
        Busca el archivo en diferentes ubicaciones del proyecto
        para evitar errores cuando se ejecuta desde src.
        """

        rutas_posibles = [
            ruta,
            os.path.join("..", ruta),
            os.path.join("..", "..", ruta),
            os.path.join("taller9-banco_preguntas", ruta),
            os.path.join("..", "taller9-banco_preguntas", ruta)
        ]

        for r in rutas_posibles:
            if os.path.exists(r):
                return r

        return ruta


    # ---------------------------------------------------------------
    # CARGA DESDE ARCHIVOS
    # ---------------------------------------------------------------

    def cargar_desde_txt(self, ruta):
        """
        Carga preguntas desde un archivo TXT.
        """

        ruta = self.obtener_ruta(ruta)

        with open(ruta, "r", encoding="utf-8") as f:
            contenido = f.read()

        bloques = contenido.split("PREGUNTA #")
        preguntas = []

        for bloque in bloques[1:]:
            try:
                id_ = int(re.search(r"^\s*(\d+)", bloque).group(1))
                tema = re.search(r"Tema:\s*(.+)", bloque).group(1).strip()
                dificultad = re.search(r"Dificultad:\s*(.+)", bloque).group(1).strip()
                enunciado = re.search(r"Enunciado:\s*(.+)", bloque).group(1).strip()
                op_a = re.search(r"A\)\s*(.+)", bloque).group(1).strip()
                op_b = re.search(r"B\)\s*(.+)", bloque).group(1).strip()
                op_c = re.search(r"C\)\s*(.+)", bloque).group(1).strip()
                op_d = re.search(r"D\)\s*(.+)", bloque).group(1).strip()
                correcta = re.search(
                    r"Respuesta Correcta:\s*([ABCD])",
                    bloque
                ).group(1).strip()

            except AttributeError:
                continue

            preguntas.append(
                Pregunta(
                    id=id_,
                    pregunta=enunciado,
                    opcion_a=op_a,
                    opcion_b=op_b,
                    opcion_c=op_c,
                    opcion_d=op_d,
                    respuesta_correcta=correcta,
                    dificultad=dificultad,
                    tema=tema
                )
            )

        return preguntas



    def cargar_desde_csv(self, ruta):
        """
        Carga preguntas desde CSV.
        """

        ruta = self.obtener_ruta(ruta)

        preguntas = []

        with open(ruta, "r", encoding="utf-8", newline="") as f:

            reader = csv.DictReader(f)

            for fila in reader:

                preguntas.append(
                    Pregunta(
                        id=fila["ID"],
                        pregunta=fila["Pregunta"],
                        opcion_a=fila["OpcionA"],
                        opcion_b=fila["OpcionB"],
                        opcion_c=fila["OpcionC"],
                        opcion_d=fila["OpcionD"],
                        respuesta_correcta=fila["RespuestaCorrecta"],
                        dificultad=fila["Dificultad"],
                        tema=fila["Tema"]
                    )
                )

        return preguntas



    def cargar_desde_json(self, ruta):
        """
        Carga preguntas desde JSON.
        """

        ruta = self.obtener_ruta(ruta)

        with open(ruta, "r", encoding="utf-8") as f:
            data = json.load(f)

        lista = data["cuestionario"]["preguntas"]

        preguntas = []

        for item in lista:

            preguntas.append(
                Pregunta(
                    id=item["id"],
                    pregunta=item["pregunta"],
                    opcion_a=item["opciones"]["A"],
                    opcion_b=item["opciones"]["B"],
                    opcion_c=item["opciones"]["C"],
                    opcion_d=item["opciones"]["D"],
                    respuesta_correcta=item["respuesta_correcta"],
                    dificultad=item["dificultad"],
                    tema=item["tema"]
                )
            )

        return preguntas



    # ---------------------------------------------------------------
    # GUARDADO EN BASE DE DATOS
    # ---------------------------------------------------------------

    def guardar_en_base_datos(self, preguntas):
        return self.dao.insertar_muchas(preguntas)



    # ---------------------------------------------------------------
    # EXPORTACIÓN
    # ---------------------------------------------------------------

    def exportar_a_txt(self, ruta, preguntas=None):

        preguntas = preguntas if preguntas is not None else self.dao.obtener_todas()

        lineas = [
            "=" * 80,
            " BANCO DE PREGUNTAS EXPORTADO",
            "=" * 80,
            ""
        ]

        for p in preguntas:

            lineas.append(f"PREGUNTA #{p.id}")
            lineas.append("-" * 80)
            lineas.append(f"ID: {p.id}")
            lineas.append(f"Tema: {p.tema}")
            lineas.append(f"Dificultad: {p.dificultad}")
            lineas.append(f"Enunciado: {p.pregunta}")
            lineas.append("Opciones:")
            lineas.append(f"A) {p.opcion_a}")
            lineas.append(f"B) {p.opcion_b}")
            lineas.append(f"C) {p.opcion_c}")
            lineas.append(f"D) {p.opcion_d}")
            lineas.append(f"Respuesta Correcta: {p.respuesta_correcta}")
            lineas.append("-" * 80)
            lineas.append("")

        with open(ruta, "w", encoding="utf-8") as f:
            f.write("\n".join(lineas))

        return len(preguntas)



    def exportar_a_csv(self, ruta, preguntas=None):

        preguntas = preguntas if preguntas is not None else self.dao.obtener_todas()

        with open(ruta, "w", encoding="utf-8", newline="") as f:

            writer = csv.writer(f)

            writer.writerow([
                "ID",
                "Pregunta",
                "OpcionA",
                "OpcionB",
                "OpcionC",
                "OpcionD",
                "RespuestaCorrecta",
                "Dificultad",
                "Tema"
            ])

            for p in preguntas:

                writer.writerow([
                    p.id,
                    p.pregunta,
                    p.opcion_a,
                    p.opcion_b,
                    p.opcion_c,
                    p.opcion_d,
                    p.respuesta_correcta,
                    p.dificultad,
                    p.tema
                ])

        return len(preguntas)



    def exportar_a_json(self, ruta, preguntas=None):

        preguntas = preguntas if preguntas is not None else self.dao.obtener_todas()

        data = {
            "cuestionario": {
                "titulo": "Banco de preguntas exportado desde la base de datos",
                "total_preguntas": len(preguntas),
                "preguntas": []
            }
        }


        for p in preguntas:

            data["cuestionario"]["preguntas"].append(
                {
                    "id": p.id,
                    "pregunta": p.pregunta,
                    "opciones": {
                        "A": p.opcion_a,
                        "B": p.opcion_b,
                        "C": p.opcion_c,
                        "D": p.opcion_d
                    },
                    "respuesta_correcta": p.respuesta_correcta,
                    "dificultad": p.dificultad,
                    "tema": p.tema
                }
            )


        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        return len(preguntas)



    # ---------------------------------------------------------------
    # ESTADÍSTICAS
    # ---------------------------------------------------------------

    def estadisticas_por_tema(self):
        return self.dao.estadisticas_por_tema()


    def estadisticas_por_dificultad(self):
        return self.dao.estadisticas_por_dificultad()

