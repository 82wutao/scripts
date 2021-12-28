# 方法请求一个指定资源的表示形式，使用GET的请求应该只被用于获取数据。
from typing import Dict


METHOD_GET: str = "GET"
# 方法请求一个与GET请求的响应相同的响应，但没有响应体。
METHOD_HEAD: str = "HEAD"
# 方法用于将实体提交到指定的资源，通常导致在服务器上的状态变化或副作用。
METHOD_POST: str = "POST"
# 方法用请求有效载荷替换目标资源的所有当前表示。
METHOD_PUT: str = "PUT"
# 方法删除指定的资源。
METHOD_DELETE: str = "DELETE"
# 方法建立一个到由目标资源标识的服务器的隧道。
METHOD_CONNECT: str = "CONNECT"
# 方法用于描述目标资源的通信选项。
METHOD_OPTIONS: str = "OPTIONS"
# 方法沿着到目标资源的路径执行一个消息环回测试。
METHOD_TRACE: str = "TRACE"
# 方法用于对资源应用部分修改。
METHOD_PATCH: str = "PATCH"


MIMETYPE_TEXT_PLAIN = "text/plain"
MIMETYPE_TEXT_HTML = "text/html"
MIMETYPE_TEXT_CSS = "text/css"
MIMETYPE_TEXT_JAVASCRIPT = "text/javascript"
# image 	表明是某种图像。不包括视频，但是动态图（比如动态gif）也使用image类型
MIMETYPE_IMAGE_GIF = "image/gif"
MIMETYPE_IMAGE_PNG = "image/png"
MIMETYPE_IMAGE_JPEG = "image/jpeg"
MIMETYPE_IMAGE_BMP = "image/bmp"
MIMETYPE_IMAGE_WEBP = "image/webp"
MIMETYPE_IMAGE_X_ICON = "image/x-icon"
MIMETYPE_IMAGE_VND_MICROSOFT_ICON = "image/vnd.microsoft.icon"
# audio 	表明是某种音频文件
MIMETYPE_AUDIO_MIDI = "audio/midi"
MIMETYPE_AUDIO_MPEG = "audio/mpeg"
MIMETYPE_AUDIO_WEBM = "audio/webm"
MIMETYPE_AUDIO_OGG = "audio/ogg"
MIMETYPE_AUDIO_WAV = "audio/wav"
MIMETYPE_AUDIO_WAVE = "audio/wave"

# video 	表明是某种视频文件
MIMETYPE_VIDEO_WEBM = "video/webm"
MIMETYPE_VIDEO_AVI = "video/avi"
MIMETYPE_VIDEO_MP4 = "video/mp4"
MIMETYPE_VIDEO_OGG = "video/ogg"
MIMETYPE_VIDEO_M3U8 = "video/m3u8"

# application 	表明是某种二进制数据
MIMETYPE_APPLICATION_OGG = "application/ogg"
MIMETYPE_APPLICATION_OCTET_STREAM = "application/octet-stream"
MIMETYPE_APPLICATION_PKCS12 = "application/pkcs12"
MIMETYPE_APPLICATION_VND_MSPOWERPOINT = "application/vnd.mspowerpoint"
MIMETYPE_APPLICATION_XHTML_XML = "application/xhtml+xml"
MIMETYPE_APPLICATION_XML = "application/xml,"
MIMETYPE_APPLICATION_PDF = "application/pdf"
MIMETYPE_APPLICATION_JSON = "application/json"

MIMETYPE_MULTIPART_FORM_DATA = "multipart/form-data"
MIMETYPE_MULTIPART_BYTERANGES = "multipart/byteranges"

