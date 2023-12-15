from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

# Configuración de la base de datos
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'skillforge'
}

# Conexión a la base de datos
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()


# Ruta para obtener todos los elementos
@app.route('/api/usuarios', methods=['GET'])
def get_usuarios():
    cursor.execute('SELECT * FROM usuarios')
    result = cursor.fetchall()
    elementos = [{'ID_Usuario': row[0], 'Nombre': row[1], 'ID_Estilo': row[2]} for row in result]
    return jsonify({'elementos': elementos})


# Ruta para obtener un usuario por ID
@app.route('/api/usuarios/<int:ID_Usuario>', methods=['GET'])
def obtener_usuario(ID_Usuario):
    cursor.execute("SELECT * FROM usuarios WHERE ID_Usuario = %s", (ID_Usuario,))
    result = cursor.fetchone()
    if result:
        elemento = {'ID_Usuario': result[0], 'Nombre': result[1], 'ID_Estilo': result[2]}
        return jsonify({'elemento': elemento})
    else:
        return jsonify({'message': 'Elemento no encontrado'}), 404


# Ruta para agregar un usuario
@app.route('/api/usuarios', methods=['POST'])
def add_usuario():
    nuevo_usuario = request.get_json()
    Nombre = nuevo_usuario.get('Nombre')
    ID_Estilo = nuevo_usuario.get('ID_Estilo')

    cursor.execute('INSERT INTO usuarios (Nombre, ID_Estilo) VALUES (%s, %s)', (Nombre, ID_Estilo))
    conn.commit()

    return jsonify({'message': 'Aprendizaje agregado a usuario correctamente'}), 201

"""
#Eliminar aprendizaje de usuario
@app.route('/api/usuarios/<int:ID_Estilo>', methods=['DELETE'])
def delete_usuario(ID_Estilo):
    cursor.execute('DELETE FROM usuarios WHERE ID_Estilo = %s', (ID_Estilo,))
    conn.commit()

    return jsonify({'message': 'Estilo de usuario eliminado correctamente'})
"""

#Actualizar aprendizaje
@app.route('/api/usuarios/<int:ID_Usuario>', methods=['PUT'])
def update_usuario(ID_Usuario):
    usuario_actualizado = request.get_json()
    ID_Estilo = usuario_actualizado.get('ID_Estilo')

    cursor.execute('UPDATE usuarios SET  ID_Estilo = %s WHERE ID_Usuario = %s', (ID_Estilo, ID_Usuario))
    conn.commit()

    return jsonify({'message': 'Estilo  de usuario actualizado correctamente'})


# Ruta para inserter nuevo consejo
@app.route('/api/consejo', methods=['POST'])
def add_consejo():
    nuevo_consejo = request.get_json()
    ID_Estilo = nuevo_consejo.get('ID_Estilo')
    Consejo = nuevo_consejo.get("Consejo")

    cursor.execute('INSERT INTO consejo (ID_Estilo, Consejo) VALUES (%s, %s)', (ID_Estilo, Consejo))
    conn.commit()

    return jsonify({'message': 'Consejo agregado correctamente'}), 201


# Ruta para obtener todos los consejos
@app.route('/api/consejo', methods=['GET'])
def get_consejos():
    cursor.execute('SELECT * FROM consejo')
    result = cursor.fetchall()
    elementos = [{'ID_Consejo': row[0], 'ID_Estilo': row[1], 'Consejo': row[2]} for row in result]
    return jsonify({'elementos': elementos})


#Eliminar consejo
@app.route('/api/consejo/<int:ID_Consejo>', methods=['DELETE'])
def delete_consejo(ID_Consejo):
    cursor.execute('DELETE FROM consejo WHERE ID_Consejo = %s', (ID_Consejo,))
    conn.commit()

    return jsonify({'message': 'Estilo de usuario eliminado correctamente'})


# Ruta para inserter nuevo ejercicio
@app.route('/api/ejercicio', methods=['POST'])
def add_ejercicio():
    nuevo_ejercicio = request.get_json()
    ID_Estilo = nuevo_ejercicio.get('ID_Estilo')
    Ejercicios = nuevo_ejercicio.get("Ejercicios")

    cursor.execute('INSERT INTO ejercicio (ID_Estilo, Ejercicios) VALUES (%s, %s)', (ID_Estilo, Ejercicios))
    conn.commit()

    return jsonify({'message': 'Ejercicio agregado correctamente'}), 201


# Ruta para obtener todos los Ejercicios
@app.route('/api/ejercicio', methods=['GET'])
def get_ejercicios():
    cursor.execute('SELECT * FROM ejercicio')
    result = cursor.fetchall()
    elementos = [{'ID_Ejercicio': row[0], 'ID_Estilo': row[1], 'Ejercicios': row[2]} for row in result]
    return jsonify({'elementos': elementos})


#Eliminar Ejercicios
@app.route('/api/ejercicio/<int:ID_Ejercicio>', methods=['DELETE'])
def delete_ejercicio(ID_Ejercicio):
    cursor.execute('DELETE FROM ejercicio WHERE ID_Ejercicio = %s', (ID_Ejercicio,))
    conn.commit()

    return jsonify({'message': 'Estilo de usuario eliminado correctamente'})


# Ruta para inserter nuevo estrategia
@app.route('/api/estrategia', methods=['POST'])
def add_estrategia():
    nuevo_estrategia = request.get_json()
    ID_Estilo = nuevo_estrategia.get('ID_Estilo')
    Estrategias = nuevo_estrategia.get("Estrategias")

    cursor.execute('INSERT INTO ejercicio (ID_Estilo, Estrategias) VALUES (%s, %s)', (ID_Estilo, Estrategias))
    conn.commit()

    return jsonify({'message': 'Estrategia agregado correctamente'}), 201


# Ruta para obtener todos los Ejercicios
@app.route('/api/estrategia', methods=['GET'])
def get_estrategias():
    cursor.execute('SELECT * FROM ejercicio')
    result = cursor.fetchall()
    elementos = [{'ID_Estrategia': row[0], 'ID_Estilo': row[1], 'Estrategias': row[2]} for row in result]
    return jsonify({'elementos': elementos})



#Eliminar Estrategias
@app.route('/api/estrategia/<int:ID_Estrategia>', methods=['DELETE'])
def delete_estrategia(ID_Estrategia):
    cursor.execute('DELETE FROM estrategia WHERE ID_Estrategia = %s', (ID_Estrategia,))
    conn.commit()

    return jsonify({'message': 'Estilo de usuario eliminado correctamente'})


# Ruta para  inserter diferente estilo
@app.route('/api/userdifest', methods=['POST'])
def add_userdifest():
    nuevo_difestilo = request.get_json()
    ID_Estilo = nuevo_difestilo.get('ID_Estilo')
    ID_Usuario = nuevo_difestilo.get("ID_Usuario")

    cursor.execute('INSERT INTO userdifest (ID_Usuario, ID_Estilo) VALUES (%s, %s)', (ID_Usuario, ID_Estilo))
    conn.commit()

    return jsonify({'message': 'Diferente estilo agregado correctamente'}), 201


#Eliminar diferente estilo
@app.route('/api/userdifest/<int:ID_difest>', methods=['DELETE'])
def delete_difestilo(ID_difest):
    cursor.execute('DELETE FROM userdifest WHERE ID_difest = %s', (ID_difest,))
    conn.commit()

    return jsonify({'message': 'Estilo de usuario eliminado correctamente'})


if __name__ == '__main__':
    app.run(debug=True)
