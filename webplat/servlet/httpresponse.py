
from . import httpheader


class HttpResponse(object):

    status_code = None
    header_dict = dict()
    cont = None

    def __init__(self) -> None:
        super().__init__()

    def response(self, content, status: str = '200 OK', content_type: str = "text/html;charset=UTF-8"):
        self.status_code = status
        self.cont = content
        self.header_dict[httpheader.HTTP_HEADER_CONTENTTYPE] = content_type
        pass

    def statuscode(self) -> str:
        return self.status_code

    def content(self) -> str:
        return self.cont

    def headers(self) -> list:
        return [(k, v) for k, v in self.header_dict.items()]

    def setstatuscode(self, status: str):
        self.status_code = status

    def setcontent(self, content: str):
        self.cont = content

    def addheader(self, header: str, value: str):
        self.header_dict[header] = value
