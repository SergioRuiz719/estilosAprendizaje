import mysql.connector
import requests

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="skillforge"
)

cursor = conexion.cursor()


def obtener_id_usuario_actual():
    # Esta función ahora hace la solicitud a la API para obtener el ID_Usuario_Actual
    response = requests.get("http://localhost:5000/api/id_usuario_actual")
    if response.status_code == 200:
        return response.json().get("ID_Usuario_Actual")
    else:
        raise Exception(f"Error al obtener ID de usuario actual. Código de respuesta: {response.status_code}")


def realizar_test_estilo_aprendizaje():
    global aux_estilo_aprendizaje
    preguntas = [
        "Cuando intentas recordar algo importante, ¿qué haces principalmente?\n a. Visualizo imágenes o diagramas.\n b. Repito la información en mi mente o en voz alta.\n c. Hago movimientos o gestos para recordar.",
        "Al aprender una nueva habilidad, ¿cómo prefieres que te enseñen?\n a. Con gráficos, diagramas o videos.\n b. A través de explicaciones verbales o discusiones.\n c. Practicando y haciendo actividades prácticas.",
        "¿Cuál es tu estrategia preferida para estudiar para un examen?\n a. Usar tarjetas de memoria o mapas conceptuales.\n b. Leer en voz alta o discutir con otros.\n c. Practicar con ejercicios y problemas.",
        "¿Cómo prefieres recibir información nueva en una presentación?\n a. A través de gráficos, gráficos y demostraciones visuales.\n b. A través de conferencias o explicaciones verbales.\n c. A través de actividades prácticas o demostraciones.",
        "Cuando tienes que seguir las instrucciones de algo nuevo, ¿qué haces primero?\n a. Observo las imágenes o diagramas si los hay.\n b. Escucho las instrucciones atentamente.\n c. Intento realizar la actividad mientras sigo las instrucciones.",
        "¿Cómo te resulta más fácil recordar nombres o datos importantes?\n a. Asociándolos con imágenes o caras.\n b. Repitiéndolos en voz alta varias veces.\n c. Relacionándolos con experiencias o actividades.",
        "En un grupo de estudio, ¿cuál es tu papel principal?\n a. Crear gráficos o presentaciones visuales.\n b. Participar en discusiones y explicar conceptos.\n c. Realizar actividades prácticas o experimentos."
    ]

    respuestas = []

    for pregunta in preguntas:
        respuesta = input(pregunta + "\nRespuesta: ").strip().lower()
        respuestas.append(respuesta)

    total_respuestas = len(respuestas)
    contador_estilos = {"a": 0, "b": 0, "c": 0}

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
        aux_estilo_aprendizaje = 1
    elif estilo_aprendizaje == "b":
        print("Auditivo.")
        aux_estilo_aprendizaje = 2
    elif estilo_aprendizaje == "c":
        print("Kinestésico.")
        aux_estilo_aprendizaje = 3


    api_url = "http://localhost:5000/api/usuarios/1"#modificar por el Id del usuario haciendo uso de la API
    aprendizaje_actualizado = {
        "ID_Estilo": aux_estilo_aprendizaje
    }
    try:
        response = requests.put(api_url, json=aprendizaje_actualizado)
        if response.status_code == 200:
            print("Estilo de aprendizaje actualizado correctamente")
        else:
            print(f"Error al actualizar aprendizaje. Código de respuesta: {response.status_code}")
    except Exception as e:
        print(f"Error al realizar la solicitud a la API: {e}")

    return estilo_aprendizaje


if __name__ == "__main__":
    estilo_usuario = realizar_test_estilo_aprendizaje()
    print(f"Estilo de aprendizaje predominante: {estilo_usuario}")