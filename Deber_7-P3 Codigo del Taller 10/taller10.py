def calcular_nivel(puntaje):
    if puntaje >= 90:
        return "Experto"
    elif puntaje >= 75:
        return "Avanzado"
    elif puntaje >= 60:
        return "Intermedio"
    else:
        return "Básico"


def calcular_evaluacion(completitud, eficiencia, competencias):
    puntaje = (completitud + eficiencia + competencias) / 3
    nivel = calcular_nivel(puntaje)
    return puntaje, nivel


def generar_informe(nombre, disciplina, puntaje, nivel):
    print("\n===== INFORME PERSONALIZADO =====")
    print("Nombre:", nombre)
    print("Disciplina:", disciplina)
    print("Puntaje final:", round(puntaje, 2))
    print("Nivel alcanzado:", nivel)


def main():
    print("===== EVALUACIÓN DE ACTIVIDAD =====")

    nombre = input("Ingrese el nombre del estudiante: ")
    disciplina = input("Ingrese la disciplina: ")

    print("\nIngrese las calificaciones de 0 a 100.")
    completitud = float(input("Completitud: "))
    eficiencia = float(input("Eficiencia: "))
    competencias = float(input("Competencias digitales: "))

    if not all(0 <= nota <= 100 for nota in [completitud, eficiencia, competencias]):
        print("Las calificaciones deben estar entre 0 y 100.")
        return

    puntaje, nivel = calcular_evaluacion(
        completitud,
        eficiencia,
        competencias
    )

    generar_informe(nombre, disciplina, puntaje, nivel)

    print("\nEl docente puede revisar la calificación y los resultados obtenidos.")


if __name__ == "__main__":
    main()
