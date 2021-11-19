

from typing import Any, Callable, Dict
from . import webcontext
from . import http

Render = Callable[[Any, Dict, Dict, webcontext.WebContext], bytes]


def htmlrender(content: Any, other: Dict, headers: Dict, webctx: webcontext.WebContext) -> bytes:
    '''
    content as html snippets
    '''
    encoding = webctx.getotherattr(webcontext.WEBCTX_RESPONSE_ENCODING_KEY)
    if encoding is None:
        encoding = webcontext.WEBCTX_RESPONSE_ENCODING_UTF8

    headers[http.HTTP_HEADER_CONTENTTYPE] = '%s; charset=%s' % (
        http.MIMETYPE_TEXT_HTML, encoding)

    snippets = str(content)
    return [snippets.encode(encoding)]


def jinjasnippetsrender(content: Any, other: Dict, headers: Dict, webctx: webcontext.WebContext) -> bytes:
    '''
    content as jinja snippets
    '''
    from jinja2 import Template

    snippets = str(content)
    tpl: Template = Template(snippets)
    out = tpl.render(**other)

    encoding = webctx.getotherattr(webcontext.WEBCTX_RESPONSE_ENCODING_KEY)
    if encoding is None:
        encoding = webcontext.WEBCTX_RESPONSE_ENCODING_UTF8

    headers[http.HTTP_HEADER_CONTENTTYPE] = '%s; charset=%s' % (
        http.MIMETYPE_TEXT_HTML, encoding)
    return [out.encode(encoding)]


def jinjastemplaterender(content: Any, other: Dict, headers: Dict, webctx: webcontext.WebContext) -> bytes:
    '''
    content as jinja template file
    '''
    from os import path
    from jinja2 import Template
    from jinja2 import Environment, FileSystemLoader

    template_file = str(content)

    work_dir = webctx.getworkdir()
    if work_dir is None:
        work_dir = webcontext.WEBCTX_WORK_DIR_DEFAULT
    template_dir = webctx.gettemplatedir()
    if template_dir is None:
        template_dir = webcontext.WEBCTX_TEMPLATES_DIR_DEFAULT

    t_loader = FileSystemLoader(path.join(work_dir, template_dir))
    env = Environment(loader=t_loader)

    tpl: Template = env.get_template(template_file)
    out = tpl.render(**other)

    encoding = webctx.getotherattr(webcontext.WEBCTX_RESPONSE_ENCODING_KEY)
    if encoding is None:
        encoding = webcontext.WEBCTX_RESPONSE_ENCODING_UTF8

    headers[http.HTTP_HEADER_CONTENTTYPE] = '%s; charset=%s' % (
        http.MIMETYPE_TEXT_HTML, encoding)
    return [out.encode(encoding)]


def jsonrender(content: Any, other: Dict, headers: Dict, webctx: webcontext.WebContext) -> bytes:
    '''
    content as object dump to jsonstr
    '''
    import json

    out: str = json.dumps(content,
                          ensure_ascii=False, default=lambda o: o.__dict__)

    encoding = webctx.getotherattr(webcontext.WEBCTX_RESPONSE_ENCODING_KEY)
    if encoding is None:
        encoding = webcontext.WEBCTX_RESPONSE_ENCODING_UTF8
    headers[http.HTTP_HEADER_CONTENTTYPE] = '%s' % (
        http.MIMETYPE_APPLICATION_JSON)

    return [out.encode(encoding)]


def filerender(content: Any, other: Dict, headers: Dict, webctx: webcontext.WebContext) -> bytes:
    '''
    content as file path
    '''
    from os import path

    file_path: str = str(content)
    file_size = path.getsize(filename=file_path)
    bs: bytes = []

    with open(file=file_path, mode='rb') as fd:
        bs = fd.read(file_size)
    print(type(bs))

    assert type(bs) is bytes,  "assert fail in filerender"

    cont_tp: str = headers.get(http.HTTP_HEADER_CONTENTTYPE, None)
    if cont_tp is not None:
        return [bs]

    headers[http.HTTP_HEADER_CONTENTTYPE] = '%s' % (
        http.MIMETYPE_APPLICATION_OCTET_STREAM)
    return [bs]


def bytesender(content: Any, other: Dict, headers: Dict, webctx: webcontext.WebContext) -> bytes:
    '''
    content as bytes
    '''
    bs: bytes = bytes(content)
    cont_tp: str = headers.get(http.HTTP_HEADER_CONTENTTYPE, None)
    if cont_tp is not None:
        return bs

    headers[http.HTTP_HEADER_CONTENTTYPE] = '%s' % (
        http.MIMETYPE_APPLICATION_OCTET_STREAM)
    return bs
