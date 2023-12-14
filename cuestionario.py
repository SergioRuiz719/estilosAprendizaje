def realizar_test_estilo_aprendizaje():
    preguntas = [
        "Cuando intentas recordar algo importante, ¿qué haces principalmente?\n a. Visualizo imágenes o diagramas.\n b. Repito la información en mi mente o en voz alta.\n c. Leo las notas o el material.\n d. Hago movimientos o gestos para recordar.",
        "Al aprender una nueva habilidad, ¿cómo prefieres que te enseñen?\n a. Con gráficos, diagramas o videos.\n b. A través de explicaciones verbales o discusiones.\n c. A través de material escrito como libros o apuntes.\n d. Practicando y haciendo actividades prácticas.",
        "¿Cuál es tu estrategia preferida para estudiar para un examen?\n a. Usar tarjetas de memoria o mapas conceptuales.\n b. Leer en voz alta o discutir con otros.\n c. Leer y subrayar el material.\n d. Practicar con ejercicios y problemas.",
        "¿Cómo prefieres recibir información nueva en una presentación?\n a. A través de gráficos, gráficos y demostraciones visuales.\n b. A través de conferencias o explicaciones verbales.\n c. A través de material escrito y notas.\n d. A través de actividades prácticas o demostraciones.",
        "Cuando tienes que seguir las instrucciones de algo nuevo, ¿qué haces primero?\n a. Observo las imágenes o diagramas si los hay.\n b. Escucho las instrucciones atentamente.\n c. Leo las instrucciones por escrito.\n d. Intento realizar la actividad mientras sigo las instrucciones.",
        "¿Cómo te resulta más fácil recordar nombres o datos importantes?\n a. Asociándolos con imágenes o caras.\n b. Repitiéndolos en voz alta varias veces.\n c. Leyendo y escribiendo la información.\n d. Relacionándolos con experiencias o actividades.",
        "En un grupo de estudio, ¿cuál es tu papel principal?\n a. Crear gráficos o presentaciones visuales.\n b. Participar en discusiones y explicar conceptos.\n c. Organizar y resumir la información por escrito.\n d. Realizar actividades prácticas o experimentos."
    ]

    respuestas = []

    for pregunta in preguntas:
        respuesta = input(pregunta + "\nRespuesta: ").strip().lower()
        respuestas.append(respuesta)

    total_respuestas = len(respuestas)
    contador_estilos = {"a": 0, "b": 0, "c": 0, "d": 0}

    for respuesta in respuestas:
        contador_estilos[respuesta] += 1

    porcentajes_estilos = {opcion: (contador / total_respuestas) * 100 for opcion, contador in contador_estilos.items()}

    estilo_aprendizaje = max(porcentajes_estilos, key=porcentajes_estilos.get)

    print("\nResultados porcentuales:")
    for opcion, porcentaje in porcentajes_estilos.items():
        print(f"{opcion.upper()}: {porcentaje:.2f}%")

    print("\nTu estilo de aprendizaje predominante es:", end=" ")
    if estilo_aprendizaje == "a":
        print("Visual.")
    elif estilo_aprendizaje == "b":
        print("Auditivo.")
    elif estilo_aprendizaje == "c":
        print("Lector-escritor.")
    elif estilo_aprendizaje == "d":
        print("Kinestésico.")

if __name__ == "__main__":
    realizar_test_estilo_aprendizaje()
