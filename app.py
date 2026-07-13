import web

urls = (
    '/', 'controllers.index.Index',

    # Rutas para el modulo contactos
    '/lista_contactos','controllers.contactos.lista_contactos.ListaContactos',
    '/insertar_contacto','controllers.contactos.insertar_contacto.InsertarContacto',
    '/ver_contacto/(.*)','controllers.contactos.ver_contacto.VerContacto',
    '/editar_contacto/(.*)','controllers.contactos.editar_contacto.EditarContacto',
    '/borrar_contacto/(.*)','controllers.contactos.borrar_contacto.BorrarContacto',

    # Rutas del modulo de direcciones
    '/ver_direccion/(.*)', 'controllers.direcciones.ver_direccion.VerDireccion',
    '/editar_direccion/(.*)', 'controllers.direcciones.editar_direccion.EditarDireccion',
    '/borrar_direccion/(.*)', 'controllers.direcciones.borrar_direccion.BorrarDireccion',
    '/insertar_direccion/(.*)', 'controllers.direcciones.insertar_direccion.InsertarDireccion'
)
app = web.application(urls, globals())

if __name__ == "__main__":
    web.config.debug = False
    app.run()
