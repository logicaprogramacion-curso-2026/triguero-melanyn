class Pregunta:
    """Representa una pregunta de selección múltiple."""

    DIFICULTADES_VALIDAS = ("Fácil", "Media", "Difícil")
    RESPUESTAS_VALIDAS = ("A", "B", "C", "D")

    def __init__(self, id, pregunta, opcion_a, opcion_b, opcion_c, opcion_d,
                 respuesta_correcta, dificultad, tema):
        self.id = int(id)
        self.pregunta = str(pregunta).strip()
        self.opcion_a = str(opcion_a).strip()
        self.opcion_b = str(opcion_b).strip()
        self.opcion_c = str(opcion_c).strip()
        self.opcion_d = str(opcion_d).strip()
        self.respuesta_correcta = str(respuesta_correcta).strip().upper()
        self.dificultad = str(dificultad).strip()
        self.tema = str(tema).strip()
        self._validar()

    def _validar(self):
        """Valida que los datos de la pregunta sean consistentes."""
        if not self.pregunta:
            raise ValueError(f"La pregunta con id={self.id} no tiene enunciado.")
        if self.respuesta_correcta not in self.RESPUESTAS_VALIDAS:
            raise ValueError(
                f"Respuesta correcta inválida en id={self.id}: "
                f"'{self.respuesta_correcta}' (debe ser A, B, C o D)."
            )
        if not all([self.opcion_a, self.opcion_b, self.opcion_c, self.opcion_d]):
            raise ValueError(f"Faltan opciones en la pregunta id={self.id}.")

    def obtener_opcion_correcta(self):
        """Devuelve el texto de la opción marcada como correcta."""
        opciones = {
            "A": self.opcion_a,
            "B": self.opcion_b,
            "C": self.opcion_c,
            "D": self.opcion_d,
        }
        return opciones[self.respuesta_correcta]

    def es_correcta(self, respuesta_usuario):
        """Compara la respuesta del usuario (A/B/C/D) con la correcta."""
        if not respuesta_usuario:
            return False
        return str(respuesta_usuario).strip().upper() == self.respuesta_correcta

    def to_dict(self):
        """Convierte la pregunta a un diccionario (útil para JSON/CSV)."""
        return {
            "id": self.id,
            "pregunta": self.pregunta,
            "opcion_a": self.opcion_a,
            "opcion_b": self.opcion_b,
            "opcion_c": self.opcion_c,
            "opcion_d": self.opcion_d,
            "respuesta_correcta": self.respuesta_correcta,
            "dificultad": self.dificultad,
            "tema": self.tema,
        }

    @classmethod
    def from_dict(cls, data):
        """Crea una Pregunta a partir de un diccionario."""
        return cls(
            id=data["id"],
            pregunta=data["pregunta"],
            opcion_a=data["opcion_a"],
            opcion_b=data["opcion_b"],
            opcion_c=data["opcion_c"],
            opcion_d=data["opcion_d"],
            respuesta_correcta=data["respuesta_correcta"],
            dificultad=data["dificultad"],
            tema=data["tema"],
        )

    def __str__(self):
        return (
            f"[{self.id}] ({self.tema} - {self.dificultad}) {self.pregunta}\n"
            f" A) {self.opcion_a}\n"
            f" B) {self.opcion_b}\n"
            f" C) {self.opcion_c}\n"
            f" D) {self.opcion_d}\n"
            f" Respuesta correcta: {self.respuesta_correcta}"
        )

    def __repr__(self):
        return f"Pregunta(id={self.id}, tema='{self.tema}', dificultad='{self.dificultad}')"

    def __eq__(self, other):
        if not isinstance(other, Pregunta):
            return False
        return self.id == other.id
