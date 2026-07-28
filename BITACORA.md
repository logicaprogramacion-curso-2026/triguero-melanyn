 Bitácora de avances

Registra aquí cada sesión de trabajo. Un commit por avance, con un mensaje claro (ver guía abajo).

## Cómo escribir buenos mensajes de commit

- ❌ `arreglos`, `cambios`, `avance`
- ✅ `Implementa función de búsqueda binaria en lista ordenada`
- ✅ `Corrige error de índice fuera de rango en recorrido de matriz`
- ✅ `Agrega validación de entrada en menú principal`

## Registro de sesiones 
Objetivo general:
Crear un sistema que ofrezca retroalimentación inmediata al estudiante mientras
aprende, permitiendo intentos múltiples y seguimiento de progreso.
Objetivos específicos:
- Diseñar e implementar un algoritmo de evaluación automatizada capaz de analizar
las respuestas del estudiante y entregar retroalimentación explicativa (no solo indicar
si es correcto o incorrecto) en un tiempo menor a 2 segundos tras el envío.
- Programar una lógica de progresión que permita al menos 3 intentos por actividad,
configurando el sistema para que reduzca el puntaje de forma proporcional en cada
intento fallido y, simultáneamente, libere pistas o recursos de apoyo multimedia
orientados a la resolución del error detectado.
- Garantizar que el sistema de retroalimentación e intentos sea completamente
funcional y fácil de usar tanto en computadoras de escritorio como en dispositivos
móviles, reduciendo la fricción en la navegación del estudiante. 

## SEMANA 2 
* **Qué hice:** Diseñé la arquitectura por capas del proyecto y desarrollé la capa de datos. Creé la lista ejercicios para almacenar las preguntas y el diccionario progreso para registrar la información del estudiante, organizando los datos de forma clara y estructurada.
* **Qué problema encontré:** Definir la estructura más adecuada para almacenar tanto los ejercicios como el progreso del usuario, de manera que fuera fácil acceder y actualizar la información durante la ejecución del programa.
* **Cómo lo resolví:** Utilicé una lista de diccionarios para representar los ejercicios, ya que permite guardar múltiples registros con sus respectivos atributos. Además, implementé un diccionario para el progreso del estudiante, facilitando la gestión de datos como aciertos, intentos y estado.
* **Próximo paso:** Implementar la siguiente capa de la arquitectura, desarrollando la lógica del programa para mostrar las preguntas, validar las respuestas, actualizar el progreso del estudiante y generar los resultados finales.


Diseño de la arquitectura por capas
Durante esta semana se planificó la estructura general del proyecto antes de comenzar a
programar.
Se decidió utilizar una arquitectura por capas para separar las responsabilidades del
sistema.
Capa 1 – Datos
Esta capa almacena toda la información utilizada durante la ejecución del programa.
Para ello se creó una lista llamada ejercicios.
Se utilizó una lista porque permite almacenar varios ejercicios dentro de una misma
variable.
Cada elemento de la lista es un diccionario, ya que un diccionario permite guardar
información relacionada mediante claves y valores.
Por ejemplo, cada ejercicio contiene:
● número
● tema
● pregunta
● respuesta correcta
● explicación
El uso de diccionarios facilita acceder a la información utilizando el nombre de cada campo.
Ejemplo:
ejercicio["pregunta"]

Con esto el programa obtiene únicamente la pregunta del ejercicio.
También se creó un diccionario llamado progreso, encargado de almacenar la información
del estudiante.
Este diccionario guarda:
● nombre
● cantidad de aciertos
● intentos realizados
● estado
● total de preguntas
Gracias a esta organización todos los datos permanecen agrupados y es más sencillo
actualizarlos durante la ejecución. 


CAPA 1 - DATOS

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


### SEMANA 4 
* **Qué hice**: Desarrollé la capa de lógica del programa implementando las funciones principales del sistema. Estas funciones permiten generar los ejercicios, verificar las respuestas del usuario, calcular el puntaje final e identificar los temas en los que el estudiante presenta mayores dificultades.

