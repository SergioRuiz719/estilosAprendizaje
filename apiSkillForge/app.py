from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'skillforge'

mysql = MySQL(app)


# Ruta para obtener todos los registros
@app.route('/api/usuarios', methods=['GET'])
def obtener_usuarios():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM usuarios")
    data = cur.fetchall()
    cur.close()
    return jsonify(data)


# Ruta para obtener un usuario por ID
@app.route('/api/usuarios/<int:ID_Usuario>', methods=['GET'])
def obtener_usuario(ID_Usuario):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM usuarios WHERE id = %s", (ID_Usuario,))
    data = cur.fetchone()
    cur.close()
    return jsonify(data)


# Ruta para crear un nuevo usuario
@app.route('/api/usuarios', methods=['POST'])
def crear_usuario():
    data = request.get_json()
    nombre = data['nombre']
    ID_Estilo_Apr = data['ID_Estilo_Apr']

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO usuarios (nombre, ID_Estilo_Apr) VALUES (%s, %s)", (nombre, ID_Estilo_Apr))
    mysql.connection.commit()
    cur.close()

    return jsonify({'mensaje': 'Usuario Asignado correctamente'})


# Ruta para actualizar un aprendizaje
@app.route('/api/usuarios/<int:ID_Usuario>', methods=['PUT'])
def actualizar_aprendizazje(ID_Usuario):
    data = request.get_json()
    ID_Estilo_Apr = data['ID_Estilo_Apr']

    cur = mysql.connection.cursor()
    cur.execute("UPDATE usuarios SET ID_Estilo_Apr = %s WHERE id = %s", (ID_Estilo_Apr, ID_Usuario))
    mysql.connection.commit()
    cur.close()

    return jsonify({'mensaje': 'Se actualizo correctamente el aprendizaje'})


"""
# Ruta para eliminar un usuario
@app.route('/api/usuarios/<int:usuario_id>', methods=['DELETE'])
def eliminar_usuario(usuario_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM usuarios WHERE id = %s", (usuario_id,))
    mysql.connection.commit()
    cur.close()

    return jsonify({'mensaje': 'Usuario eliminado correctamente'})
"""


# Ruta para inserter nuevo consejo
@app.route('/api/consejo', methods=['POST'])
def crear_consejo():
    data = request.get_json()
    ID_Estilo = data['ID_Estilo']
    Consejo = data['Consejo']

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO consejo (ID_Estilo, Consejo) VALUES (%s, %s)", (ID_Estilo, Consejo))
    mysql.connection.commit()
    cur.close()

    return jsonify({'mensaje': 'Consejo creado correctamente'})


# Ruta para eliminar un consejo
@app.route('/api/consejo/<int:ID_Consejo>', methods=['DELETE'])
def eliminar_consejo(ID_Consejo):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM consejo WHERE id = %s", (ID_Consejo,))
    mysql.connection.commit()
    cur.close()

    return jsonify({'mensaje': 'Consejo eliminado correctamente'})


# Ruta para  inserter nuevo ejercicio
@app.route('/api/ejercicio', methods=['POST'])
def crear_ejercicio():
    data = request.get_json()
    ID_Estilo = data['ID_Estilo']
    Ejercicios = data['Ejercicios']

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO ejercicio (ID_Estilo, Ejercicios) VALUES (%s, %s)", (ID_Estilo, Ejercicios))
    mysql.connection.commit()
    cur.close()

    return jsonify({'mensaje': 'Ejercicio creado correctamente'})


# Ruta para eliminar un ejercicio
@app.route('/api/ejercicio/<int:ID_Ejercicio>', methods=['DELETE'])
def eliminar_ejercicio(ID_Ejercicio):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM ejercicio WHERE id = %s", (ID_Ejercicio,))
    mysql.connection.commit()
    cur.close()

    return jsonify({'mensaje': 'Ejercicio eliminado correctamente'})


# Ruta para  inserter nueva estrategia
@app.route('/api/estrategia', methods=['POST'])
def crear_estrategia():
    data = request.get_json()
    ID_Estilo = data['ID_Estilo']
    Estrategias = data['Estrategias']

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO ejercicio (ID_Estilo, Estrategias) VALUES (%s, %s)", (ID_Estilo, Estrategias))
    mysql.connection.commit()
    cur.close()

    return jsonify({'mensaje': 'Estrategia creado correctamente'})


# Ruta para eliminar un estrategia
@app.route('/api/estrategia/<int:ID_Estrategia>', methods=['DELETE'])
def eliminar_estrategia(ID_Estrategia):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM estrategia WHERE id = %s", (ID_Estrategia,))
    mysql.connection.commit()
    cur.close()

    return jsonify({'mensaje': 'Estrategia eliminado correctamente'})


# Ruta para  inserter diferente estilo
@app.route('/api/dif_estilo', methods=['POST'])
def diferente_estilo():
    data = request.get_json()
    ID_Estilo = data['ID_Estilo']
    ID_Usuario = data['ID_Usuario']

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO ejercicio (ID_Estilo, ID_Usuario) VALUES (%s, %s)", (ID_Estilo, ID_Usuario))
    mysql.connection.commit()
    cur.close()

    return jsonify({'mensaje': 'Diferente estilo de aprendizaje seleccionado correctamente'})


if __name__ == '__main__':
    app.run(debug=True)
