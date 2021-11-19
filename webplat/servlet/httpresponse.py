
from typing import Any, Callable, Dict

from servlet import webcontext

from . import httpheader
from . import renders


class HttpResponse(object):

    status_code: int = None
    header_dict = dict()

    content: Any = None
    other = dict()
    rewrite_path: str = None

    renderfunc: renders.Render = None
    contentrendered: bytes = None

    def __init__(self) -> None:
        super().__init__()

    def responsex(self, status_code: int, content: Any, **other_args) -> None:
        self.status_code = status_code
        self.content = content
        self.other = other_args
        pass

    def setrender(self, r: renders.Render) -> None:
        self.renderfunc = r
        pass

    def redirect(self, url: str, status_code: int = httpheader.HTTP_STATUSCODE_301):
        # Location: http: // www.example.org/index.asp
        self.status_code = status_code
        self.header_dict[httpheader.HTTP_HEADER_LOCATION] = url
        pass

    def rewrite(self, path: str):
        self.rewrite_path = path
        pass

    def getstatuscode(self) -> int:
        return self.status_code

    def getcontent(self) -> Any:
        return self.content

    def getcontentrendered(self) -> bytes:
        return self.contentrendered

    def getheaders(self) -> list:
        return [(k, v) for k, v in self.header_dict.items()]

    def setstatuscode(self, status: int):
        self.status_code = status

    def setcontent(self, cont: Any):
        self.content = cont

    def setcontenttype(self, conttype: str) -> None:
        self.header_dict[httpheader.HTTP_HEADER_CONTENTTYPE] = conttype

    def addheader(self, header: str, value: str):
        self.header_dict[header] = value

    def render(self, webctx: webcontext.WebContext):
        if self.renderfunc is None:
            self.renderfunc = renders.htmlrender

        self.contentrendered = self.renderfunc(
            self.content, self.other, self.header_dict, webctx)