* **Qué problema encontré:** Organizar la lógica del programa de forma modular para evitar código repetido y facilitar el mantenimiento, asegurando que cada función cumpliera una única responsabilidad.

* **Cómo lo resolví:** Dividí el programa en funciones independientes: `generar_ejercicio()` para obtener los ejercicios, `verificar_respuesta()` para validar las respuestas, `calcular_puntaje()` para calcular y redondear la nota, y `detectar_temas_debiles()` para identificar los temas en los que el estudiante cometió errores.

* **Próximo paso:** Implementar la capa de presentación para integrar estas funciones con la interfaz del usuario, permitiendo mostrar las preguntas, recibir respuestas y presentar los resultados finales de manera interactiva.

Desarrollo de la lógica del programa
En esta etapa se implementaron todas las funciones encargadas de realizar los procesos
principales del sistema.
Las funciones permiten dividir el programa en pequeñas tareas independientes, haciendo
que el código sea más organizado y fácil de mantener.
Función generar_ejercicio()
def generar_ejercicio():
return ejercicios

Esta función devuelve la lista completa de ejercicios.
Su objetivo es entregar los datos que posteriormente serán utilizados por la interfaz para
mostrar las preguntas.
Función verificar_respuesta()
def verificar_respuesta(respuesta, ejercicio):
return respuesta == ejercicio["correcta"]

Esta función compara la respuesta ingresada por el usuario con la respuesta correcta
almacenada en el diccionario.
Se utiliza el operador de comparación ==, el cual devuelve un valor booleano.
Puede devolver:
● True si la respuesta es correcta.
● False si la respuesta es incorrecta.
Esto permite tomar decisiones posteriormente mediante estructuras condicionales.
Función calcular_puntaje()
nota = (progreso["aciertos"] / progreso["total_preguntas"]) * 10

Esta función calcula automáticamente la nota del estudiante.
Para ello divide el número de respuestas correctas entre el total de preguntas y
posteriormente multiplica el resultado por diez.
Finalmente utiliza:
round(nota,1)

La función round() sirve para redondear la nota a un decimal.
Función detectar_temas_debiles()
Esta función recibe una lista llamada errores.
Primero verifica si la lista está vacía.
if len(errores)==0

La función len() devuelve la cantidad de elementos de una lista.
Si el estudiante no tuvo errores, se muestra el mensaje:
No se detectaron temas débiles.
En caso contrario utiliza:
",".join(errores)
El método join() une todos los temas dentro de un solo texto separados por comas. 

CAPA 2 - LÓGICA

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

- Qué hice:
- Qué problema encontré:
- Cómo lo resolví:
- Próximo paso:

### SEMANA 6 
* **Qué hice:** Desarrollé la capa de interfaz de usuario (CLI), implementando las funciones necesarias para interactuar con el usuario desde la consola. Estas funciones permiten mostrar el menú, presentar las preguntas, recibir las respuestas, brindar retroalimentación inmediata y mostrar el panel final de progreso.

* **Qué problema encontré:** Organizar la interacción con el usuario de forma clara y sencilla, asegurando que la información se mostrara en el orden correcto y que las respuestas ingresadas pudieran procesarse adecuadamente.

* **Cómo lo resolví:** Implementé funciones específicas para cada interacción: `mostrar_menu()` para las opciones principales, `mostrar_pregunta()` para presentar cada ejercicio, `recibir_respuesta()` para capturar y convertir la respuesta del usuario, `mostrar_retroalimentacion()` para informar si la respuesta fue correcta o incorrecta, y `mostrar_panel_progreso()` para mostrar el resumen final de la evaluación.

* **Próximo paso:** Integrar la interfaz con las capas de datos y lógica, realizar pruebas completas del flujo de evaluación y corregir posibles errores para garantizar el correcto funcionamiento del sistema.

Desarrollo de la interfaz de usuario (CLI)
Como el uso de LLM era opcional, el grupo decidió implementar únicamente la interfaz de
consola.
Esta capa se encarga de toda la interacción con el usuario.
Función mostrar_menu()
Esta función imprime las opciones disponibles.
Utiliza la función:
print()

