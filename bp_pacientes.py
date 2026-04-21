from flask import Blueprint, redirect, render_template, request, url_for

from base import db
from models import Paciente


bp_pacientes = Blueprint("pacientes", __name__, url_prefix="/pacientes")


@bp_pacientes.route("/")
def index():
    lista_pacientes = Paciente.query.order_by(Paciente.Codigo.desc()).all()
    return render_template("pacientes/index.html", lista_pacientes=lista_pacientes)


@bp_pacientes.route("/agregar", methods=["GET", "POST"])
def agregar():
    if request.method == "POST":
        nuevo_paciente = Paciente(
            Identidad=request.form["Identidad"],
            Nombre=request.form["Nombre"],
            Apellido=request.form["Apellido"],
            Fecha=request.form["Fecha"],
            Telefono=request.form["Telefono"],
            Correo=request.form["Correo"],
            Direccion=request.form["Direccion"],
        )
        db.session.add(nuevo_paciente)
        db.session.commit()
        return redirect(url_for("pacientes.index"))

    return render_template("pacientes/agregar.html")


@bp_pacientes.route("/editar/<int:codigo>", methods=["GET", "POST"])
def editar(codigo):
    paciente = Paciente.query.get_or_404(codigo)

    if request.method == "POST":
        paciente.Identidad = request.form["Identidad"]
        paciente.Nombre = request.form["Nombre"]
        paciente.Apellido = request.form["Apellido"]
        paciente.Fecha = request.form["Fecha"]
        paciente.Telefono = request.form["Telefono"]
        paciente.Correo = request.form["Correo"]
        paciente.Direccion = request.form["Direccion"]

        db.session.commit()
        return redirect(url_for("pacientes.index"))

    return render_template("pacientes/editar.html", paciente=paciente)


@bp_pacientes.route("/eliminar/<int:codigo>", methods=["GET", "POST"])
def eliminar(codigo):
    paciente = Paciente.query.get_or_404(codigo)

    if request.method == "POST":
        db.session.delete(paciente)
        db.session.commit()
        return redirect(url_for("pacientes.index"))

    return render_template("pacientes/eliminar.html", paciente=paciente)
