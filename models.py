from base import db


class Paciente(db.Model):
    __tablename__ = "pacientes"

    Codigo = db.Column(db.Integer, primary_key=True)
    Identidad = db.Column(db.String(100))
    Nombre = db.Column(db.String(100))
    Apellido = db.Column(db.String(100))
    Fecha = db.Column(db.String(100))
    Correo = db.Column(db.String(100))
    Telefono = db.Column(db.String(20))
    Direccion = db.Column(db.String(255))

    def __repr__(self):
        return f"<Paciente {self.Identidad}>"