para mostrar información en pantalla.
El usuario puede escoger:
● Iniciar evaluación.
● Salir.
Función mostrar_pregunta()
Recibe como parámetro un ejercicio.

Posteriormente utiliza:
print()

para mostrar:
● número
● tema
● pregunta
Se utilizan las f-strings.
Ejemplo:
print(Tema: {ejercicio[tema]})

Las f-strings permiten insertar variables dentro de un texto de forma sencilla.
Función recibir_respuesta()
return int(input())

Esta función utiliza:
input()
para leer lo que escribe el usuario.
Luego utiliza:
int()
para convertir el texto ingresado en un número entero.
Finalmente devuelve ese número para que pueda ser comparado con la respuesta correcta.
Función mostrar_retroalimentacion()
Esta función utiliza una estructura condicional.
if correcta:

Si la respuesta fue correcta, muestra un mensaje de felicitación.

En caso contrario utiliza:
else

para mostrar:
● respuesta correcta
● explicación
De esta manera el estudiante conoce cuál era la solución correcta.
Función mostrar_panel_progreso()
Esta función presenta el resumen final de la evaluación.
Utiliza varias instrucciones print() para mostrar:
● nombre
● aciertos
● intentos
● nota
● temas débiles
● estado 

CAPA 3 - INTERFAZ CLI

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

### SEMANA 8 
En ese caso, el **próximo paso** debe reflejar que el desarrollo ya terminó y solo queda cerrar el proyecto.

* **Qué hice:** Integré las capas de datos, lógica e interfaz para construir el flujo completo del programa. Implementé la secuencia de ejecución que permite mostrar el menú, recorrer las preguntas, validar las respuestas, actualizar el progreso del estudiante y presentar el resultado final de la evaluación.

* **Qué problema encontré:** Coordinar la comunicación entre las diferentes funciones y asegurar que el progreso del estudiante se actualizara correctamente durante toda la evaluación para obtener resultados precisos.

* **Cómo lo resolví:** Integré todas las funciones utilizando ciclos y estructuras condicionales para controlar el flujo del programa, actualicé el diccionario `progreso` en cada intento y generé el panel final con la nota y los temas débiles del estudiante.

* **Próximo paso:** Elaborar la conclusión del proyecto, documentar los resultados obtenidos y realizar la presentación final del sistema desarrollado.

Integración del proyecto
En la etapa final se integraron todas las funciones para construir el flujo completo del
programa.
Para controlar la ejecución se utiliza un bucle while.
while True:

El bucle while permite repetir un conjunto de instrucciones mientras la condición sea
verdadera.
En este caso la condición es True, por lo que el menú permanece activo hasta que el
usuario decide salir.
Cuando el usuario selecciona la opción de salir, se utiliza:
break

La instrucción break finaliza inmediatamente el bucle y termina la ejecución del programa.
Uso del ciclo for
Para recorrer todas las preguntas se utiliza un ciclo for.
for ejercicio in lista:

Este ciclo permite recorrer uno por uno todos los ejercicios almacenados dentro de la lista.
En cada repetición el programa:
● muestra la pregunta;
● recibe la respuesta;
● verifica si es correcta;
● actualiza el progreso;
● muestra la retroalimentación.
El ciclo finaliza automáticamente cuando ya no quedan ejercicios por recorrer.
Uso de estructuras condicionales
Durante todo el programa se emplean estructuras if, elif y else.
Estas permiten tomar decisiones dependiendo de distintas condiciones.
Por ejemplo:
if correcta:

Si la respuesta es correcta se incrementan los aciertos.
En caso contrario:
else:

se agrega el tema a la lista de errores para identificar posteriormente las áreas donde el
estudiante presentó dificultades.

Actualización del progreso

Cada vez que el usuario responde una pregunta se actualizan los datos del diccionario
progreso.
Por ejemplo:
progreso[intentos] += 1

El operador += incrementa el valor anterior en una unidad.
Si la respuesta fue correcta también se incrementa:
progreso[aciertos] += 1

Esto permite calcular correctamente la nota al finalizar la evaluación. 


PROGRAMA UNION 
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
<!-- Agrega tantas secciones como sesiones de trabajo tengas -->

