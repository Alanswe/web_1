import sqlite3
import os

BASE_DATOS = os.path.join(os.path.dirname(__file__),'personas.db') # en sqlite, una base de datos es un fichero

creacion = """
        create table persona(
            id integer primary key autoincrement,
            nombre text,
            apellidos text,
            dni text)
"""
def crear_db(): #esto siempre se tiene que hacer con un TRY
    cnx = sqlite3.connect(BASE_DATOS)
    cnx.execute(creacion)
    cnx.close()#cerrar siempre la consulta

crear_db()