_mimetypes: Dict[str, str] = dict()
_mimetypes["323"] = "text/h323"
_mimetypes["acx"] = "application/internet-property-stream"
_mimetypes["ai"] = "application/postscript"
_mimetypes["aif"] = "audio/x-aiff"
_mimetypes["aifc"] = "audio/x-aiff"
_mimetypes["aiff"] = "audio/x-aiff"
_mimetypes["asf"] = "video/x-ms-asf"
_mimetypes["asr"] = "video/x-ms-asf"
_mimetypes["asx"] = "video/x-ms-asf"
_mimetypes["au"] = "audio/basic"
_mimetypes["avi"] = "video/x-msvideo"
_mimetypes["axs"] = "application/olescript"
_mimetypes["bas"] = "text/plain"
_mimetypes["bcpio"] = "application/x-bcpio"
_mimetypes["bin"] = "application/octet-stream"
_mimetypes["bmp"] = "image/bmp"
_mimetypes["c"] = "text/plain"
_mimetypes["cat"] = "application/vnd.ms-pkiseccat"
_mimetypes["cdf"] = "application/x-cdf"
_mimetypes["cer"] = "application/x-x509-ca-cert"
_mimetypes["class"] = "application/octet-stream"
_mimetypes["clp"] = "application/x-msclip"
_mimetypes["cmx"] = "image/x-cmx"
_mimetypes["cod"] = "image/cis-cod"
_mimetypes["cpio"] = "application/x-cpio"
_mimetypes["crd"] = "application/x-mscardfile"
_mimetypes["crl"] = "application/pkix-crl"
_mimetypes["crt"] = "application/x-x509-ca-cert"
_mimetypes["csh"] = "application/x-csh"
_mimetypes["css"] = "text/css"
_mimetypes["dcr"] = "application/x-director"
_mimetypes["der"] = "application/x-x509-ca-cert"
_mimetypes["dir"] = "application/x-director"
_mimetypes["dll"] = "application/x-msdownload"
_mimetypes["dms"] = "application/octet-stream"
_mimetypes["doc"] = "application/msword"
_mimetypes["dot"] = "application/msword"
_mimetypes["dvi"] = "application/x-dvi"
_mimetypes["dxr"] = "application/x-director"
_mimetypes["eps"] = "application/postscript"
_mimetypes["etx"] = "text/x-setext"
_mimetypes["evy"] = "application/envoy"
_mimetypes["exe"] = "application/octet-stream"
_mimetypes["fif"] = "application/fractals"
_mimetypes["flr"] = "x-world/x-vrml"
_mimetypes["gif"] = "image/gif"
_mimetypes["gtar"] = "application/x-gtar"
_mimetypes["gz"] = "application/x-gzip"
_mimetypes["h"] = "text/plain"
_mimetypes["hdf"] = "application/x-hdf"
_mimetypes["hlp"] = "application/winhlp"
_mimetypes["hqx"] = "application/mac-binhex40"
_mimetypes["hta"] = "application/hta"
_mimetypes["htc"] = "text/x-component"
_mimetypes["htm"] = "text/html"
_mimetypes["html"] = "text/html"
_mimetypes["htt"] = "text/webviewhtml"
_mimetypes["ico"] = "image/x-icon"
_mimetypes["ief"] = "image/ief"
_mimetypes["iii"] = "application/x-iphone"
_mimetypes["ins"] = "application/x-internet-signup"
_mimetypes["isp"] = "application/x-internet-signup"
_mimetypes["jfif"] = "image/pipeg"
_mimetypes["jpe"] = "image/jpeg"
_mimetypes["jpeg"] = "image/jpeg"
_mimetypes["jpg"] = "image/jpeg"
_mimetypes["js"] = "application/x-javascript"
_mimetypes["latex"] = "application/x-latex"
_mimetypes["lha"] = "application/octet-stream"
_mimetypes["lsf"] = "video/x-la-asf"
_mimetypes["lsx"] = "video/x-la-asf"
_mimetypes["lzh"] = "application/octet-stream"
_mimetypes["m13"] = "application/x-msmediaview"
_mimetypes["m14"] = "application/x-msmediaview"
_mimetypes["m3u"] = "audio/x-mpegurl"
_mimetypes["man"] = "application/x-troff-man"
_mimetypes["mdb"] = "application/x-msaccess"
_mimetypes["me"] = "application/x-troff-me"
_mimetypes["mht"] = "message/rfc822"
_mimetypes["mhtml"] = "message/rfc822"
_mimetypes["mid"] = "audio/mid"
_mimetypes["mny"] = "application/x-msmoney"
_mimetypes["mov"] = "video/quicktime"
_mimetypes["movie"] = "video/x-sgi-movie"
_mimetypes["mp2"] = "video/mpeg"
_mimetypes["mp3"] = "audio/mpeg"
_mimetypes["mpa"] = "video/mpeg"
_mimetypes["mpe"] = "video/mpeg"
_mimetypes["mpeg"] = "video/mpeg"
_mimetypes["mpg"] = "video/mpeg"
_mimetypes["mpp"] = "application/vnd.ms-project"
_mimetypes["mpv2"] = "video/mpeg"
_mimetypes["ms"] = "application/x-troff-ms"
_mimetypes["mvb"] = "application/x-msmediaview"
_mimetypes["nws"] = "message/rfc822"
_mimetypes["oda"] = "application/oda"
_mimetypes["p10"] = "application/pkcs10"
_mimetypes["p12"] = "application/x-pkcs12"
_mimetypes["p7b"] = "application/x-pkcs7-certificates"
_mimetypes["p7c"] = "application/x-pkcs7-mime"
_mimetypes["p7m"] = "application/x-pkcs7-mime"
_mimetypes["p7r"] = "application/x-pkcs7-certreqresp"
_mimetypes["p7s"] = "application/x-pkcs7-signature"
_mimetypes["pbm"] = "image/x-portable-bitmap"
_mimetypes["pdf"] = "application/pdf"
_mimetypes["pfx"] = "application/x-pkcs12"
_mimetypes["pgm"] = "image/x-portable-graymap"
_mimetypes["pko"] = "application/ynd.ms-pkipko"
_mimetypes["pma"] = "application/x-perfmon"
_mimetypes["pmc"] = "application/x-perfmon"
_mimetypes["pml"] = "application/x-perfmon"
_mimetypes["pmr"] = "application/x-perfmon"
_mimetypes["pmw"] = "application/x-perfmon"
_mimetypes["pnm"] = "image/x-portable-anymap"
_mimetypes["pot"] = "application/vnd.ms-powerpoint"
_mimetypes["ppm"] = "image/x-portable-pixmap"
_mimetypes["pps"] = "application/vnd.ms-powerpoint"
_mimetypes["ppt"] = "application/vnd.ms-powerpoint"
_mimetypes["prf"] = "application/pics-rules"
_mimetypes["ps"] = "application/postscript"
_mimetypes["pub"] = "application/x-mspublisher"
_mimetypes["qt"] = "video/quicktime"
_mimetypes["ra"] = "audio/x-pn-realaudio"
_mimetypes["ram"] = "audio/x-pn-realaudio"
_mimetypes["ras"] = "image/x-cmu-raster"
_mimetypes["rgb"] = "image/x-rgb"
_mimetypes["rmi"] = "audio/mid"
_mimetypes["roff"] = "application/x-troff"
_mimetypes["rtf"] = "application/rtf"
_mimetypes["rtx"] = "text/richtext"
_mimetypes["scd"] = "application/x-msschedule"
_mimetypes["sct"] = "text/scriptlet"
_mimetypes["setpay"] = "application/set-payment-initiation"
_mimetypes["setreg"] = "application/set-registration-initiation"
_mimetypes["sh"] = "application/x-sh"
_mimetypes["shar"] = "application/x-shar"
_mimetypes["sit"] = "application/x-stuffit"
_mimetypes["snd"] = "audio/basic"
_mimetypes["spc"] = "application/x-pkcs7-certificates"
_mimetypes["spl"] = "application/futuresplash"
_mimetypes["src"] = "application/x-wais-source"
_mimetypes["sst"] = "application/vnd.ms-pkicertstore"
_mimetypes["stl"] = "application/vnd.ms-pkistl"
_mimetypes["stm"] = "text/html"
_mimetypes["svg"] = "image/svg+xml"
_mimetypes["sv4cpio"] = "application/x-sv4cpio"
_mimetypes["sv4crc"] = "application/x-sv4crc"
_mimetypes["swf"] = "application/x-shockwave-flash"
_mimetypes["t"] = "application/x-troff"
_mimetypes["tar"] = "application/x-tar"
_mimetypes["tcl"] = "application/x-tcl"
_mimetypes["tex"] = "application/x-tex"
_mimetypes["texi"] = "application/x-texinfo"
_mimetypes["texinfo"] = "application/x-texinfo"
_mimetypes["tgz"] = "application/x-compressed"
_mimetypes["tif"] = "image/tiff"
_mimetypes["tiff"] = "image/tiff"
_mimetypes["tr"] = "application/x-troff"
_mimetypes["trm"] = "application/x-msterminal"
_mimetypes["tsv"] = "text/tab-separated-values"
_mimetypes["txt"] = "text/plain"
_mimetypes["uls"] = "text/iuls"
_mimetypes["ustar"] = "application/x-ustar"
_mimetypes["vcf"] = "text/x-vcard"
_mimetypes["vrml"] = "x-world/x-vrml"
_mimetypes["wav"] = "audio/x-wav"
_mimetypes["wcm"] = "application/vnd.ms-works"
_mimetypes["wdb"] = "application/vnd.ms-works"
_mimetypes["wks"] = "application/vnd.ms-works"
_mimetypes["wmf"] = "application/x-msmetafile"
_mimetypes["wps"] = "application/vnd.ms-works"
_mimetypes["wri"] = "application/x-mswrite"
_mimetypes["wrl"] = "x-world/x-vrml"
_mimetypes["wrz"] = "x-world/x-vrml"
_mimetypes["xaf"] = "x-world/x-vrml"
_mimetypes["xbm"] = "image/x-xbitmap"
_mimetypes["xla"] = "application/vnd.ms-excel"
_mimetypes["xlc"] = "application/vnd.ms-excel"
_mimetypes["xlm"] = "application/vnd.ms-excel"
_mimetypes["xls"] = "application/vnd.ms-excel"
_mimetypes["xlt"] = "application/vnd.ms-excel"
_mimetypes["xlw"] = "application/vnd.ms-excel"
_mimetypes["xof"] = "x-world/x-vrml"
_mimetypes["xpm"] = "image/x-xpixmap"
_mimetypes["xwd"] = "image/x-xwindowdump"
_mimetypes["z"] = "application/x-compress"
_mimetypes["zip"] = "application/zip"


