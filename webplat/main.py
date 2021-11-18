#!/usr/bin/python3

from re import I
from wsgiref.simple_server import make_server
from servlet import httpheader, httpresponse


from servlet.httprequest import HttpRequest
from servlet.httpresponse import HttpResponse
from servlet.httpresponse import Render
from servlet.webappliction import WebApplication

app = WebApplication()


@app.requestmapping('/hello/*', 'get')
@app.formatresponse(httpresponse.htmlrender)
def helloworld(http_request: HttpRequest, http_response: HttpResponse):
    path = http_request.getpath()
    body = '<h1>Hello, %s!</h1>' % (path)
    http_response.responsex(httpheader.HTTP_STATUSCODE_200, body)


@app.requestmapping('/index/*', 'get')
@app.formatresponse(httpresponse.jinjastemplaterender)
def helloworld2(http_request: HttpRequest, http_response: HttpResponse):
    other_args = dict()
    other_args['WORKDIR'] = "./"
    other_args['TEMPLATESDIR'] = "resource/template"
    other_args['name'] = 'python3'
    http_response.responsex(httpheader.HTTP_STATUSCODE_200,
                            "hello.tpl", **other_args)


if __name__ == "__main__":

    httpd = make_server('', 8000, app)
    print('Serving HTTP on port 8000...')
    # 开始监听HTTP请求:
    httpd.serve_forever()
    pass
