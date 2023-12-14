import mysql.connector

# Conexión a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="tu_usuario",
    password="tu_contraseña",
    database="skillforge"
)

cursor = conexion.cursor()


class EstiloAprendizaje:
    def __init__(self, visual=0, auditivo=0, lector_escritor=0, kinestesico=0):
        self.visual = visual
        self.auditivo = auditivo
        self.lector_escritor = lector_escritor
        self.kinestesico = kinestesico


def calcular_estilo_aprendizaje(respuestas):
    puntajes = {'visual': 0, 'auditivo': 0, 'lector_escritor': 0, 'kinestesico': 0}

    for respuesta in respuestas:
        puntajes[respuesta['estilo']] += 1

    total_preguntas = len(respuestas)
    porcentajes = {estilo: (puntos / total_preguntas) * 100 for estilo, puntos in puntajes.items()}

    estilo_dominante = max(porcentajes, key=porcentajes.get)
    return estilo_dominante


def almacenar_estilo_aprendizaje(id_usuario, estilo_aprendizaje):
    cursor.execute(
        "INSERT INTO Usuarios (ID_Usuario, ID_Estilo_Apr) VALUES (%s, (SELECT ID_Estilo FROM EstilosAprendizaje WHERE Nombre = %s)) ON DUPLICATE KEY UPDATE ID_Estilo_Apr = (SELECT ID_Estilo FROM EstilosAprendizaje WHERE Nombre = %s)",
        (id_usuario, estilo_aprendizaje, estilo_aprendizaje))
    conexion.commit()


def obtener_consejos(estilo_aprendizaje):
    cursor.execute(
        "SELECT Consejo FROM Consejo WHERE ID_Estilo = (SELECT ID_Estilo FROM EstilosAprendizaje WHERE Nombre = %s)",
        (estilo_aprendizaje,))
    return cursor.fetchone()[0]


def obtener_estrategias(estilo_aprendizaje):
    cursor.execute(
        "SELECT Estrategias FROM Estrategia WHERE ID_Estilo = (SELECT ID_Estilo FROM EstilosAprendizaje WHERE Nombre = %s)",
        (estilo_aprendizaje,))
    return cursor.fetchone()[0]


def obtener_ejercicios(estilo_aprendizaje):
    cursor.execute(
        "SELECT Ejercicios FROM Ejercicio WHERE ID_Estilo = (SELECT ID_Estilo FROM EstilosAprendizaje WHERE Nombre = %s)",
        (estilo_aprendizaje,))
    return cursor.fetchone()[0]


# Ejemplo de uso
respuestas_usuario = [
    {'pregunta': 1, 'respuesta': 'a', 'estilo': 'visual'},
    {'pregunta': 2, 'respuesta': 'b', 'estilo': 'auditivo'},
    # ... Agrega todas las respuestas del usuario
]

# Calcula el estilo de aprendizaje
estilo_dominante = calcular_estilo_aprendizaje(respuestas_usuario)

# Almacena el estilo de aprendizaje en la base de datos (sustituye 'id_usuario' con el ID real del usuario)
almacenar_estilo_aprendizaje(id_usuario=1, estilo_aprendizaje=estilo_dominante)

# Obtiene consejos, estrategias y ejercicios basados en el estilo de aprendizaje
consejos = obtener_consejos(estilo_dominante)
estrategias = obtener_estrategias(estilo_dominante)
ejercicios = obtener_ejercicios(estilo_dominante)

print(f"Estilo de aprendizaje dominante: {estilo_dominante}")
print(f"Consejos: {consejos}")
print(f"Estrategias: {estrategias}")
print(f"Ejercicios: {ejercicios}")
