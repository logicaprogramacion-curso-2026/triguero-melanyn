ejercicios = [
    {
        "numero": 1,
        "tema": "Suma",
        "pregunta": "¿Cuánto es 8 + 5?",
        "correcta": 13,
        "explicacion": "La suma de 8 y 5 es 13."
    },
    {
        "numero": 2,
        "tema": "Resta",
        "pregunta": "¿Cuánto es 15 - 7?",
        "correcta": 8,
        "explicacion": "Al restar 7 de 15 obtenemos 8."
    },
    {
        "numero": 3,
        "tema": "Multiplicación",
        "pregunta": "¿Cuánto es 6 × 4?",
        "correcta": 24,
        "explicacion": "Multiplicar 6 por 4 da como resultado 24."
    },
    {
        "numero": 4,
        "tema": "División",
        "pregunta": "¿Cuánto es 20 ÷ 5?",
        "correcta": 4,
        "explicacion": "20 dividido entre 5 es igual a 4."
    },
    {
        "numero": 5,
        "tema": "Raíz cuadrada",
        "pregunta": "¿Cuál es la raíz cuadrada de 81?",
        "correcta": 9,
        "explicacion": "La raíz cuadrada de 81 es 9 porque 9 × 9 = 81."
    }
]

nombre = input("Ingresa tu nombre: ")

progreso = {
    "nombre": nombre,
    "aciertos": 0,
    "intentos": 0,
    "estado": "En proceso",
    "total_preguntas": len(ejercicios)
}

def generar_ejercicio():
    return ejercicios


def verificar_respuesta(respuesta, ejercicio):
    return respuesta == ejercicio["correcta"]


def calcular_puntaje(progreso):
    nota = (progreso["aciertos"] / progreso["total_preguntas"]) * 10
    return round(nota, 1)


def detectar_temas_debiles(errores):
    if len(errores) == 0:
        return "No se detectaron temas débiles."

    return ", ".join(errores)

def mostrar_menu():
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Iniciar evaluación")
    print("2. Salir")


def mostrar_pregunta(ejercicio):
    print(f"\nPregunta {ejercicio['numero']}")
    print(f"Tema: {ejercicio['tema']}")
    print(ejercicio['pregunta'])


def recibir_respuesta():
    return int(input("Tu respuesta: "))


def mostrar_retroalimentacion(correcta, ejercicio):
    if correcta:
        print("Respuesta correcta\n")
    else:
        print("Respuesta incorrecta")
        print(f"Respuesta correcta: {ejercicio['correcta']}")
        print(f"Explicación: {ejercicio['explicacion']}\n")


def mostrar_panel_progreso(progreso, nota, temas):
    print("\n===== PANEL DE PROGRESO =====")
    print(f"Estudiante: {progreso['nombre']}")
    print(f"Aciertos: {progreso['aciertos']} de {progreso['total_preguntas']}")
    print(f"Intentos realizados: {progreso['intentos']}")
    print(f"Nota final: {nota}/10")
    print(f"Temas débiles: {temas}")
    print(f"Estado: {progreso['estado']}")

mostrar_menu()
opcion = input("Seleccione una opción: ")

if opcion == "1":

    errores = []

    for ejercicio in generar_ejercicio():

        mostrar_pregunta(ejercicio)

        respuesta = recibir_respuesta()

        progreso["intentos"] += 1

        correcta = verificar_respuesta(respuesta, ejercicio)

        if correcta:
            progreso["aciertos"] += 1
        else:
            errores.append(ejercicio["tema"])

        mostrar_retroalimentacion(correcta, ejercicio)

    nota = calcular_puntaje(progreso)

    temas = detectar_temas_debiles(errores)

    progreso["estado"] = "Finalizada"

    mostrar_panel_progreso(progreso, nota, temas)

else:
    print("Programa finalizado.")