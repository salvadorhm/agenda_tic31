import web

render = web.template.render('views')

class Index:
    def GET(self):
        return render.index()
