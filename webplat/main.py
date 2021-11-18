#!/usr/bin/python3

from wsgiref.simple_server import make_server
from servlet import httpheader, httpresponse


from servlet.httprequest import HttpRequest
from servlet.httpresponse import HttpResponse
from servlet.httpresponse import Render
from servlet.webappliction import WebApplication

app = WebApplication()


@app.formatresponse(httpresponse.htmlrender)
@app.requestmapping('/index/*', 'get')
def helloworld(http_request: HttpRequest, http_response: HttpResponse):
    path = http_request.getpath()
    body = '<h1>Hello, %s!</h1>' % (path)
    http_response.responsex(httpheader.HTTP_STATUSCODE_200, body)


if __name__ == "__main__":

    httpd = make_server('', 8000, app)
    print('Serving HTTP on port 8000...')
    # 开始监听HTTP请求:
    httpd.serve_forever()
    pass
