
from bilirecommend.up import newup
from servlet import http, httprequest, httpresponse, renders
from servlet.webappliction import WebApplication


def route(app: WebApplication):

    @app.requestmapping("/bilibili/up/new", http.HTTP_METHOD_POST, renders.htmlrender)
    def _newup(req: httprequest.HttpRequest, resp: httpresponse.HttpResponse):
        newup(req, resp)
    pass
