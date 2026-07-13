import web
import sqlite3

render = web.template.render("views/direcciones", base="layout_direcciones")

class VerDireccion:

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
            print(f"ERROR ModelDirecciones buscar: {error.args}")
            return {}
        except Exception as error:
            print(f"ERROR ModelDirecciones buscar: {error.args}")
            return {}
        finally:
            if 'conn' in locals() and conn:
                conn.close()

    def GET(self, id_direccion):
        response = self.buscarDireccion(id_direccion)
        return render.ver_direccion(response)  # type: ignore