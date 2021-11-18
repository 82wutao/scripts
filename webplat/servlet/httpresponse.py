
from abc import ABC, ABCMeta
from abc import abstractmethod
from typing import Any, Callable, Dict

from . import httpheader


# /book/{id:int} get
# query=>reflact=>paramclass
# form=>reflact=>paramclass
# response content-type


Render = Callable[[Any, Dict, Dict], bytes]

__RESPONSE_ENCODING_KEY = "ENCODING"
__RESPONSE_ENCODING_UTF8 = "UTF-8"
__TEMPLATES_DIR_KEY = "TEMPLATESDIR"
__TEMPLATES_DIR_DEFAULT = "templates"
__WORK_DIR_KEY = "WORKDIR"
__WORK_DIR_DEFAULT = "./"


def htmlrender(content: Any, other: Dict, headers: Dict) -> bytes:
    '''
    content as html snippets
    '''
    snippets = str(content)
    encoding = other.get(__RESPONSE_ENCODING_KEY, __RESPONSE_ENCODING_UTF8)
    headers[httpheader.HTTP_HEADER_CONTENTTYPE] = '%s; charset=%s' % (
        httpheader.HTTP_MEMITYPE_HTML, encoding)
    return [snippets.encode(encoding)]


def jinjasnippetsrender(content: Any, other: Dict, headers: Dict) -> bytes:
    '''
    content as jinja snippets
    '''
    from jinja2 import Template

    snippets = str(content)
    tpl: Template = Template(snippets)
    out = tpl.render(**other)

    encoding = other.get(__RESPONSE_ENCODING_KEY, __RESPONSE_ENCODING_UTF8)
    headers[httpheader.HTTP_HEADER_CONTENTTYPE] = '%s; charset=%s' % (
        httpheader.HTTP_MEMITYPE_HTML, encoding)
    return [out.encode(encoding)]


def jinjastemplaterender(content: Any, other: Dict, headers: Dict) -> bytes:
    '''
    content as jinja template file
    '''
    from os import path
    from jinja2 import Template
    from jinja2 import Environment, FileSystemLoader

    template_file = str(content)

    root_dir = other.get(__WORK_DIR_KEY, __WORK_DIR_DEFAULT)
    template_dir = other.get(__TEMPLATES_DIR_KEY, __TEMPLATES_DIR_DEFAULT)

    t_loader = FileSystemLoader(path.join(root_dir, template_dir))
    env = Environment(loader=t_loader)

    tpl: Template = env.get_template(template_file)
    out = tpl.render(**other)

    encoding = other.get(__RESPONSE_ENCODING_KEY, __RESPONSE_ENCODING_UTF8)
    headers[httpheader.HTTP_HEADER_CONTENTTYPE] = '%s; charset=%s' % (
        httpheader.HTTP_MEMITYPE_HTML, encoding)
    return [out.encode(encoding)]


def jsonrender(content: Any, other: Dict, headers: Dict) -> bytes:
    '''
    content as object dump to jsonstr
    '''
    import json

    out: str = json.dumps(content)
    encoding = other.get(__RESPONSE_ENCODING_KEY, __RESPONSE_ENCODING_UTF8)
    headers[httpheader.HTTP_HEADER_CONTENTTYPE] = '%s' % (
        httpheader.HTTP_MEMITYPE_JSON, encoding)
    return [out.encode(encoding)]


def filerender(content: Any, other: Dict, headers: Dict) -> bytes:
    '''
    content as file path
    '''
    from os import path

    file_path: str = str(content)
    file_size = path.getsize(filename=file_path)
    bs: bytes = []

    with open(file=file_path, mode='rb') as fd:
        bs = fd.read(file_size)

    cont_tp: str = headers.get(httpheader.HTTP_HEADER_CONTENTTYPE, None)
    if cont_tp is not None:
        return bs

    headers[httpheader.HTTP_HEADER_CONTENTTYPE] = '%s' % (
        httpheader.HTTP_MEMITYPE_OCTET_STREAM)
    return bs


def bytesender(content: Any, other: Dict, headers: Dict) -> bytes:
    '''
    content as bytes
    '''
    bs: bytes = bytes(content)
    cont_tp: str = headers.get(httpheader.HTTP_HEADER_CONTENTTYPE, None)
    if cont_tp is not None:
        return bs

    headers[httpheader.HTTP_HEADER_CONTENTTYPE] = '%s' % (
        httpheader.HTTP_MEMITYPE_OCTET_STREAM)
    return bs


class HttpResponse(object):

    status_code: int = None
    header_dict = dict()

    content: Any = None
    other = dict()
    rewrite_path: str = None

    renderfunc: Render = None
    contentrendered: bytes = None

    def __init__(self) -> None:
        super().__init__()

    def responsex(self, status_code: int, content: Any, **other_args) -> None:
        self.status_code = status_code
        self.content = content
        self.other = other_args
        pass

    def setrender(self, r: Render) -> None:
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

    def addheader(self, header: str, value: str):
        self.header_dict[header] = value

    def render(self):
        if self.renderfunc is None:
            self.renderfunc = htmlrender

        self.contentrendered = self.renderfunc(
            self.content, self.other, self.header_dict)
