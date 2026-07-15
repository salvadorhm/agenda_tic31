import web
import sqlite3

render = web.template.render("views/direcciones", base="layout_direcciones")


class EditarDireccion:

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

    def actualizarDireccion(self, registro: dict) -> bool:
        try:
            conexion = sqlite3.connect("sql/agenda.db")
            cursor = conexion.cursor()
            query = """
                UPDATE direcciones
                SET
                    id_contacto = ?,
                    pais = ?,
                    estado = ?,
                    ciudad = ?,
                    colonia = ?,
                    calle = ?,
                    numero_exterior = ?
                WHERE id_direccion = ?;
            """
            datos = [
                registro["id_contacto"],
                registro["pais"],
                registro["estado"],
                registro["ciudad"],
                registro["colonia"],
                registro["calle"],
                registro["numero_exterior"],
                registro["id_direccion"],
            ]
            cursor.execute(query, datos)
            conexion.commit()
            return True
        except sqlite3.Error as error:
            print(f"ERROR EditarDireccion 102: {error.args}")
            return False
        except Exception as error:
            print(f"ERROR EditarDireccion 103: {error.args}")
            return False
        finally:
            if conexion:
                conexion.close()

    def GET(self, id_direccion):
        response = self.buscarDireccion(id_direccion)
        return render.editar_direccion(response)  # type: ignore

    def POST(self, id_direccion):
        formulario = web.input()
        registro = {
            "id_direccion": id_direccion,
            "id_contacto": formulario["id_contacto"],
            "pais": formulario["pais"],
            "estado": formulario["estado"],
            "ciudad": formulario["ciudad"],
            "colonia": formulario["colonia"],
            "calle": formulario["calle"],
            "numero_exterior": formulario["numero_exterior"],
        }
        response = self.actualizarDireccion(registro)
        web.ctx.status = '303 See Other'
        web.header('Location', f"/ver_contacto/{formulario['id_contacto']}")
        return ''
