import sqlite3
import os
from scr.entidad import Pregunta


class PreguntaDAO:
    def __init__(self, ruta_db="database/preguntas.db"):
        carpeta = os.path.dirname(ruta_db)
        if carpeta and not os.path.exists(carpeta):
            os.makedirs(carpeta, exist_ok=True)
        self.ruta_db = ruta_db
        self.crear_tabla()

    def _conectar(self):
        conexion = sqlite3.connect(self.ruta_db)
        conexion.row_factory = sqlite3.Row
        return conexion

    def crear_tabla(self):
        """Crea la tabla 'preguntas' si no existe."""
        sql = """
        CREATE TABLE IF NOT EXISTS preguntas (
            id INTEGER PRIMARY KEY,
            pregunta TEXT NOT NULL,
            opcion_a TEXT NOT NULL,
            opcion_b TEXT NOT NULL,
            opcion_c TEXT NOT NULL,
            opcion_d TEXT NOT NULL,
            respuesta_correcta TEXT NOT NULL,
            dificultad TEXT NOT NULL,
            tema TEXT NOT NULL
        );
        """
        with self._conectar() as conexion:
            conexion.execute(sql)

    def insertar(self, pregunta: Pregunta):
        """Inserta una pregunta (o la reemplaza si el id ya existe)."""
        sql = """
        INSERT OR REPLACE INTO preguntas
            (id, pregunta, opcion_a, opcion_b, opcion_c, opcion_d,
             respuesta_correcta, dificultad, tema)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        with self._conectar() as conexion:
            conexion.execute(sql, (
                pregunta.id, pregunta.pregunta, pregunta.opcion_a,
                pregunta.opcion_b, pregunta.opcion_c, pregunta.opcion_d,
                pregunta.respuesta_correcta, pregunta.dificultad, pregunta.tema
            ))

    def insertar_muchas(self, preguntas):
        """Inserta una lista de preguntas en una sola transacción."""
        sql = """
        INSERT OR REPLACE INTO preguntas
            (id, pregunta, opcion_a, opcion_b, opcion_c, opcion_d,
             respuesta_correcta, dificultad, tema)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        datos = [
            (p.id, p.pregunta, p.opcion_a, p.opcion_b, p.opcion_c, p.opcion_d,
             p.respuesta_correcta, p.dificultad, p.tema)
            for p in preguntas
        ]
        with self._conectar() as conexion:
            conexion.executemany(sql, datos)
        return len(datos)

    def _fila_a_pregunta(self, fila):
        return Pregunta(
            id=fila["id"], pregunta=fila["pregunta"],
            opcion_a=fila["opcion_a"], opcion_b=fila["opcion_b"],
            opcion_c=fila["opcion_c"], opcion_d=fila["opcion_d"],
            respuesta_correcta=fila["respuesta_correcta"],
            dificultad=fila["dificultad"], tema=fila["tema"]
        )

    def obtener_todas(self):
        """Devuelve una lista con todas las preguntas almacenadas."""
        with self._conectar() as conexion:
            filas = conexion.execute("SELECT * FROM preguntas ORDER BY id").fetchall()
        return [self._fila_a_pregunta(f) for f in filas]

    def obtener_por_id(self, id):
        """Devuelve una pregunta por su id, o None si no existe."""
        with self._conectar() as conexion:
            fila = conexion.execute(
                "SELECT * FROM preguntas WHERE id = ?", (id,)
            ).fetchone()
        return self._fila_a_pregunta(fila) if fila else None

    def obtener_por_tema(self, tema):
        """Devuelve todas las preguntas de un tema dado."""
        with self._conectar() as conexion:
            filas = conexion.execute(
                "SELECT * FROM preguntas WHERE tema = ? ORDER BY id", (tema,)
            ).fetchall()
        return [self._fila_a_pregunta(f) for f in filas]

    def obtener_por_dificultad(self, dificultad):
        """Devuelve todas las preguntas de una dificultad dada."""
        with self._conectar() as conexion:
            filas = conexion.execute(
                "SELECT * FROM preguntas WHERE dificultad = ? ORDER BY id",
                (dificultad,)
            ).fetchall()
        return [self._fila_a_pregunta(f) for f in filas]

    def actualizar(self, pregunta: Pregunta):
        """Actualiza una pregunta existente. Devuelve True si se modificó algo."""
        sql = """
        UPDATE preguntas SET
            pregunta = ?, opcion_a = ?, opcion_b = ?, opcion_c = ?, opcion_d = ?,
            respuesta_correcta = ?, dificultad = ?, tema = ?
        WHERE id = ?
        """
        with self._conectar() as conexion:
            cursor = conexion.execute(sql, (
                pregunta.pregunta, pregunta.opcion_a, pregunta.opcion_b,
                pregunta.opcion_c, pregunta.opcion_d, pregunta.respuesta_correcta,
                pregunta.dificultad, pregunta.tema, pregunta.id
            ))
        return cursor.rowcount > 0

    def eliminar(self, id):
        """Elimina una pregunta por id. Devuelve True si se eliminó algo."""
        with self._conectar() as conexion:
            cursor = conexion.execute("DELETE FROM preguntas WHERE id = ?", (id,))
        return cursor.rowcount > 0

    def contar_preguntas(self):
        """Devuelve el número total de preguntas almacenadas."""
        with self._conectar() as conexion:
            fila = conexion.execute("SELECT COUNT(*) as total FROM preguntas").fetchone()
        return fila["total"]

    def estadisticas_por_tema(self):
        """Devuelve un diccionario {tema: cantidad_de_preguntas}."""
        with self._conectar() as conexion:
            filas = conexion.execute(
                "SELECT tema, COUNT(*) as total FROM preguntas GROUP BY tema ORDER BY total DESC"
            ).fetchall()
        return {f["tema"]: f["total"] for f in filas}

    def estadisticas_por_dificultad(self):
        """Devuelve un diccionario {dificultad: cantidad_de_preguntas}."""
        with self._conectar() as conexion:
            filas = conexion.execute(
                "SELECT dificultad, COUNT(*) as total FROM preguntas GROUP BY dificultad"
            ).fetchall()
        return {f["dificultad"]: f["total"] for f in filas}
