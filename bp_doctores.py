from flask import Blueprint, redirect, render_template, request, url_for

from db import get_db_connection


bp_doctores = Blueprint("doctores", __name__, url_prefix="/doctores")


@bp_doctores.route("/")
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM doctores ORDER BY Codigo DESC")
    lista_doctores = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("doctores/index.html", lista_doctores=lista_doctores)


@bp_doctores.route("/agregar", methods=["GET", "POST"])
def agregar():
    if request.method == "POST":
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO doctores (Nombre, Apellido, Especialidad, Licencia, Telefono, Correo)
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (
                request.form["Nombre"],
                request.form["Apellido"],
                request.form["Especialidad"],
                request.form["Licencia"],
                request.form["Telefono"],
                request.form["Correo"],
            ),
        )
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for("doctores.index"))

    return render_template("doctores/agregar.html")


@bp_doctores.route("/editar/<int:codigo>", methods=["GET", "POST"])
def editar(codigo):
    conn = get_db_connection()

    if request.method == "POST":
        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE doctores
            SET Nombre = %s, Apellido = %s, Especialidad = %s,
                Licencia = %s, Telefono = %s, Correo = %s
            WHERE Codigo = %s
            """,
            (
                request.form["Nombre"],
                request.form["Apellido"],
                request.form["Especialidad"],
                request.form["Licencia"],
                request.form["Telefono"],
                request.form["Correo"],
                codigo,
            ),
        )
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for("doctores.index"))

    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM doctores WHERE Codigo = %s", (codigo,))
    doctor = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template("doctores/editar.html", doctor=doctor)


@bp_doctores.route("/eliminar/<int:codigo>", methods=["GET", "POST"])
def eliminar(codigo):
    conn = get_db_connection()

    if request.method == "POST":
        cursor = conn.cursor()
        cursor.execute("DELETE FROM doctores WHERE Codigo = %s", (codigo,))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for("doctores.index"))

    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM doctores WHERE Codigo = %s", (codigo,))
    doctor = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template("doctores/eliminar.html", doctor=doctor)
