import sqlite3

class BaseDeDatos:
    def __init__(self, nombre_bd="analisis_portafolio.db"):
        # Establecer conexión con la base de datos
        self.conexion = sqlite3.connect(nombre_bd)
        self.puntero = self.conexion.cursor()
        print("Conexión establecida correctamente")

    def cerrar_conexion(self):
        # Cerrar la conexión
        self.conexion.close()
