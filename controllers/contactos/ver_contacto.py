import web
import sqlite3

render = web.template.render('views/contactos', base='layout')

class VerContacto:

    def buscarContacto(self, id_contacto:int):
        try:
            conexion = sqlite3.connect("sql/agenda.db")
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()
            query = "SELECT * FROM contactos WHERE id_contacto = ?"
            cursor.execute(query,(id_contacto,))
            resultado = cursor.fetchone()

            contacto = {
                "id_contacto":resultado[0],
                "nombre":resultado[1],
                "primer_apellido":resultado[2],
                "segundo_apellido":resultado[3],
                "email":resultado[4],
                "telefono":resultado[5]
            }
            conexion.close()
            print(contacto)
            return contacto
        except sqlite3.Error as error:
            print(f"ERROR VerContacto 500: {error.args}")
            return {}
        except Exception as error:
            print(f"ERROR VerContacto 501: {error.args}")
            return {}

    def GET(self,id_contacto:int):
        try:
            print(f"ID_CONTACTO: {id_contacto}")
            contacto = self.buscarContacto(id_contacto)
            return render.ver_contacto(contacto) # type: ignore
        except Exception as error:
            print(f"ERROR VerContacto 502: {error.args}")
            return f"UPS, algo fallo"
