import web
import sqlite3

render = web.template.render('views', base='layout')

class ListaContactos:

    def conectar(self):
        try:
            conexion = sqlite3.connect("sql/agenda.db")
            conexion.row_factory = sqlite3.Row
            return conexion
        except Exception as error:
            print(f"ERROR 100: {error.args}")
            return None

    def listaContactos(self):
        try:
            conexion = self.conectar()
            cursor = conexion.cursor()
            sql = "SELECT * FROM contactos"
            cursor.execute(sql)
            contactos = cursor.fetchall()
            return contactos
        except Exception as error:
            print(f"ERROR 101: {error.args}")
            return None

    def GET(self):
        print(self.listaContactos())
        return render.lista_contactos()