def mimetype_on_ext(ext: str) -> str:
    return _mimetypes.get(ext, MIMETYPE_APPLICATION_OCTET_STREAM)


# -*- coding: utf-8 -*-
""" this module define http protocol status code """


STATUSCODE_100: int = 100
STATUSCODE_101: int = 101
STATUSCODE_103: int = 103
STATUSCODE_200: int = 200
STATUSCODE_201: int = 201
STATUSCODE_202: int = 202
STATUSCODE_203: int = 203
STATUSCODE_204: int = 204
STATUSCODE_205: int = 205
STATUSCODE_206: int = 206
STATUSCODE_300: int = 300
STATUSCODE_301: int = 301
STATUSCODE_302: int = 302
STATUSCODE_303: int = 303
STATUSCODE_304: int = 304
STATUSCODE_307: int = 307
STATUSCODE_308: int = 308
STATUSCODE_400: int = 400
STATUSCODE_401: int = 401
STATUSCODE_402: int = 402
STATUSCODE_403: int = 403
STATUSCODE_404: int = 404
STATUSCODE_405: int = 405
STATUSCODE_406: int = 406
STATUSCODE_407: int = 407
STATUSCODE_408: int = 408
STATUSCODE_409: int = 409
STATUSCODE_410: int = 410
STATUSCODE_411: int = 411
STATUSCODE_412: int = 412
STATUSCODE_413: int = 413
STATUSCODE_414: int = 414
STATUSCODE_415: int = 415
STATUSCODE_416: int = 416
STATUSCODE_417: int = 417
STATUSCODE_418: int = 418
STATUSCODE_422: int = 422
STATUSCODE_425: int = 425
STATUSCODE_426: int = 426
STATUSCODE_428: int = 428
STATUSCODE_429: int = 429
STATUSCODE_431: int = 431
STATUSCODE_451: int = 451
STATUSCODE_500: int = 500
STATUSCODE_501: int = 501
STATUSCODE_502: int = 502
STATUSCODE_503: int = 503
STATUSCODE_504: int = 504
STATUSCODE_505: int = 505
STATUSCODE_506: int = 506
STATUSCODE_507: int = 507
STATUSCODE_508: int = 508
STATUSCODE_510: int = 510
STATUSCODE_511: int = 511

