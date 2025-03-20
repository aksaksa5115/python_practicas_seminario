import random
# Preguntas para el juego
questions = [
"¿Qué función se usa para obtener la longitud de una cadena en Python?",
"¿Cuál de las siguientes opciones es un número entero en Python?",
"¿Cómo se solicita entrada del usuario en Python?",
"¿Cuál de las siguientes expresiones es un comentario válido en Python?",
"¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    (
        "// Esto es un comentario",
        "/* Esto es un comentario */",
        "-- Esto es un comentario",
        "# Esto es un comentario",
    ),
    ("=", "==", "!=", "==="),
]
# Índice de la respuesta correcta para cada pregunta, el el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]
# se comprimen las listas para facilitar su entrada
questions_to_ask = random.sample(list(
    zip(questions, answers, correct_answers_index)), k=3)
# El usuario deberá contestar 3 preguntas
puntaje = 0
for question, answer, correct_answers in questions_to_ask:
    # Se muestra la pregunta y las respuestas posibles
    print(question)
    # extraigo indice para acomodar la impresion de las respuestas
    index = questions.index(question)
    # imprimo las respuestas de forma limpia y ordenada
    for i, answer in enumerate(answers[index]):
        print(f"{i + 1}. {answer}")
        # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        respuesta = input('ingrese un numero entre 1 y 4 inclusive: ')
        # se le ruega al usuario que imprima una opcion valida
        while not respuesta.isdigit() or not (1 <= int(respuesta) <= 4):
            respuesta = input('ingrese un numero entre 1 y 4 valido: ')
        
        respuesta = int(respuesta) - 1
        # Se verifica si la respuesta es correcta
        if respuesta == correct_answers:
            print("¡Correcto!")
            puntaje += 1
            break
        else:
            # Si el usuario no responde correctamente después de 2 intentos,
            # se muestra la respuesta correcta
            puntaje += -0.5
            print("incorrecto, intentalo de nuevo burro")
            if intento == 1:
                print("Incorrecto. La respuesta correcta es:")
                print(correct_answers + 1)
        # Se imprime un blanco al final de la pregunta
    print()
print('--------------------------------')
print(f'juego terminado, tu puntaje fue de {puntaje}')