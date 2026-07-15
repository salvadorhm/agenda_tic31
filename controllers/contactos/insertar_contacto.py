import web
import sqlite3

render = web.template.render('views/contactos', base='layout')

class InsertarContacto:

    def guardarContacto(self, contacto: dict) -> bool:
        try:
            conexion = sqlite3.connect("sql/agenda.db")
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()

            nombre = contacto["nombre"]
            primer_apellido = contacto["primer_apellido"]
            segundo_apellido = contacto["segundo_apellido"]
            email = contacto["email"]
            telefono = contacto["telefono"]

            query = """
                INSERT INTO contactos(
                    nombre,
                    primer_apellido,
                    segundo_apellido,
                    email,
                    telefono
                ) VALUES (?,?,?,?,?);
                """
            datos = (
                nombre,
                primer_apellido,
                segundo_apellido,
                email,
                telefono,
            )
            cursor.execute(query,datos)
            conexion.commit()
            return True
        except sqlite3.Error as error:
            print(f"ERROR InsertarContacto 300: {error.args}")
            return False
        except Exception as error:
            print(f"ERROR InsertarContacto 301: {error.args}")
            return False
        finally:
            if conexion:
                conexion.close()


    def GET(self):
        try:
            return render.insertar_contacto() # type: ignore
        except Exception as error:
            print(f"ERROR InsertarContacto 302: {error.args}")
            return f"UPS, algo fallo"

    def POST(self):
        try:
            formulario = web.input()
            contacto = {
                "nombre" : formulario['nombre'],
                "primer_apellido" : formulario['primer_apellido'],
                "segundo_apellido" : formulario['segundo_apellido'],
                "email" : formulario['email'],
                "telefono" : formulario['telefono']
            }
            resultado = self.guardarContacto(contacto)
            web.ctx.status = '303 See Other'
            web.header('Location', '/lista_contactos')
            return ''
        except Exception as error:
            print(f"ERROR InsertarContacto 303: {error.args}")
            return f"UPS, algo fallo"