_statusmsg: Dict[int, str] = dict()
_statusmsg[STATUSCODE_100] = "Continue"
_statusmsg[STATUSCODE_101] = "Switching Protocols"
_statusmsg[STATUSCODE_103] = "Early Hints"
_statusmsg[STATUSCODE_200] = "OK"
_statusmsg[STATUSCODE_201] = "Created"
_statusmsg[STATUSCODE_202] = "Accepted"
_statusmsg[STATUSCODE_203] = "Non-Authoritative Information"
_statusmsg[STATUSCODE_204] = "No Content"
_statusmsg[STATUSCODE_205] = "Reset Content"
_statusmsg[STATUSCODE_206] = "Partial Content"
_statusmsg[STATUSCODE_300] = "Multiple Choices"
_statusmsg[STATUSCODE_301] = "Moved Permanently"
_statusmsg[STATUSCODE_302] = "Found"
_statusmsg[STATUSCODE_303] = "See Other"
_statusmsg[STATUSCODE_304] = "Not Modified"
_statusmsg[STATUSCODE_307] = "Temporary Redirect"
_statusmsg[STATUSCODE_308] = "Permanent Redirect"
_statusmsg[STATUSCODE_400] = "Bad Request"
_statusmsg[STATUSCODE_401] = "Unauthorized"
_statusmsg[STATUSCODE_402] = "Payment Required"
_statusmsg[STATUSCODE_403] = "Forbidden"
_statusmsg[STATUSCODE_404] = "Not Found"
_statusmsg[STATUSCODE_405] = "Method Not Allowed"
_statusmsg[STATUSCODE_406] = "Not Acceptable"
_statusmsg[STATUSCODE_407] = "Proxy Authentication Required"
_statusmsg[STATUSCODE_408] = "Request Timeout"
_statusmsg[STATUSCODE_409] = "Conflict"
_statusmsg[STATUSCODE_410] = "Gone"
_statusmsg[STATUSCODE_411] = "Length Required"
_statusmsg[STATUSCODE_412] = "Precondition Failed"
_statusmsg[STATUSCODE_413] = "Payload Too Large"
_statusmsg[STATUSCODE_414] = "URI Too Long"
_statusmsg[STATUSCODE_415] = "Unsupported Media Type"
_statusmsg[STATUSCODE_416] = "Range Not Satisfiable"
_statusmsg[STATUSCODE_417] = "Expectation Failed"
_statusmsg[STATUSCODE_418] = "I'm a teapot"
_statusmsg[STATUSCODE_422] = "Unprocessable Entity"
_statusmsg[STATUSCODE_425] = "Too Early"
_statusmsg[STATUSCODE_426] = "Upgrade Required"
_statusmsg[STATUSCODE_428] = "Precondition Required"
_statusmsg[STATUSCODE_429] = "Too Many Requests"
_statusmsg[STATUSCODE_431] = "Request Header Fields Too Large"
_statusmsg[STATUSCODE_451] = "Unavailable For Legal Reasons"
_statusmsg[STATUSCODE_500] = "Internal Server Error"
_statusmsg[STATUSCODE_501] = "Not Implemented"
_statusmsg[STATUSCODE_502] = "Bad Gateway"
_statusmsg[STATUSCODE_503] = "Service Unavailable"
_statusmsg[STATUSCODE_504] = "Gateway Timeout"
_statusmsg[STATUSCODE_505] = "HTTP Version Not Supported"
_statusmsg[STATUSCODE_506] = "Variant Also Negotiates"
_statusmsg[STATUSCODE_507] = "Insufficient Storage"
_statusmsg[STATUSCODE_508] = "Loop Detected"
_statusmsg[STATUSCODE_510] = "Not Extended"
_statusmsg[STATUSCODE_511] = "Network Authentication Required"


def msg_on_statuscode(code: int) -> str:
    '''
    return status msg
    '''
    msg = _statusmsg.get(code, '--')
    return msg


def statusline(code: int) -> str:
    '''
    return $code $msg
    '''
    msg = _statusmsg.get(code, '--')
    return '%d %s' % (code, msg)


HTTP: str = "http"
HTTPPORT: int = 80
HTTPS: str = "https"
HTTPSPORT: int = 443

ENCODING_NONE: str = ""
ENCODING_DEFLATE: str = "deflate"
ENCODING_BR: str = "br"
ENCODING_GZIP: str = "gzip"

HTTP_HEADER_CONTENTTYPE = "Content-Type"
HTTP_HEADER_CONTENTLENGTH = "Content-Length"
HTTP_HEADER_CONTENTLANGUAGE = "Content-Language"
HTTP_HEADER_LOCATION = "Location"
HTTP_HEADER_ACCEPTENCODING = "Accept-Encoding"
HTTP_HEADER_CONTENTENCODING = "Content-Encoding"
HTTP_HEADER_ACCEPTRANGES = "Accept-Ranges"
HTTP_HEADER_CONTENTRANGE = "Content-Range"
HTTP_HEADER_SETCOOKIE = "Set-Cookie"
