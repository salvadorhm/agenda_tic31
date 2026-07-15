import web
import sqlite3

render = web.template.render("views/contactos", base="layout")


class EditarContacto:

    def actualizarContacto(self, contacto: dict) -> bool:
        try:
            conexion = sqlite3.connect("sql/agenda.db")
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()

            id_contacto = contacto["id_contacto"]
            nombre = contacto["nombre"]
            primer_apellido = contacto["primer_apellido"]
            segundo_apellido = contacto["segundo_apellido"]
            email = contacto["email"]
            telefono = contacto["telefono"]

            query = """UPDATE contactos 
                SET nombre = ?,
                primer_apellido = ?,
                segundo_apellido = ?,
                email = ?,
                telefono = ?
                WHERE id_contacto = ?;
                """
            datos = (
                nombre,
                primer_apellido,
                segundo_apellido,
                email,
                telefono,
                id_contacto,
            )
            cursor.execute(query, datos)
            conexion.commit()
            return True
        except sqlite3.Error as error:
            print(f"ERROR EditarContacto 200: {error.args}")
            return False
        except Exception as error:
            print(f"ERROR EditarContacto 201: {error.args}")
            return False
        finally:
            if conexion:
                conexion.close()

    def buscarContacto(self, id_contacto: int):
        try:
            conexion = sqlite3.connect("sql/agenda.db")
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()
            query = "SELECT * FROM contactos WHERE id_contacto = ?"
            cursor.execute(query, (id_contacto,))
            resultado = cursor.fetchone()

            contacto = {
                "id_contacto": resultado[0],
                "nombre": resultado[1],
                "primer_apellido": resultado[2],
                "segundo_apellido": resultado[3],
                "email": resultado[4],
                "telefono": resultado[5],
            }
            print(contacto)
            return contacto
        except sqlite3.Error as error:
            print(f"ERROR EditarContacto 202: {error.args}")
            return {}
        except Exception as error:
            print(f"ERROR EditarContacto 203: {error.args}")
            return {}
        finally:
            if conexion:
                conexion.close()

    def GET(self, id_contacto: int):
        try:
            print(f"ID_CONTACTO: {id_contacto}")
            contacto = self.buscarContacto(id_contacto)
            return render.editar_contacto(contacto) # type: ignore
        except Exception as error:
            print(f"ERROR EditarContacto 204: {error.args}")
            return f"UPS, algo fallo"

    def POST(self, id_contacto: int):
        try:
            formulario = web.input()
            contacto = {
                "id_contacto": formulario["id_contacto"],
                "nombre": formulario["nombre"],
                "primer_apellido": formulario["primer_apellido"],
                "segundo_apellido": formulario["segundo_apellido"],
                "email": formulario["email"],
                "telefono": formulario["telefono"],
            }
            resultado = self.actualizarContacto(contacto)
            web.ctx.status = "303 See Other"
            web.header("Location", "/lista_contactos")
            return ""
        except Exception as error:
            print(f"ERROR EditarContacto 205: {error.args}")
            return f"UPS, algo fallo"
