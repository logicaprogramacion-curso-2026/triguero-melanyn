# [Nombre del proyecto]

**Grupo:** [Triguero Melanyn
            Anthony Conforme
            Fiorella Herdoiza]
**Curso:** [Logica de programacion]
**Fecha de inicio:** [12/06/2026]

# Sistema de Evaluación con Retroalimentación Inmediata

## 1. Objetivo del proyecto

Este proyecto tiene como objetivo desarrollar un sistema de evaluación que permita al estudiante responder ejercicios de matemáticas y recibir retroalimentación inmediata sobre su desempeño. Durante su desarrollo se aprendió a aplicar una arquitectura por capas, organizar el código mediante funciones y utilizar estructuras de datos para facilitar el mantenimiento y la escalabilidad del sistema.

---

## 2. Cómo ejecutar el código

```bash
python main.py
```

**Requisitos previos:**

- Python 3.10 o superior.
- No requiere librerías externas, únicamente Python estándar.

---

## 3. Estructura del repositorio

```
├── src/               # Código fuente del proyecto
├── docs/              # Documentación y evidencias
├── README.md          # Documentación del proyecto
└── BITACORA.md        # Registro de avances por fases
```

---

## 4. Decisiones de diseño

Se implementó una arquitectura por capas para separar la gestión de datos, la lógica del programa y la interfaz de usuario, facilitando el mantenimiento del código.

Para almacenar los ejercicios se utilizó una lista de diccionarios, ya que permite organizar múltiples preguntas con sus respectivos atributos (tema, pregunta, respuesta correcta y explicación). El progreso del estudiante se almacenó en un diccionario para actualizar fácilmente los aciertos, intentos, estado y total de preguntas.

Además, la lógica del sistema se dividió en funciones independientes para evitar la duplicación de código y hacer más sencilla la reutilización y comprensión del programa.

---

## 5. Problemas encontrados y cómo los resolviste

- **Organización de los datos:** Al inicio fue necesario definir una estructura que permitiera almacenar los ejercicios y el progreso del estudiante de manera ordenada. Se resolvió utilizando listas y diccionarios.

- **Modularización de la lógica:** Se buscó evitar código repetido durante el desarrollo. Para solucionarlo se implementaron funciones específicas para generar ejercicios, verificar respuestas, calcular la nota e identificar los temas débiles.

- **Interacción con el usuario:** Fue necesario organizar correctamente la comunicación mediante consola para mostrar preguntas, recibir respuestas y presentar resultados. Esto se resolvió creando funciones independientes para cada interacción.

- **Integración del sistema:** La principal dificultad fue coordinar correctamente las capas de datos, lógica e interfaz. Se solucionó integrando todas las funciones mediante ciclos y estructuras condicionales que permitieron actualizar el progreso y mostrar el resultado final correctamente.

---

## 6. Reflexión final

Este proyecto permitió aplicar conceptos fundamentales de programación como estructuras de datos, funciones, ciclos y condicionales dentro de un caso práctico. Uno de los mayores desafíos fue integrar correctamente todas las capas del sistema para que trabajaran de forma coordinada.

Si se desarrollara nuevamente el proyecto, se incorporaría una interfaz gráfica o una aplicación web para mejorar la experiencia del usuario, además de agregar más ejercicios, distintos niveles de dificultad y un sistema de intentos múltiples con pistas automáticas, tal como fue planteado inicialmente en los objetivos. 


