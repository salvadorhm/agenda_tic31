import web
import sqlite3

render = web.template.render("views/direcciones", base="layout_direcciones")

class BorrarDireccion:

    def buscarDireccion(self, id_direccion: int) -> dict:
        try:
            conexion = sqlite3.connect("sql/agenda.db")
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()
            query = "SELECT * FROM direcciones WHERE id_direccion = ?"
            cursor.execute(query, (id_direccion,))
            row = cursor.fetchone()
            if not row:
                return {}
            registro = {
                'id_direccion': row['id_direccion'],
                'id_contacto': row['id_contacto'],
                'pais': row['pais'],
                'estado': row['estado'],
                'ciudad': row['ciudad'],
                'colonia': row['colonia'],
                'calle': row['calle'],
                'numero_exterior': row['numero_exterior']
            }
            return registro
        except sqlite3.Error as error:
            print(f"ERROR BorrarDireccion 100: {error.args}")
            return {}
        except Exception as error:
            print(f"ERROR BorrarDireccion 101: {error.args}")
            return {}
        finally:
            if conexion:
                conexion.close()

    def eliminarDireccion(self, id_direccion: int) -> bool:
        try:
            conexion = sqlite3.connect("sql/agenda.db")
            cursor = conexion.cursor()
            query = "DELETE FROM direcciones WHERE id_direccion = ?"
            cursor.execute(query, (id_direccion,))
            conexion.commit()
            conexion.close()
            return True
        except sqlite3.Error as error:
            print(f"ERROR BorrarDireccion 102: {error.args}")
            return False
        except Exception as error:
            print(f"ERROR BorrarDireccion 103: {error.args}")
            return False
        finally:
            if conexion:
                conexion.close()


    def GET(self, id_direccion):
        response = self.buscarDireccion(id_direccion)
        return render.borrar_direccion(response)  # type: ignore

    def POST(self, id_direccion):
        contacto = self.buscarDireccion(id_direccion)
        response = self.eliminarDireccion(id_direccion)
        web.ctx.status = '303 See Other'
        web.header('Location', f"/ver_contacto/{contacto['id_contacto']}")
        return ''
