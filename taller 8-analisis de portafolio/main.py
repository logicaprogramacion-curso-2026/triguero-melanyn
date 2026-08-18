from foro_virtual import ForoVirtual
from base_datos import BaseDeDatos
from foro_dao import ForoDAO

# Crear conexión con la base de datos
bd_local = BaseDeDatos()
foro_dao = ForoDAO(bd_local)

# Crear la tabla si no existe
foro_dao.crear_tabla()

# Crear un objeto foro con datos de ejemplo
foro_1 = ForoVirtual(
    identificador=1,
    nombre="Comienzo del proyecto",
    detalle="Este proyecto generará bastante esfuerzo, pero al final será provechoso",
    creado_en="21/07/26",
    inicio="21/07/26",
    cierre="21/07/26",
    estado_actual="Activo",
    tema="El proyecto",
    mensajes_totales=1,
    participantes_totales=1,
    curso_id=1,
    docente_id=1
)

# Insertar el foro en la base de datos
foro_dao.insertar(foro_1)

# Cerrar la conexión
bd_local.cerrar_conexion()
