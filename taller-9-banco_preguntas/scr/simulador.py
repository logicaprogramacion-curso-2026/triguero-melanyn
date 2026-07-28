import random
import csv
import json
from datetime import datetime


class Simulador:
    """Simula una evaluación de selección múltiple sobre un banco de preguntas."""

    def __init__(self, dao):
        self.dao = dao
        self.resultados = []       # Lista de dicts con el detalle de cada respuesta
        self.puntaje = 0
        self.total_preguntas = 0
        self.fecha_hora = None

    def iniciar_simulacion(self, cantidad, tema=None, dificultad=None):
        """Selecciona 'cantidad' preguntas al azar (filtrando opcionalmente
        por tema y/o dificultad) y ejecuta la evaluación interactiva.
        """
        if tema:
            banco = self.dao.obtener_por_tema(tema)
        elif dificultad:
            banco = self.dao.obtener_por_dificultad(dificultad)
        else:
            banco = self.dao.obtener_todas()

        if not banco:
            print("No hay preguntas disponibles con esos criterios.")
            return

        cantidad = min(cantidad, len(banco))
        seleccionadas = random.sample(banco, cantidad)

        self.resultados = []
        self.puntaje = 0
        self.total_preguntas = cantidad
        self.fecha_hora = datetime.now()

        print(f"\n{'='*60}")
        print(f"  INICIANDO SIMULACIÓN - {cantidad} preguntas")
        print(f"{'='*60}\n")

        for i, pregunta in enumerate(seleccionadas, start=1):
            respuesta_usuario = self.mostrar_pregunta(pregunta, i, cantidad)
            correcta = self.validar_respuesta(pregunta, respuesta_usuario)
            if correcta:
                self.puntaje += 1
            self.resultados.append({
                "id": pregunta.id,
                "pregunta": pregunta.pregunta,
                "tema": pregunta.tema,
                "dificultad": pregunta.dificultad,
                "respuesta_usuario": respuesta_usuario,
                "respuesta_correcta": pregunta.respuesta_correcta,
                "es_correcta": correcta,
            })

        self.generar_reporte()

    def mostrar_pregunta(self, pregunta, numero=1, total=1):
        """Muestra una pregunta en pantalla y solicita la respuesta del usuario."""
        print(f"Pregunta {numero}/{total} — Tema: {pregunta.tema} ({pregunta.dificultad})")
        print(pregunta.pregunta)
        print(f"  A) {pregunta.opcion_a}")
        print(f"  B) {pregunta.opcion_b}")
        print(f"  C) {pregunta.opcion_c}")
        print(f"  D) {pregunta.opcion_d}")

        respuesta = input("Tu respuesta (A/B/C/D): ").strip().upper()
        while respuesta not in ("A", "B", "C", "D"):
            respuesta = input("Respuesta inválida. Ingresa A, B, C o D: ").strip().upper()
        print()
        return respuesta

    def validar_respuesta(self, pregunta, respuesta_usuario):
        """Valida si la respuesta del usuario coincide con la correcta."""
        return pregunta.es_correcta(respuesta_usuario)

    def generar_reporte(self):
        """Imprime en pantalla un resumen del resultado de la simulación."""
        porcentaje = (self.puntaje / self.total_preguntas * 100) if self.total_preguntas else 0
        print(f"{'='*60}")
        print("  RESULTADOS DE LA SIMULACIÓN")
        print(f"{'='*60}")
        print(f"Puntaje: {self.puntaje}/{self.total_preguntas} ({porcentaje:.1f}%)")
        print(f"{'='*60}\n")
        return {
            "puntaje": self.puntaje,
            "total": self.total_preguntas,
            "porcentaje": porcentaje,
            "resultados": self.resultados,
        }

    # ---------------------------------------------------------------
    # GUARDADO DE RESULTADOS EN ARCHIVOS
    # ---------------------------------------------------------------
    def _estadisticas_por_tema(self):
        stats = {}
        for r in self.resultados:
            tema = r["tema"]
            stats.setdefault(tema, {"total": 0, "correctas": 0})
            stats[tema]["total"] += 1
            if r["es_correcta"]:
                stats[tema]["correctas"] += 1
        return stats

    def _estadisticas_por_dificultad(self):
        stats = {}
        for r in self.resultados:
            dif = r["dificultad"]
            stats.setdefault(dif, {"total": 0, "correctas": 0})
            stats[dif]["total"] += 1
            if r["es_correcta"]:
                stats[dif]["correctas"] += 1
        return stats

    def guardar_respuestas_txt(self, ruta="resultados/respuestas_usuario.txt"):
        """Guarda el detalle de la simulación en un archivo TXT."""
        porcentaje = (self.puntaje / self.total_preguntas * 100) if self.total_preguntas else 0
        lineas = [
            "=" * 60,
            "  REPORTE DE SIMULACIÓN",
            "=" * 60,
            f"Fecha: {self.fecha_hora.strftime('%Y-%m-%d %H:%M:%S') if self.fecha_hora else '-'}",
            f"Puntaje: {self.puntaje}/{self.total_preguntas} ({porcentaje:.1f}%)",
            "-" * 60,
        ]
        for r in self.resultados:
            estado = "CORRECTA" if r["es_correcta"] else "INCORRECTA"
            lineas.append(f"[{r['id']}] {r['pregunta']}")
            lineas.append(f"  Tu respuesta: {r['respuesta_usuario']} | "
                          f"Correcta: {r['respuesta_correcta']} | {estado}")
        with open(ruta, "w", encoding="latin-1") as f:
            f.write("\n".join(lineas))

    def guardar_estadisticas_csv(self, ruta="resultados/estadisticas.csv"):
        """Guarda estadísticas por tema y dificultad en un archivo CSV."""
        with open(ruta, "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Categoria", "Nombre", "Total", "Correctas", "Porcentaje"])
            for tema, s in self._estadisticas_por_tema().items():
                pct = (s["correctas"] / s["total"] * 100) if s["total"] else 0
                writer.writerow(["Tema", tema, s["total"], s["correctas"], f"{pct:.1f}"])
            for dif, s in self._estadisticas_por_dificultad().items():
                pct = (s["correctas"] / s["total"] * 100) if s["total"] else 0
                writer.writerow(["Dificultad", dif, s["total"], s["correctas"], f"{pct:.1f}"])

    def guardar_reporte_json(self, ruta="resultados/reporte.json"):
        """Guarda el reporte completo de la simulación en formato JSON."""
        porcentaje = (self.puntaje / self.total_preguntas * 100) if self.total_preguntas else 0
        data = {
            "fecha": self.fecha_hora.strftime("%Y-%m-%d %H:%M:%S") if self.fecha_hora else None,
            "puntaje": self.puntaje,
            "total_preguntas": self.total_preguntas,
            "porcentaje": round(porcentaje, 1),
            "respuestas": self.resultados,
            "estadisticas_por_tema": self._estadisticas_por_tema(),
            "estadisticas_por_dificultad": self._estadisticas_por_dificultad(),
        }
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def guardar_todos_los_reportes(self):
        """Genera y guarda los tres formatos de reporte a la vez."""
        self.guardar_respuestas_txt()
        self.guardar_estadisticas_csv()
        self.guardar_reporte_json()