

from http.client import HTTPSConnection, HTTPConnection, HTTPException, HTTPResponse

from typing import Callable, Dict, List, Mapping, Tuple, TypeVar
from typing import Callable, Mapping, TypeVar

from urllib.parse import urlencode
from quickcli import httpconst as httpcli


IT = TypeVar('IT')
OT = TypeVar('OT')

MapToBytes = Callable[[IT], bytes]
"""
def MapToBytes(data:IT)->bytes
"""

MapBytesTo = Callable[[bytes, str, str], OT]
"""
def MapBytesTo(body:bytes,conttype:str,charset:str)->OT
"""


class HttpReqData:
    Alias = TypeVar('Alias', bound='HttpReqData')

    method: str
    path: str
    queries: Mapping[str, List[str]]

    headers: Mapping[str, str]
    body: IT
    convert: MapToBytes

    def __init__(self) -> None:
        pass

    def request(self, method: str, path: str, queries: Mapping[str, List[str]]) -> Alias:
        self.method = method
        self.path = path
        self.queries = queries
        return self

    def send(self, headers: Mapping[str, str], body: IT, converter: MapToBytes) -> Alias:
        self.headers = headers
        self.body = body
        self.convert = converter
        return self
    pass


class HttpRespData:
    def __init__(self, statuscode: int, headers: Mapping[str, str], rawbody: bytes) -> None:
        self.code: int = statuscode
        self.headerEntir: Mapping[str, str] = headers
        self.rawbody: bytes = rawbody
        self.decodedbytes: bytes = None

    def statuscode(self) -> int:
        return self.code

    def headers(self) -> Dict[str, str]:
        return self.headerEntir

    def location(self) -> str:
        return self.headerEntir.get(httpcli.HTTP_HEADER_LOCATION, None)

    def ContentLanguage(self) -> str:
        return self.headerEntir.get(httpcli.HTTP_HEADER_CONTENTLANGUAGE, None)

    def contentlength(self) -> int:
        leng: str = self.headerEntir.get(
            httpcli.HTTP_HEADER_CONTENTLENGTH, "-1")
        return int(leng)

    def contentencoding(self) -> str:
        return self.headerEntir.get(httpcli.HTTP_HEADER_CONTENTENCODING, None)

    def contenttype(self) -> List[str]:
        conttype: str = httpcli.MIMETYPE_TEXT_PLAIN
        contcharset: str = "utf-8"

        type_charset = self.headerEntir.get(
            httpcli.HTTP_HEADER_CONTENTTYPE, "{}; charset=utf-8".format(httpcli.MIMETYPE_TEXT_PLAIN))

        type_charset = type_charset.lower()

        arr: List[str] = type_charset.split(";")
        conttype = arr[0]
        contcharset = arr[1].split("=")[1]
        return [conttype, contcharset]

    def acceptranges(self) -> str:
        return self.headerEntir.get(httpcli.HTTP_HEADER_ACCEPTRANGES, None)

    def contentrange(self) -> Tuple[str, int, int, int]:
        # Content-Range: <unit> <range-start>-<range-end>/<size>
        # Content-Range: <unit> <range-start>-<range-end>/*
        # Content-Range: <unit> */<size>
        unit: str = "bytes"
        begin: str = "0"
        end: str = "0"
        size: str = "-1"

        rangedesc: str = self.headerEntir.get(
            httpcli.HTTP_HEADER_CONTENTRANGE, "bytes 0-0/*")

        arr: List[str] = rangedesc.split(" ")
        unit = arr[0]

        arr = arr[1].split("/")
        size = -1 if arr[1] == "*" else arr[1]

        (begin, end) = tuple(
            "0", size) if arr[0] == "*" else tuple(arr[0].split("-")[:2])

        return (unit, int(begin), int(end), int(size))

    def cookie(self) -> Dict[str, str]:
        cookie: str = self.headerEntir.get(httpcli.HTTP_HEADER_SETCOOKIE, None)
        if cookie is None:
            return None
        arr: List[str] = cookie.split(";")

        ret: Dict[str, str] = dict()
        for seg in arr:
            kv: List[str] = seg.strip().split("=")
            ret[kv[0]] = kv[1]
        return ret

    def rawbody(self) -> bytes:
        return self.rawbody

    def decodedbody(self) -> bytes:
        if self.decodedbytes is not None:
            return self.decodedbytes

        encoding = self.headerEntir.get(
            httpcli.HTTP_HEADER_CONTENTENCODING, None)
        if not couldDecode(encoding):
            raise HTTPException(
                "not supported encoding {}".format(encoding))

        self.decodedbytes = decodeContent(encoding, self.rawbody)
        return self.decodedbytes

    def receive(self, convert: MapBytesTo) -> OT:
        body: bytes = self.decodedbody()

        type_charset = self.headerEntir.get(
            httpcli.HTTP_HEADER_CONTENTTYPE, None)

        conttype: str = httpcli.MIMETYPE_TEXT_PLAIN
        contcharset: str = "utf-8"

        r: bool = True
        while r:
            if type_charset is None or type_charset == "":
                break

            type_charset = type_charset.lower()
            if type_charset.find(";") == -1:
                conttype = type_charset
                break

            arr: List[str] = type_charset.split(";")
            conttype = arr[0]
            contcharset = arr[1].split("=")[1]
            r = False

        return convert(body, conttype, contcharset)


class HttpConn:

    HTTPCONN = TypeVar('HTTPCONN', HTTPSConnection, HTTPConnection)

    rawconn: HTTPCONN
    schema: str
    host: str
    port: str

    def __init__(self, rawConn: HTTPCONN,
                 schema: str, host: str, port: int) -> None:
        self.rawconn = rawConn
        self.schema = schema
        self.host = host
        self.port = port


def newHttpConnection(schema: str, host: str, port: int,
                      key_file: str = None, cert_file: str = None) -> HttpConn:
    conn: HTTPConnection = None

    if schema.lower() == httpcli.HTTPS:
        conn = HTTPSConnection(
            host=host, port=port, key_file=key_file, cert_file=cert_file)
    else:
        conn = HTTPConnection(host=host, port=port)

    return HttpConn(conn, schema, host, port)


def doRequest(conn: HttpConn, req: HttpReqData) -> HttpRespData:

    url: List[str] = []
    url.append(req.path)

    while(True):
        if req.queries is None:
            break
        if len(req.queries) == 0:
            break
        url.append(urlencode(req.queries, doseq=True))

    conn.rawconn.request(method=req.method.upper(), url="?".join(url),
                         body=req.convert(
                             req.body) if req.body is not None else None,
                         headers=req.headers)
    resp: HTTPResponse = conn.rawconn.getresponse()

    respData: HttpRespData = HttpRespData(
        resp.status, resp.headers, resp.read())
    return respData


def couldDecode(encoding: str) -> bool:
    if encoding is None or encoding == httpcli.ENCODING_NONE:
        return True

    if encoding.lower() == httpcli.ENCODING_DEFLATE:
        return True

    if encoding.lower() == httpcli.ENCODING_GZIP:
        return True

    if encoding.lower == httpcli.ENCODING_BR:
        return True

    return False


def decodeContent(encoding: str,  raw: bytes) -> bytes:
    if encoding is None or encoding == httpcli.ENCODING_NONE:
        return raw

    if encoding.lower() == httpcli.ENCODING_DEFLATE:
        import zlib
        return zlib.decompress(raw)
    if encoding.lower() == httpcli.ENCODING_GZIP:
        import gzip
        return gzip.decompress(raw)

    if encoding.lower == httpcli.ENCODING_BR:
        import brotli
        cont = brotli.decompress(raw)

    return None
