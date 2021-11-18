
from typing import Any, Callable, List
import re

from .httprequest import HttpRequest
from .httpresponse import HttpResponse
from .httpheader import *
from servlet import httpheader

from servlet import httpresponse


class WebApplication(object):

    def __init__(self) -> None:
        super().__init__()
        self.services = dict()

    def mapurl(self, url_pattern: str,
               run: Callable[[HttpRequest, HttpResponse], None], method: str = "*"):
        regexp = re.compile(url_pattern)
        url_services = self.services.get(regexp, list())
        url_services.append((method, run))
        self.services[regexp] = url_services
        pass

    def requestmapping(self, url: str, method: str = '*'):
        def proxy(func):
            def wrapper(req: HttpRequest, resp: HttpResponse):
                func(req, resp)
            self.mapurl(url_pattern=url, run=wrapper, method=method)
            return wrapper
        return proxy

    def formatresponse(self, renderfunc: httpresponse. Render):
        def proxy(func):
            def wrapper(req: HttpRequest, resp: HttpResponse):
                resp.setrender(renderfunc)
                func(req, resp)
            return wrapper
        return proxy

    def __call__(self, usgi_env: dict,
                 start_response: Callable[[str, List, object], Any]) -> Any:
        path = usgi_env["PATH_INFO"]
        method = usgi_env["REQUEST_METHOD"].upper()

        status_code = None
        header_list = []
        resp_cont = None

        runs = None
        for exp, services in self.services.items():
            m = exp.match(path)
            if m is None:
                continue

            runs = services
            break

        if runs is None:
            status_code = '404 Not Found Resource'
            header_list.append(
                (HTTP_HEADER_CONTENTTYPE, HTTP_MEMITYPE_HTML))
            resp_cont = "Resource has gone"
            start_response(status_code, header_list)
            return [resp_cont.encode("utf8")]

        run = None
        for s in runs:
            if s[0] == '*':
                run = s[1]
                break
            if method != s[0].upper():
                continue
            run = s[1]
            break

        if run is None:
            status_code = '405 Method Not Allowed'
            header_list.append(
                (HTTP_HEADER_CONTENTTYPE, HTTP_MEMITYPE_HTML))
            resp_cont = "Method Not Allowed"
            start_response(status_code, header_list)
            return [resp_cont.encode("utf8")]

        # try:
        req = HttpRequest(usgi_env)
        resp = HttpResponse()
        run(req, resp)
        status_code = resp.getstatuscode()
        # TODO is redirect or rewrite
        resp.render()
        header_list = resp.getheaders()
        resp_cont = resp.getcontentrendered()
        # except:
        #    status_code = '500 SErver error'
        #    header_list.append(
        #        (httpheader.HTTP_HEADER_CONTENTTYPE, "text/html;charset=UTF-8"))
        #    resp_cont = 'Server Inner Error'
        #    pass
        status = httpheader.statusline(status_code)
        start_response(status, header_list)
        return resp_cont
