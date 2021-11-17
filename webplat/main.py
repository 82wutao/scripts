#!/usr/bin/python3

from wsgiref.simple_server import make_server


from servlet.httprequest import HttpRequest
from servlet.httpresponse import HttpResponse
from servlet.httpresponse import Render
from servlet.webappliction import WebApplication


def urlmapping(url: str, method: str = '*'):
    # regis mapping to webapp pattern
    def proxy(func):
        def wrapper(*args, **keywords):
            print("before................")
            func(*args, **keywords)
        return wrapper
    return proxy


def typemapping(renderfunc: Render):
    def proxy(func):
        def wrapper(*args, **keywords):
            # inject func to response object
            print("before................")
            func(*args, **keywords)
        return wrapper
    return proxy


def logwrap(func):
    def wrapper(*args, **keywords):
        print("before................")
        func(*args, **keywords)
        pass
    return wrapper


@logwrap
def helloworld(http_request: HttpRequest, http_response: HttpResponse):
    path = http_request.getpath()
    body = '<h1>Hello, %s!</h1>' % (path)
    http_response.response(body, '200 OK')


if __name__ == "__main__":
    app = WebApplication()
    app.mapurl("/index", helloworld, "GET")
    app.mapurl("/index/*", helloworld, "GET")

    httpd = make_server('', 8000, app)
    print('Serving HTTP on port 8000...')
    # 开始监听HTTP请求:
    httpd.serve_forever()
    pass
