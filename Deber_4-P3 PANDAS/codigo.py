import pandas as pd

# 1. Crear un DataFrame con datos de estudiantes
datos = {
    'Nombre': ['Ana', 'Carlos', 'Elena', 'Diego', 'Beatriz'],
    'Edad': [20, 22, 21, 23, 20],
    'Nota': [8.5, 6.0, 9.2, 5.5, 9.8],
    'Aprobado': [True, False, True, False, True]
}

df_estudiantes = pd.DataFrame(datos)

# 2. Filtrar estudiantes aprobados con nota mayor o igual a 8.0
aprobados_destacados = df_estudiantes[df_estudiantes['Nota'] >= 8.0]

# 3. Calcular el promedio general de notas
promedio_notas = df_estudiantes['Nota'].mean()

# Mostrar resultados
print("=== DATOS GENERALES ===")
print(df_estudiantes)
print("\n=== ESTUDIANTES DESTACADOS (Nota >= 8.0) ===")
print(aprobados_destacados)
print(f"\nPromedio general de notas: {promedio_notas:.2f}")