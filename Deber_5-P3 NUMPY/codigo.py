import numpy as np

# Datos: Calificaciones de 10 estudiantes en 3 parciales (Matriz de 10x3)
np.random.seed(42)  # Semilla para reproducibilidad
calificaciones = np.random.uniform(5.0, 10.0, (10, 3)).round(2)

print("--- MATRIZ DE CALIFICACIONES ---")
print(calificaciones)
print("-" * 35)

# Operaciones Estadísticas
promedio_por_estudiante = np.mean(calificaciones, axis=1)
promedio_general = np.mean(calificaciones)
nota_maxima = np.max(calificaciones)
aprobados = np.sum(promedio_por_estudiante >= 7.0)

print(f"Promedio por estudiante: {promedio_por_estudiante.round(2)}")
print(f"Promedio general del grupo: {promedio_general:.2f}")
print(f"Nota más alta registrada: {nota_maxima}")
print(f"Cantidad de estudiantes aprobados (promedio >= 7.0): {aprobados}")