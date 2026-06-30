import web

urls = (
    '/', 'controllers.index.Index',
    '/lista_contactos','controllers.lista_contactos.ListaContactos',
    '/ver_contacto/(.*)','controllers.ver_contacto.VerContacto'
)
app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()