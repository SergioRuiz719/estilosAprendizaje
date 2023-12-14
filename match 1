import mysql.connector

conexion = mysql.connector.connect(
    host="localhots",
    user="root",
    password="",
    database="skillforge"
)
cursor = conexion.cursor()


# Clase para representar el perfil de aprendizaje del usuario
class EstiloAprendizaje:
    def __init__(self, id_estilo, nombre):
        self.id_estilo = id_estilo
        self.nombre = nombre


# Clase para el sistema de match learning
class MatchLearning:
    def __init__(self, id_estilo):
        self.id_estilo = id_estilo

    def obtener_consejos(self):
        cursor.execute("SELECT Consejo FROM Consejo WHERE ID_Estilo = %s", (self.id_estilo,))
        return cursor.fetchone()[0]

    def obtener_estrategias(self):
        cursor.execute("SELECT Estrategias FROM Estrategia WHERE ID_Estilo = %s", (self.id_estilo,))
        return cursor.fetchone()[0]

    def obtener_ejercicios(self):
        cursor.execute("SELECT Ejercicios FROM Ejercicio WHERE ID_Estilo = %s", (self.id_estilo,))
        return cursor.fetchone()[0]


# Función para determinar el estilo de aprendizaje basado en las respuestas del cuestionario
def obtener_estilo_aprendizaje(respuestas):
    # Lógica para determinar el estilo de aprendizaje
    # (en este caso, simplemente se cuenta la mayoría de respuestas)
    conteo_respuestas = {'A': respuestas.count('A'), 'B': respuestas.count('B'), 'C': respuestas.count('C'),
                         'D': respuestas.count('D')}
    estilo_dominante = max(conteo_respuestas, key=conteo_respuestas.get)

    # Obtener el ID del estilo de aprendizaje desde la base de datos
    cursor.execute("SELECT ID_Estilo FROM EstilosAprendizaje WHERE Nombre = %s", (estilo_dominante,))
    id_estilo = cursor.fetchone()[0]

    return id_estilo


def insertar_usuario(nombre, id_estilo):
    cursor.execute("INSERT INTO Usuarios (Nombre, ID_Estilo_Apr) VALUES (%s, %s)", (nombre, id_estilo))
    conexion.commit()


# Cuestionario de ejemplo
respuestas_usuario = ['A', 'B', 'A', 'C', 'D', 'A', 'B']

# Obtener el estilo de aprendizaje del usuario
estilo_usuario = obtener_estilo_aprendizaje(respuestas_usuario)

# Insertar el nuevo usuario en la base de datos
nombre_usuario = "UsuarioEjemplo"
insertar_usuario(nombre_usuario, estilo_usuario)

# Crear una instancia de MatchLearning para el usuario
match_learning = MatchLearning(estilo_usuario)

# Obtener consejos, estrategias y ejercicios personalizados
consejos_personalizados = match_learning.obtener_consejos()
estrategias_personalizadas = match_learning.obtener_estrategias()
ejercicios_personalizados = match_learning.obtener_ejercicios()

# Mostrar resultados
print(f"Consejos para {nombre_usuario}: {consejos_personalizados}")
print(f"Estrategias para {nombre_usuario}: {estrategias_personalizadas}")
print(f"Ejercicios para {nombre_usuario}: {ejercicios_personalizados}")

cursor.close()
conexion.close()
