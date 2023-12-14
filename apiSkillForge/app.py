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
@app.route('/api/usuarios/<int:usuario_id>', methods=['GET'])
def obtener_usuario(usuario_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM usuarios WHERE id = %s", (usuario_id,))
    data = cur.fetchone()
    cur.close()
    return jsonify(data)


# Ruta para crear un nuevo usuario
@app.route('/api/usuarios', methods=['POST'])
def crear_usuario():
    data = request.get_json()
    nombre = data['nombre']
    email = data['email']

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO usuarios (nombre, email) VALUES (%s, %s)", (nombre, email))
    mysql.connection.commit()
    cur.close()

    return jsonify({'mensaje': 'Usuario creado correctamente'})


# Ruta para actualizar un usuario
@app.route('/api/usuarios/<int:usuario_id>', methods=['PUT'])
def actualizar_usuario(usuario_id):
    data = request.get_json()
    nombre = data['nombre']
    email = data['email']

    cur = mysql.connection.cursor()
    cur.execute("UPDATE usuarios SET nombre = %s, email = %s WHERE id = %s", (nombre, email, usuario_id))
    mysql.connection.commit()
    cur.close()

    return jsonify({'mensaje': 'Usuario actualizado correctamente'})


# Ruta para eliminar un usuario
@app.route('/api/usuarios/<int:usuario_id>', methods=['DELETE'])
def eliminar_usuario(usuario_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM usuarios WHERE id = %s", (usuario_id,))
    mysql.connection.commit()
    cur.close()

    return jsonify({'mensaje': 'Usuario eliminado correctamente'})


if __name__ == '__main__':
    app.run(debug=True)
