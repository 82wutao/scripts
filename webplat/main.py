#!/usr/bin/python3

from re import I
from wsgiref.simple_server import make_server
from servlet import httpheader, httpresponse, webcontext
from os import path


from servlet.httprequest import HttpRequest
from servlet.httpresponse import HttpResponse
from servlet.webappliction import WebApplication
from servlet import renders

app = WebApplication()


@app.requestmapping('/hello/*', 'get')
@app.formatresponse(renders.htmlrender)
def helloworld(http_request: HttpRequest, http_response: HttpResponse):
    path = http_request.getpath()
    body = '<h1>Hello, %s!</h1>' % (path)
    http_response.responsex(httpheader.HTTP_STATUSCODE_200, body)


@app.requestmapping('/index/*', 'get')
@app.formatresponse(renders.jinjastemplaterender)
def helloworld2(http_request: HttpRequest, http_response: HttpResponse):
    other_args = dict()
    other_args['name'] = 'python3'
    http_response.responsex(httpheader.HTTP_STATUSCODE_200,
                            "hello.tpl", **other_args)


if __name__ == "__main__":
   #:w
   #  os.path.dirname(os.path.realpath(__file__)) = /home/wutao/code/scripts/webplat
    main_path = path.realpath(__file__)
    work_dir = path.dirname(main_path)

    other_setting = dict()
    other_setting[webcontext.WEBCTX_RESPONSE_ENCODING_KEY] = webcontext.WEBCTX_RESPONSE_ENCODING_UTF8

    webctx = webcontext.WebContext(
        work_dir, "resource", "resource/template", **other_setting)
    app.setwebcontext(webctx)

    httpd = make_server('', 8000, app)
    print('Serving HTTP on port 8000...')
    # 开始监听HTTP请求:
    httpd.serve_forever()
    pass
