import web
import sqlite3

render = web.template.render('views', base='layout')

class VerContacto:

    def GET(self,id_contacto:int):
        print(f"ID_CONTACTO: {id_contacto}")
        return render.ver_contacto()
