class ForoVirtual:
    def __init__(self,
                 identificador=0,
                 nombre="",
                 detalle="",
                 creado_en="",
                 inicio="",
                 cierre="",
                 estado_actual="",
                 tema="",
                 mensajes_totales=0,
                 participantes_totales=0,
                 curso_id=0,
                 docente_id=0):

        self.identificador = identificador
        self.nombre = nombre
        self.detalle = detalle
        self.creado_en = creado_en
        self.inicio = inicio
        self.cierre = cierre
        self.estado_actual = estado_actual
        self.tema = tema
        self.mensajes_totales = mensajes_totales
        self.participantes_totales = participantes_totales
        self.curso_id = curso_id
        self.docente_id = docente_id

        print("Objeto foro inicializado con parámetros")
