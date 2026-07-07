import web
import sqlite3

render = web.template.render('views', base='layout')

class InsertarContactos:


    def GET(self):
        return render.insertar_contactos()
