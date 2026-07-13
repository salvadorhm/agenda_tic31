import web

urls = (
    '/', 'controllers.index.Index',
    '/lista_contactos','controllers.contactos.lista_contactos.ListaContactos',
    '/ver_contacto/(.*)','controllers.contactos.ver_contacto.VerContacto',
    '/editar_contacto/(.*)','controllers.contactos.editar_contacto.EditarContacto',
    '/borrar_contacto/(.*)','controllers.contactos.borrar_contacto.BorrarContacto',
)
app = web.application(urls, globals())

if __name__ == "__main__":
    web.config.debug = False
    app.run()
