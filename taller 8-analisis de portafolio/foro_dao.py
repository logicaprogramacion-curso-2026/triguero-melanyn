from foro_virtual import ForoVirtual

class ForoDAO:
    def __init__(self, base_datos):
        self.base_datos = base_datos
        
    def crear_tabla(self):
        self.base_datos.puntero.execute('''
            CREATE TABLE IF NOT EXISTS foro_virtual (
                identificador INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(150) NOT NULL,
                detalle TEXT,
                creado_en DATETIME NOT NULL,
                inicio DATETIME,
                cierre DATETIME,
                estado_actual TEXT NOT NULL CHECK (estado_actual IN ('Activo', 'Cerrado', 'Archivado')),
                tema VARCHAR(200),
                mensajes_totales INTEGER DEFAULT 0,
                participantes_totales INTEGER DEFAULT 0,
                curso_id INTEGER NOT NULL,
                docente_id INTEGER NOT NULL
            )
        ''')
    
    def insertar(self, foro_virtual):
        self.base_datos.puntero.execute('''
            INSERT INTO foro_virtual (nombre, detalle, creado_en, inicio, cierre, estado_actual, tema, mensajes_totales, participantes_totales, curso_id, docente_id)
            VALUES (?,?,?,?,?,?,?,?,?,?,?)
            ''', (foro_virtual.nombre, foro_virtual.detalle, foro_virtual.creado_en, foro_virtual.inicio, foro_virtual.cierre, foro_virtual.estado_actual, foro_virtual.tema, foro_virtual.mensajes_totales, foro_virtual.participantes_totales, foro_virtual.curso_id, foro_virtual.docente_id))
        self.base_datos.conexion.commit()
        return self.base_datos.puntero.lastrowid
