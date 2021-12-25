#!/usr/bin/python3

# from os import path
# from re import I
# from wsgiref.simple_server import make_server
# import bilirecommend
# from servlet import http, httpresponse, webcontext
# from servlet import httprequest
#
#
# from servlet.httprequest import HttpRequest
# from servlet.httpresponse import HttpResponse
# from servlet.webappliction import WebApplication
# from servlet import renders
#
# app = WebApplication()
#
#
# @app.requestmapping('/hello/*', 'get', renders.htmlrender)
# def helloworld(http_request: HttpRequest, http_response: HttpResponse):
#     request_path = http_request.getpath()
#     body = '<h1>Hello, %s!</h1>' % (request_path)
#     http_response.responsex(http.HTTP_STATUSCODE_200, body)
#
#
# @app.requestmapping('/index/*', 'get', renders.jinjastemplaterender)
# def helloworld2(http_request: HttpRequest, http_response: HttpResponse):
#     other_args = dict()
#     other_args['name'] = 'python3'
#     http_response.responsex(http.HTTP_STATUSCODE_200,
#                             "hello.tpl", **other_args)
#
#
# class Student(object):
#     def __init__(self) -> None:
#         super().__init__()
#         self.name: str = "的的嘎嘎wutao"
#         self.age: int = 99
#
#
# @app.requestmapping('/json/*', 'get', renders.jsonrender)
# def helloworld12(http_request: HttpRequest, http_response: HttpResponse):
#     s = Student()
#
#     http_response.responsex(http.HTTP_STATUSCODE_200, s)
#
#
# @app.requestmapping('/method/get', 'get', renders.htmlrender)
# def helloworld11(http_request: HttpRequest, http_response: HttpResponse):
#     query = http_request.getquery()
#     param = httprequest.query_as_form_urlencoded(query)
#
#     snippets = '<h1>%s</h1>' % (param['hello'])
#     http_response.responsex(http.HTTP_STATUSCODE_200, snippets)
#
#
# @app.requestmapping('/method/post', "post", renders.htmlrender)
# def helloworld3(http_request: HttpRequest, http_response: HttpResponse):
#     io_handle = http_request.getbody()
#     param = httprequest.body_as_form_urlencoded(
#         io_handle, http_request.getcontentlength())
#
#     snippets = '<h1>%s</h1>' % (param['age'])
#     http_response.responsex(http.HTTP_STATUSCODE_200, snippets)
#
#
# if __name__ == "__main__":
#    #:w
#    #  os.path.dirname(os.path.realpath(__file__)) = /home/wutao/code/scripts/webplat
#     main_path = path.realpath(__file__)
#     work_dir = path.dirname(main_path)
#
#     other_setting = dict()
#     other_setting[webcontext.WEBCTX_RESPONSE_ENCODING_KEY] = webcontext.WEBCTX_RESPONSE_ENCODING_UTF8
#
#     webctx = webcontext.WebContext(
#         work_dir, "resource", "resource/template", **other_setting)
#     app.setwebcontext(webctx)
#
#     bilirecommend.route(app)
#
#     httpd = make_server('', 8000, app)
#     print('Serving HTTP on port 8000...')
#     # 开始监听HTTP请求:
#     httpd.serve_forever()
#     pass
from quickcli.client import HttpReqData, doRequest, newHttpConnection
from quickcli import httpconst


headers = {}
headers['Host'] = 'www.runoob.com'
headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0'
headers['Accept'] = 'text/html, application/xhtml+xml, application/xml; q= 0.9, image/avif, image/webp, */*; q = 0.8'
headers['Accept-Language'] = 'zh-CN, zh; q = 0.8, zh-TW; q = 0.7, zh-HK; q = 0.5, en-US; q = 0.3, en; q = 0.2'
headers['Accept-Encoding'] = 'gzip, deflate, br'
headers['Connection'] = 'keep-alive'
headers['Upgrade-Insecure-Requests'] = '1'
headers['Sec-Fetch-Dest'] = 'document'
headers['Sec-Fetch-Mode'] = 'navigate'
headers['Sec-Fetch-Site'] = 'same-origin'
headers['Sec-Fetch-User'] = '?1'
req = HttpReqData().request(httpconst.METHOD_GET,
                            '/python3/python3-function.html', None).send(headers, None, None)
conn = newHttpConnection(
    httpconst.HTTPS, "www.runoob.com", httpconst.HTTPSPORT)
resp = doRequest(conn, req)


def mapfunc(body, contty,  charset: bytes) -> str:
    return body.decode(charset)


print(resp.receive(mapfunc))
conn.rawconn.close()
