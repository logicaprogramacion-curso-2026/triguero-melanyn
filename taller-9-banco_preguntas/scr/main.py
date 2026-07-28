import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from scr.dao import PreguntaDAO
from scr.gestor import GestorPreguntas
from scr.simulador import Simulador


# =========================================================
# RUTAS DEL PROYECTO
# =========================================================

RAIZ = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

RUTA_DB = os.path.join(
    RAIZ,
    "database",
    "preguntas.db"
)

RUTA_TXT = os.path.join(
    RAIZ,
    "preguntas.txt"
)

RUTA_CSV = os.path.join(
    RAIZ,
    "preguntas.csv"
)

RUTA_JSON = os.path.join(
    RAIZ,
    "preguntas.json"
)

CARPETA_RESULTADOS = os.path.join(
    RAIZ,
    "resultados"
)

os.makedirs(CARPETA_RESULTADOS, exist_ok=True)


# =========================================================
# COMPROBAR ARCHIVOS
# =========================================================

def comprobar_archivos():
    print("\n--- COMPROBACIÓN DE ARCHIVOS ---")
    print("Proyecto:", RAIZ)

    print(
        "TXT:",
        os.path.exists(RUTA_TXT),
        RUTA_TXT
    )

    print(
        "CSV:",
        os.path.exists(RUTA_CSV),
        RUTA_CSV
    )

    print(
        "JSON:",
        os.path.exists(RUTA_JSON),
        RUTA_JSON
    )

    print("--------------------------------\n")



# =========================================================
# MENÚ
# =========================================================

def mostrar_menu():

    print("\n" + "=" * 50)
    print(" BANCO DE PREGUNTAS - MENÚ PRINCIPAL")
    print("=" * 50)

    print("1. Cargar preguntas desde archivo")
    print("2. Ver todas las preguntas")
    print("3. Ver estadísticas")
    print("4. Iniciar simulación")
    print("5. Exportar datos")
    print("6. Ver reportes")
    print("7. Salir")

    print("=" * 50)

    return input("Selecciona una opción: ").strip()



# =========================================================
# CARGAR PREGUNTAS
# =========================================================

def cargar_preguntas(gestor):

    print("\n¿Desde qué archivo deseas cargar?")
    print("1. TXT")
    print("2. CSV")
    print("3. JSON")

    opcion = input("Opción: ").strip()


    try:

        if opcion == "1":

            preguntas = gestor.cargar_desde_txt(
                RUTA_TXT
            )


        elif opcion == "2":

            preguntas = gestor.cargar_desde_csv(
                RUTA_CSV
            )


        elif opcion == "3":

            preguntas = gestor.cargar_desde_json(
                RUTA_JSON
            )


        else:

            print("Opción inválida.")
            return



    except FileNotFoundError as e:

        print("\nArchivo no encontrado:")
        print(e)
        return


    except Exception as e:

        print("\nError al cargar:")
        print(e)
        return



    print(
        f"\nSe leyeron {len(preguntas)} preguntas."
    )


    if len(preguntas) > 0:

        guardadas = gestor.guardar_en_base_datos(
            preguntas
        )

        print(
            f"Se guardaron {guardadas} preguntas en la BD."
        )

    else:

        print(
            "El archivo está vacío o no tiene el formato correcto."
        )



# =========================================================
# VER PREGUNTAS
# =========================================================

def ver_preguntas(dao):

    preguntas = dao.obtener_todas()


    if not preguntas:

        print(
            "\nNo hay preguntas cargadas."
        )

        return


    print(
        f"\nTotal preguntas: {len(preguntas)}"
    )


    for p in preguntas:

        print(p)
        print("-" * 50)



# =========================================================
# ESTADÍSTICAS
# =========================================================

def ver_estadisticas(gestor):

    print("\n--- Por tema ---")

    for tema, total in gestor.estadisticas_por_tema().items():

        print(
            tema,
            ":",
            total
        )


    print("\n--- Por dificultad ---")

    for dif, total in gestor.estadisticas_por_dificultad().items():

        print(
            dif,
            ":",
            total
        )



# =========================================================
# SIMULACIÓN
# =========================================================

def iniciar_simulacion(dao):

    total = dao.contar_preguntas()


    if total == 0:

        print(
            "\nPrimero carga preguntas."
        )

        return


    try:

        cantidad = int(
            input(
                f"\nCantidad (máx {total}): "
            )
        )


    except ValueError:

        print(
            "Cantidad inválida."
        )

        return



    simulador = Simulador(dao)

    simulador.iniciar_simulacion(
        cantidad
    )

    simulador.guardar_todos_los_reportes()



# =========================================================
# EXPORTAR
# =========================================================

def exportar_datos(gestor):

    print("\n1 TXT")
    print("2 CSV")
    print("3 JSON")
    print("4 Todos")

    opcion = input("Opción: ")


    if opcion in ("1", "4"):

        gestor.exportar_a_txt(
            os.path.join(
                RAIZ,
                "preguntas_exportadas.txt"
            )
        )


    if opcion in ("2", "4"):

        gestor.exportar_a_csv(
            os.path.join(
                RAIZ,
                "preguntas_exportadas.csv"
            )
        )


    if opcion in ("3", "4"):

        gestor.exportar_a_json(
            os.path.join(
                RAIZ,
                "preguntas_exportadas.json"
            )
        )



# =========================================================
# REPORTES
# =========================================================

def ver_reportes():

    print(
        "\nCarpeta de reportes:"
    )

    print(
        CARPETA_RESULTADOS
    )



# =========================================================
# PROGRAMA PRINCIPAL
# =========================================================

def main():

    comprobar_archivos()


    dao = PreguntaDAO(
        ruta_db=RUTA_DB
    )


    gestor = GestorPreguntas(
        dao=dao
    )


    while True:

        opcion = mostrar_menu()


        if opcion == "1":

            cargar_preguntas(
                gestor
            )


        elif opcion == "2":

            ver_preguntas(
                dao
            )


        elif opcion == "3":

            ver_estadisticas(
                gestor
            )


        elif opcion == "4":

            iniciar_simulacion(
                dao
            )


        elif opcion == "5":

            exportar_datos(
                gestor
            )


        elif opcion == "6":

            ver_reportes()


        elif opcion == "7":

            print(
                "Hasta luego"
            )

            break


        else:

            print(
                "Opción inválida"
            )



if __name__ == "__main__":
    main()
