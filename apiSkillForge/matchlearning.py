import mysql.connector
from cuestionario import realizar_test_estilo_aprendizaje

# Conexión a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="skillforge"
)

cursor = conexion.cursor()

respuestas_usuario = [
    {'pregunta': 1, 'respuesta': None, 'estilo': 'visual'},
    {'pregunta': 2, 'respuesta': None, 'estilo': 'auditivo'},
    {'pregunta': 3, 'respuesta': None, 'estilo': 'visual'},
    {'pregunta': 4, 'respuesta': None, 'estilo': 'auditivo'},
    {'pregunta': 5, 'respuesta': None, 'estilo': 'visual'},
    {'pregunta': 6, 'respuesta': None, 'estilo': 'auditivo'},
    {'pregunta': 7, 'respuesta': None, 'estilo': 'visual'},
    {'pregunta': 8, 'respuesta': None, 'estilo': 'auditivo'},
    {'pregunta': 9, 'respuesta': None, 'estilo': 'visual'},
    {'pregunta': 10, 'respuesta': None, 'estilo': 'auditivo'},
]

# Rellenar respuestas del usuario
for respuesta in respuestas_usuario:
    respuesta['respuesta'] = input(f"{respuesta['pregunta']}. {respuesta['estilo'].capitalize()} - Respuesta: ").strip().lower()

# Calcula el estilo de aprendizaje
estilo_dominante = realizar_test_estilo_aprendizaje()

# Calcula el estilo de aprendizaje
estilo_dominante = realizar_test_estilo_aprendizaje()

# Imprime resultados
print(f"Estilo de aprendizaje dominante: {estilo_dominante}")
