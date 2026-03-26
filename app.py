from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Función para conectar a la BD
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='Project_Progra2',
        ssl_disabled=True
    )

@app.route("/")
def index():
    return render_template('index.html')

# ======================= CRUD PACIENTES =======================

@app.route("/pacientes/")
def pacientes_index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM pacientes")
    datos = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('pacientes/index.html', lista_pacientes=datos)

@app.route("/pacientes/agregar", methods=["GET", "POST"])
def pacientes_agregar():
    if request.method == 'POST':
        conn = get_db_connection()
        cursor = conn.cursor()
        identidad = request.form['Identidad']
        nombre = request.form['Nombre']
        apellido = request.form['Apellido']
        fecha =  request.form['Fecha']
        telefono = request.form['Telefono']
        correo = request.form['Correo']
        direccion = request.form['Direccion']
        cursor.execute("INSERT INTO pacientes (Identidad, Nombre, Apellido, Fecha, Telefono, Correo, Direccion) VALUES (%s, %s, %s, %s, %s, %s, %s)", 
                       (identidad, nombre, apellido, fecha, telefono, correo, direccion))
        conn.commit()
        conn.close()
        return redirect(url_for('pacientes_index'))
    return render_template('pacientes/agregar.html')

@app.route("/pacientes/editar/<string:codigo>", methods=["GET", "POST"])
def pacientes_editar(codigo):
    conn = get_db_connection()
    if request.method == 'GET':
        cur = conn.cursor()
        cur.execute("SELECT * FROM pacientes WHERE Codigo = %s", (codigo,))
        paciente = cur.fetchone()
        conn.close()
        return render_template('pacientes/editar.html', paciente=paciente)
    elif request.method == 'POST':
        cursor = conn.cursor()
        identidad = request.form['Identidad']
        nombre = request.form['Nombre']
        apellido = request.form['Apellido']
        fecha =  request.form['Fecha']
        telefono = request.form['Telefono']
        correo = request.form['Correo']
        direccion = request.form['Direcciom']
        cursor.execute("UPDATE pacientes SET Identidad=%s, Nombre=%s, Apellido=%s, Fecha=%s, Telefono=%s, Correo=%s, Direccion=%s WHERE Codigo=%s", 
                       (identidad, nombre, apellido, fecha, telefono, correo, direccion, codigo))
        conn.commit()
        conn.close()
        return redirect(url_for('pacientes_index'))

@app.route("/pacientes/eliminar/<string:codigo>", methods=["GET", "POST"])
def pacientes_eliminar(codigo):
    conn = get_db_connection()
    if request.method == 'GET':
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM pacientes WHERE Codigo = %s", (codigo,))
        paciente = cursor.fetchone()
        conn.close()
        return render_template('pacientes/eliminar.html', paciente=paciente)
    elif request.method == 'POST':
        cursor = conn.cursor()
        cursor.execute("DELETE FROM pacientes WHERE Codigo = %s", (codigo,))
        conn.commit()
        conn.close()
        return redirect(url_for('pacientes_index'))

# ======================= CRUD DOCTORES =======================

@app.route("/doctores/")
def doctores_index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM doctores")
    datos = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('doctores/index.html', lista_doctores=datos)

@app.route("/doctores/agregar", methods=["GET", "POST"])
def doctores_agregar():
    if request.method == 'POST':
        conn = get_db_connection()
        cursor = conn.cursor()
        nombre = request.form['Nombre']
        apellido = request.form['Apellido']
        especialidad = request.form['Especialidad']
        licencia = request.form['Licencia']
        telefono = request.form['Telefono']
        correo = request.form['Correo']
        cursor.execute("INSERT INTO doctores (Nombre, Apellido, Especialidad, Licencia, Telefono, Correo) VALUES (%s, %s, %s, %s, %s, %s)", 
                       (nombre, apellido, especialidad, licencia, telefono, correo))
        conn.commit()
        conn.close()
        return redirect(url_for('doctores_index'))
    return render_template('doctores/agregar.html')

@app.route("/doctores/editar/<string:codigo>", methods=["GET", "POST"])
def doctores_editar(codigo):
    conn = get_db_connection()
    if request.method == 'GET':
        cur = conn.cursor()
        cur.execute("SELECT * FROM doctores WHERE Codigo = %s", (codigo,))
        doctor = cur.fetchone()
        conn.close()
        return render_template('doctores/editar.html', doctor=doctor)
    elif request.method == 'POST':
        cursor = conn.cursor()
        nombre = request.form['Nombre']
        apellido = request.form['Apellido']
        especialidad = request.form['Especialidad']
        licencia = request.form['Licencia']
        telefono = request.form['Telefono']
        correo = request.form['Correo']
        cursor.execute("UPDATE doctores SET Nombre=%s, Apellido=%s, Especialidad=%s, Licencia=%s, Telefono=%s, Correo=%s,WHERE Codigo=%s", 
                       (nombre, apellido, especialidad, licencia, telefono, correo, codigo))
        conn.commit()
        conn.close()
        return redirect(url_for('doctores_index'))

@app.route("/doctores/eliminar/<string:codigo>", methods=["GET", "POST"])
def doctores_eliminar(codigo):
    conn = get_db_connection()
    if request.method == 'GET':
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM doctores WHERE Codigo = %s", (codigo,))
        doctor = cursor.fetchone()
        conn.close()
        return render_template('doctores/eliminar.html', doctor=doctor)
    elif request.method == 'POST':
        cursor = conn.cursor()
        cursor.execute("DELETE FROM doctores WHERE Codigo = %s", (codigo,))
        conn.commit()
        conn.close()
        return redirect(url_for('doctores_index'))

if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)