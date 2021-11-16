
from abc import ABC, ABCMeta
from abc import abstractmethod
from typing import Any, Dict

from . import httpheader


# /book/{id:int} get
# query=>reflact=>paramclass
# form=>reflact=>paramclass
# response content-type

class HttpResponse(ABC):

    status_code = None
    header_dict = dict()
    content = None
    other = dict()
    rewrite_path = None

    def __init__(self) -> None:
        super().__init__()

    # def response(self, content, status: str = '200 OK', content_type: str = "text/html;charset=UTF-8"):
    #    self.status_code = status
    #    self.cont = content
    #    self.header_dict[httpheader.HTTP_HEADER_CONTENTTYPE] = content_type
    #    pass

    # responsex(200,"OK","<div>hello world</div>") html snippets
    # responsex(200,"OK","template_path",data="$data"[,name="$name"]) template
    # responsex(200,"OK",obj) obj=>json
    # responsex(200,"OK",obj) obj=>xml
    # responsex(200,"OK","file_path") file => octect stream
    # responsex(200,"OK",[]byte) bytes=> octect stream
    def responsex(self, status_code: int, content: Any, **other_args):
        self.status_code = status_code
        self.content = content
        self.other = other_args
        pass

    def redirect(self, url: str, status_code: int = httpheader.HTTP_STATUSCODE_301):
        # Location: http: // www.example.org/index.asp
        pass

    def rewrite(self, path: str):
        self.rewrite_path = path
        pass

    def getstatuscode(self) -> str:
        return self.status_code

    def getcontent(self) -> str:
        return self.cont

    def getheaders(self) -> list:
        return [(k, v) for k, v in self.header_dict.items()]

    def setstatuscode(self, status: str):
        self.status_code = status

    def setcontent(self, content: str):
        self.cont = content

    def addheader(self, header: str, value: str):
        self.header_dict[header] = value

    @abstractmethod
    def render(self):
        # code = ?
        # content = > bytes
        # content-type seted,charset ,encoding
        pass
