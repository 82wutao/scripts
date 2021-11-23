
from servlet import http as httplet
from typing import Callable, Dict
from http import client
from urllib import parse

HandleCallback = Callable[[int, str, Dict[str, str], bytes], None]


def https_get(host: str, port: int, path: str, query: Dict[str, str], headers: Dict[str, str], handle: HandleCallback):
    conn = client.HTTPSConnection(host, port)
    params = parse.urlencode(query)
    url = path+'?'+params
    conn.request(httplet.HTTP_METHOD_GET, url, headers=headers)

    resp: client.HTTPResponse = conn.getresponse()
    handle(resp.status, resp.reason, resp.headers, resp.read())
    conn.close()
