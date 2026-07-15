import web
import sqlite3

render = web.template.render("views/direcciones", base="layout_direcciones")

class InsertarDireccion:

    def insertarDireccion(self, registro: dict) -> bool:
        try:
            conn = sqlite3.connect("sql/agenda.db")
            cursor = conn.cursor()
            cursor.execute("PRAGMA foreign_keys = ON;")
            query = """
                INSERT INTO direcciones (
                    id_contacto,
                    pais,
                    estado,
                    ciudad,
                    colonia,
                    calle,
                    numero_exterior
                )
                VALUES (?, ?, ?, ?, ?, ?, ?);
            """
            datos = [
                registro['id_contacto'],
                registro['pais'],
                registro['estado'],
                registro['ciudad'],
                registro['colonia'],
                registro['calle'],
                registro['numero_exterior']
            ]
            cursor.execute(query, datos)
            conn.commit()
            return True
        except sqlite3.Error as error:
            print(f"ERROR InsertarDireccion 100: {error.args}")
            return False
        except Exception as error:
            print(f"ERROR InsertarDireccion 101: {error.args}")
            return False
        finally:
            if 'conn' in locals() and conn:
                conn.close()


    def GET(self,id_contacto:int):
        return render.insertar_direccion(id_contacto)  # type: ignore

    def POST(self,id_contacto:int):
        formulario = web.input()
        registro = {
            'id_contacto': formulario['id_contacto'],
            'pais': formulario['pais'],
            'estado': formulario['estado'],
            'ciudad': formulario['ciudad'],
            'colonia': formulario['colonia'],
            'calle': formulario['calle'],
            'numero_exterior': formulario['numero_exterior'],
        }
        response = self.insertarDireccion(registro)
        web.ctx.status = '303 See Other'
        web.header('Location', f"/ver_contacto/{formulario['id_contacto']}")
        return ''
