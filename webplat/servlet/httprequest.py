

class HttpRequest(object):

    __ENV_KEY_REQUEST_METHOD = "REQUEST_METHOD"
    __ENV_KEY_PATH_INFO = "PATH_INFO"
    __ENV_KEY_QUERY_STRING = "QUERY_STRING"
    __ENV_KEY_REMOTE_ADDR = "REMOTE_ADDR"
    __ENV_KEY_CONTENT_TYPE = "CONTENT_TYPE"
    __ENV_KEY_CONTENT_LENGTH = "CONTENT_LENGTH"
    __ENV_KEY_HTTP_HOST = "HTTP_HOST"
    __ENV_KEY_HTTP_USER_AGENT = "HTTP_USER_AGENT"
    __ENV_KEY_HTTP_ACCEPT = "HTTP_ACCEPT"
    __ENV_KEY_HTTP_ACCEPT_LANGUAGE = "HTTP_ACCEPT_LANGUAGE"
    __ENV_KEY_HTTP_ACCEPT_ENCODING = "HTTP_ACCEPT_ENCODING"
    __ENV_KEY_HTTP_CONNECTION = "HTTP_CONNECTION"
    __ENV_KEY_HTTP_COOKIE = "HTTP_COOKIE"
    __ENV_KEY_HTTP_UPGRADE_INSECURE_REQUESTS = "HTTP_UPGRADE_INSECURE_REQUESTS"
    __ENV_KEY_HTTP_SEC_FETCH_DEST = "HTTP_SEC_FETCH_DEST"
    __ENV_KEY_HTTP_SEC_FETCH_MODE = "HTTP_SEC_FETCH_MODE"
    __ENV_KEY_HTTP_SEC_FETCH_SITE = "HTTP_SEC_FETCH_SITE"
    __ENV_KEY_HTTP_SEC_FETCH_USER = "HTTP_SEC_FETCH_USER"
    __ENV_KEY_HTTP_CACHE_CONTROL = "HTTP_CACHE_CONTROL"
    __ENV_KEY_HTTP_PROTOCOL = "SERVER_PROTOCOL"
    __ENV_KEY_SERVER_NAME = "SERVER_NAME"
    __ENV_KEY_SERVER_PORT = "SERVER_PORT"
    __ENV_KEY_SERVER_SOFTWARE = "SERVER_SOFTWARE"

    # wsgi_env = None
    def __init__(self, wsgi_env) -> None:
        super().__init__()
        self.wsgi_env = wsgi_env

    def gethost(self) -> str:
        hostaddr = self.wsgi_env[HttpRequest.__ENV_KEY_HTTP_HOST]
        host = hostaddr.split(":")[0]
        return host

    def getport(self) -> int:
        port = self.wsgi_env[HttpRequest.__ENV_KEY_SERVER_PORT]
        return int(port)

    def getprotocol(self) -> str:
        return self.wsgi_env[HttpRequest.__ENV_KEY_HTTP_PROTOCOL]

    def getmethod(self) -> str:
        return self.wsgi_env[HttpRequest.__ENV_KEY_REQUEST_METHOD]

    def getpath(self) -> str:
        return self.wsgi_env[HttpRequest.__ENV_KEY_PATH_INFO]

    def getquery(self) -> str:
        return self.wsgi_env[HttpRequest.__ENV_KEY_QUERY_STRING]

    def getheader(self, key, defaultval) -> str:
        return self.wsgi_env.get(key, defaultval)

    def getheaders(self) -> dict:
        return self.wsgi_env

    def getcontenttype(self) -> str:
        return self.wsgi_env[HttpRequest.__ENV_KEY_CONTENT_TYPE]

    def getcontentlength(self) -> int:
        length = self.wsgi_env[HttpRequest.__ENV_KEY_CONTENT_LENGTH]
        return int(length)

    def getuseragent(self) -> str:
        return self.wsgi_env[HttpRequest.__ENV_KEY_HTTP_USER_AGENT]

    def getaccept(self) -> str:
        return self.wsgi_env[HttpRequest.__ENV_KEY_HTTP_ACCEPT]

    def getacceptlanguage(self) -> str:
        return self.wsgi_env[HttpRequest.__ENV_KEY_HTTP_ACCEPT_LANGUAGE]

    def getacceptencoding(self) -> str:
        return self.wsgi_env[HttpRequest.__ENV_KEY_HTTP_ACCEPT_ENCODING]

    def getcookie(self) -> str:
        return self.wsgi_env[HttpRequest.__ENV_KEY_HTTP_COOKIE]

    def getbody(self) -> bytes:
        return []


def body_as_xml(bs: bytes):
    pass


def body_as_json(bs: bytes):
    pass


def body_as_form_urlencoded(bs: bytes):
    pass


def body_as_form_multipart(bs: bytes):
    pass
