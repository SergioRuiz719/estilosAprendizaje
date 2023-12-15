# **Cosas a desarrollar**

- [] Determinar que base vamos a usar
- [] Desarrollar la Api
- [] Implementar Firbase
- [] Obtener el correo para relacionarlo y que se guarde en la base y con esto se quede determinado el estilo de aprendizaje obtenido
- [] Desarrollar Perfiles de Estilo de Aprendizaje:
    - Define perfiles para cada estilo de aprendizaje, indicando consejos, estrategias y ejercicios específicos para cada uno. Estos perfiles serán utilizados para proporcionar recomendaciones personalizadas a los usuarios.
- [] 

# **PROCEDIMIENTO PARA DESARROLLO DEL MATCH LEARNING**

1. Iniciar nuevo archivo de python
2. Instalar MySQL 
    - pip install mysql-connector-python

3. Conexiòn
    - ``` Python
        conexion = mysql.connector.connect(
        host="localhots",
        user="root",
        password="",
        database="skillforge"
        ) ```

4. Clase para representar el perfil de aprendizaje del usuario
    - ``` Python
        class EstiloAprendizaje:
             def __init__(self, id_estilo, nombre):
                self.id_estilo = id_estilo
                self.nombre = nombre

5. Clase para el sistema de match learning
    - ``` Python
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


# Consultas
- https://hevodata.com/learn/flask-mysql/
- https://keepcoding.io/blog/ejemplos-de-algoritmos-de-matching/
https://tecadmin.net/working-with-python-fastapi-and-mysql/