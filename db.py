import os

import mysql.connector
from dotenv import load_dotenv


load_dotenv()


def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("MYSQLHOST", "localhost"),
        user=os.getenv("MYSQLUSER", "root"),
        password=os.getenv("MYSQLPASSWORD", ""),
        database=os.getenv("MYSQLDATABASE", "Project_Progra2"),
        port=int(os.getenv("MYSQLPORT", "3306")),
        ssl_disabled=True,
    )
