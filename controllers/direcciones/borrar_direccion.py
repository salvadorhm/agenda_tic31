import web
import sqlite3

render = web.template.render("views/direcciones", base="layout_direcciones")

class BorrarDireccion:

    def buscarDireccion(self, id_direccion: int) -> dict:
        try:
            conn = sqlite3.connect("sql/agenda.db")
            cursor = conn.cursor()
            query = "SELECT * FROM direcciones WHERE id_direccion = ?"
            cursor.execute(query, (id_direccion,))
            row = cursor.fetchone()
            if not row:
                return {}
            registro = {
                'id_direccion': row[0],
                'id_contacto': row[1],
                'pais': row[2],
                'estado': row[3],
                'ciudad': row[4],
                'colonia': row[5],
                'calle': row[6],
                'numero_exterior': row[7]
            }
            conn.close()
            return registro
        except sqlite3.Error as error:
            print(f"ERROR BorrarDireccion 100: {error.args}")
            return {}
        except Exception as error:
            print(f"ERROR BorrarDireccion 101: {error.args}")
            return {}
        finally:
            # Si algo falla cierra la conexión
            conn.close()

    def eliminarDireccion(self, id_direccion: int) -> bool:
        try:
            conn = sqlite3.connect("sql/agenda.db")
            cursor = conn.cursor()
            query = "DELETE FROM direcciones WHERE id_direccion = ?"
            cursor.execute(query, (id_direccion,))
            conn.commit()
            conn.close()
            return True
        except sqlite3.Error as error:
            print(f"ERROR BorrarDireccion 102: {error.args}")
            return False
        except Exception as error:
            print(f"ERROR BorrarDireccion 103: {error.args}")
            return False
        finally:
            conn.close()


    def GET(self, id_direccion):
        response = self.buscarDireccion(id_direccion)
        return render.borrar_direccion(response)  # type: ignore

    def POST(self, id_direccion):
        contacto = self.buscarDireccion(id_direccion)
        response = self.eliminarDireccion(id_direccion)
        web.ctx.status = '303 See Other'
        web.header('Location', f"/ver_contacto/{contacto['id_contacto']}")
        return ''
