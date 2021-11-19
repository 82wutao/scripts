
import os
from typing import Any, Callable, List
import re
from os import path

from .httprequest import HttpRequest
from .httpresponse import HttpResponse
from .httpheader import *
from . import util, httpheader, httprequest, httpresponse, webcontext, renders


class WebApplication(object):

    def __init__(self) -> None:
        super().__init__()
        self.services = dict()
        self.ctx = None

    def mapurl(self, url_pattern: str,
               run: Callable[[HttpRequest, HttpResponse], None], method: str = "*"):
        regexp = re.compile(url_pattern)
        url_services = self.services.get(regexp, list())
        url_services.append((method, run))
        self.services[regexp] = url_services
        pass

    def setwebcontext(self, ctx: webcontext.WebContext):
        self.ctx = ctx

        workdir = ctx.getworkdir()
        resourcedir = ctx.getstaticpath()
        if workdir is None:
            workdir = webcontext.WEBCTX_WORK_DIR_DEFAULT
        if resourcedir is None:
            resourcedir = webcontext.WEBCTX_RESOURCE_DIR_DEFAULT

        def _file_exists(request_path: str) -> str:
            ps = request_path.split("/static", maxsplit=1)
            if len(ps) == 1:
                return None

            file_path = util.pathjoin(workdir, '/', resourcedir, ps[1])
            if not path.exists(file_path):
                return None
            return file_path

        def _cssload(req: HttpRequest, resp: HttpResponse) -> None:
            resp.setrender(renders.filerender)

            request_path = req.getpath()
            file_path = _file_exists(request_path)
            if file_path is None:
                resp.responsex(httpheader.HTTP_STATUSCODE_404, None)
                return

            resp.setcontenttype(httpheader.MIMETYPE_TEXT_CSS)
            resp.responsex(httpheader.HTTP_STATUSCODE_200, file_path)
            pass

        def _octetstreamload(req: HttpRequest, resp: HttpResponse) -> None:
            resp.setrender(renders.filerender)

            request_path = req.getpath()
            file_path = _file_exists(request_path)
            if file_path is None:
                resp.responsex(httpheader.HTTP_STATUSCODE_404, None)
                return

            resp.setcontenttype(httpheader.MIMETYPE_APPLICATION_OCTET_STREAM)
            resp.responsex(httpheader.HTTP_STATUSCODE_200, file_path)
            pass

        def _imgload(req: HttpRequest, resp: HttpResponse) -> None:
            resp.setrender(renders.filerender)

            request_path = req.getpath()
            file_path = _file_exists(request_path)
            if file_path is None:
                resp.responsex(httpheader.HTTP_STATUSCODE_404, None)
                return

            ext = file_path.split(".", maxsplit=1)
            resp.setcontenttype("image/"+ext)
            resp.responsex(httpheader.HTTP_STATUSCODE_200, file_path)
            pass

        def _jsload(req: HttpRequest, resp: HttpResponse) -> None:
            resp.setrender(renders.filerender)

            request_path = req.getpath()
            file_path = _file_exists(request_path)
            if file_path is None:
                resp.responsex(httpheader.HTTP_STATUSCODE_404, None)
                return

            resp.setcontenttype(httpheader.MIMETYPE_TEXT_JAVASCRIPT)
            resp.responsex(httpheader.HTTP_STATUSCODE_200, file_path)
            pass

        self.mapurl("/static/js/*", _jsload, 'get')
        self.mapurl("/static/css/*", _cssload, 'get')
        self.mapurl("/static/img/*", _imgload, 'get')
        self.mapurl("/static/font/*", _octetstreamload, 'get')
        #self.mapurl("/static/av/*", _resourceload, 'get')

    def requestmapping(self, url: str, method: str = '*'):
        def proxy(func):
            def wrapper(req: HttpRequest, resp: HttpResponse):
                func(req, resp)
            self.mapurl(url_pattern=url, run=wrapper, method=method)
            return wrapper
        return proxy

    def formatresponse(self, renderfunc: renders.Render):
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
                (HTTP_HEADER_CONTENTTYPE, MIMETYPE_TEXT_HTML))
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
                (HTTP_HEADER_CONTENTTYPE, MIMETYPE_TEXT_HTML))
            resp_cont = "Method Not Allowed"
            start_response(status_code, header_list)
            return [resp_cont.encode("utf8")]

        # try:
        req = HttpRequest(usgi_env)
        resp = HttpResponse()
        run(req, resp)
        status_code = resp.getstatuscode()
        # TODO is redirect or rewrite
        resp.render(self.ctx)
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
