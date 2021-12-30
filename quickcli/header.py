
from typing import Dict, Mapping, TypeVar


###################
header_request_host: str = ""
header_request_accept_mime: str = ""
header_request_accept_charset: str = ""
header_request_accept_features: str = ""
header_request_accept_encoding: str = ""
header_request_accept_language: str = ""
header_request_useragent: str = ""
header_request_cookie: str = ""

header_request_CORS_origin: str = ""
header_request_CORS_method: str = ""
header_request_CORS_headers: str = ""


#################################
header_response_server: str = ""
# "bytes|none"
header_response_accept_ranges: str = ""
header_response_setcookie: str = ""
header_response_setcookie2: str = ""
header_response_Vary: str = ""

header_response_CORS_allow_origin: str = ""
header_response_CORS_allow_methods: str = ""
heade_responser_CORS_allow_headers: str = ""
header_response_CORS_allow_credentials: str = ""
header_response_CORS_maxage: str = ""
header_response_CORS_exposeheaders: str = ""

######################################
# Date、Cache-Control 或 Connection。
header_generic_date: str = ""
header_generic_cachectrl: str = ""
header_generic_connection: str = ""
header_generic_KeepAlive: str = ""

##########################################
# 实体报头包括 Content-Length、Content-Language、Content-Encoding、Content-Type 和 Expires
header_entity_expires: str = ""
header_entity_contentlocation: str = ""
header_entity_contentsecuritypolicy: str = ""
header_entity_contentrange: str = ""
header_entity_contentlength: str = ""
header_entity_contentmd5: str = ""
header_entity_contentencoding: str = ""
header_entity_contenttype: str = ""
header_entity_contentlanguage: str = ""


"""
Range: <unit>=<range-start>-
Range: <unit>=<range-start>-<range-end>
Range: <unit>=<range-start>-<range-end>, <range-start>-<range-end>
Range: <unit>=<range-start>-<range-end>, <range-start>-<range-end>, <range-start>-<range-end>
Range: <unit>=-<suffix-length>

消息头 	描述 	更多信息 	标准
 

 
Age
Allow
Alternates 		HTTP Content Negotiation 	RFC 2295, §8.3
Authorization 	包含用服务器验证用户代理的凭证
 

 
DNT 	设置该值为1， 表明用户明确退出任何形式的网上跟踪。 	Supported by Firefox 4, Firefox 5 for mobile, IE9, and a few major companies. 	Tracking Preference Expression(DNT)
Date
ETag 		HTTP Caching FAQ
Expect
Expires 		HTTP Caching FAQ
From
 
If-Match
If-Modified-Since 		HTTP Caching FAQ
If-None-Match 		HTTP Caching FAQ
If-Range
If-Unmodified-Since
Last-Event-ID 	给出服务器在先前HTTP连接上接收的最后事件的ID。用于同步文本/事件流。 	Server-Sent Events 	Server-Sent Events spec
Last-Modified 		HTTP Caching FAQ
Link 	等同于HTML标签中的"link"，但它是在HTTP层上，给出一个与获取的资源相关的URL以及关系的种类。	For the rel = prefetch case, see Link Prefetching FAQ	           Introduced in HTTP 1.1's RFC 2068, section 19.6.2.4, it was removed in the final HTTP 1.1 spec, then reintroduced, with some extensions, in RFC 5988
Location
Max-Forwards
Negotiate 		HTTP Content Negotiation 	RFC 2295, §8.4
Origin 		HTTP Access Control and Server Side Access Control 	More recently defined in the Fetch spec(see Fetch API.) Originally defined in W3C Cross-Origin Resource Sharing
Pragma for the pragma: nocache value see HTTP Caching FAQ
Proxy-Authenticate
Proxy-Authorization
Range
Referer 	（请注意，在HTTP / 0.9规范中引入的正交错误必须在协议的后续版本中保留）
Retry-After
Sec-Websocket-Extensions 			 Websockets
Sec-Websocket-Key 			 Websockets
Sec-Websocket-Origin 			 Websockets
Sec-Websocket-Protocol 			 Websockets
Sec-Websocket-Version 			 Websockets
 
 
Strict-Transport-Security 		HTTP Strict Transport Security 	IETF reference
TCN 		HTTP Content Negotiation 	RFC 2295, §8.5
TE
Trailer 	列出将在消息正文之后在尾部块中传输的头。这允许服务器计算一些值，如Content-MD5：在传输数据时。请注意，Trailer：标头不得列出Content-Length: , Trailer：或Transfer-Encoding：headers。		RFC 2616, §14.40
Transfer-Encoding
Upgrade 
Variant-Vary 		HTTP Content Negotiation 	RFC 2295, §8.6
Vary 	列出了用作Web服务器选择特定内容的条件的标头。此服务器对于高效和正确缓存发送的资源很重要。	HTTP Content Negotiation & HTTP Caching FAQ
Via
Warning
WWW-Authenticate
X-Content-Duration 		Configuring servers for Ogg media
X-Content-Security-Policy 		Using Content Security Policy
X-DNSPrefetch-Control 		Controlling DNS prefetching
X-Frame-Options 		The XFrame-Option Response Header
X-Requested-With 	通常在值为“XMLHttpRequest”时使用		Not standard
"""


class HttpHeaderData:
    '''
    通用首部指的是可以应用于请求和响应中，但是不能应用于消息内容自身的 HTTP 首部\n
    请求中使用，并且和请求主体无关\n
    响应中并且和响应消息主体无关的那一类
    HTTP 消息有效载荷（即关于消息主体的元数据）的 HTTP 报头
    '''
    _type_alias = TypeVar('_type_alias', bound='HttpHeaderData')

    def __init__(self) -> None:
        self._headers: Dict[str, str] = dict()

    @staticmethod
    def wrap_headers(headers: Mapping[str, str]) -> _type_alias:
        d: HttpHeaderData._type_alias = HttpHeaderData._type_alias()
        d._headers = headers
        return d

    def generic_header(self) -> None:

        pass

    def entity_header(self) -> None:

        pass

    def request_header(self) -> None:
        #  Accept、Accept-*、 If-* 允许执行条件请求。某些请求头如：Cookie, User-Agent 和 Referer  Host
        #
        # Accept,
        # Accept-Language,
        # Content-Language,
        # Content-Type并且值是 application/x-www-form-urlencoded, multipart/form-data, 或者 text/plain之一的（忽略参数）.
        pass

    def response_header(self) -> None:
        # 像Age, Location 和 Server都属于响应头
        pass
