import os
from urllib.parse import quote_plus

from dotenv import load_dotenv
from flask import Flask, render_template

from base import db
from bp_doctores import bp_doctores
from bp_pacientes import bp_pacientes


load_dotenv()


def create_app():
    app = Flask(__name__)

    mysql_user = os.getenv("MYSQLUSER", "root")
    mysql_password = quote_plus(os.getenv("MYSQLPASSWORD", ""))
    mysql_host = os.getenv("MYSQLHOST", "localhost")
    mysql_port = os.getenv("MYSQLPORT", "3306")
    mysql_database = os.getenv("MYSQLDATABASE", "Project_Progra2")

    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"mysql+mysqlconnector://{mysql_user}:{mysql_password}"
        f"@{mysql_host}:{mysql_port}/{mysql_database}"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    app.register_blueprint(bp_pacientes)
    app.register_blueprint(bp_doctores)

    @app.route("/")
    def index():
        return render_template("index.html")

    return app


app = create_app()


if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.run(debug=True)
