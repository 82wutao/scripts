
from typing import Dict


HTTP_STATUSCODE_100 = 100
HTTP_STATUSCODE_101 = 101
HTTP_STATUSCODE_103 = 103
HTTP_STATUSCODE_200 = 200
HTTP_STATUSCODE_201 = 201
HTTP_STATUSCODE_202 = 202
HTTP_STATUSCODE_203 = 203
HTTP_STATUSCODE_204 = 204
HTTP_STATUSCODE_205 = 205
HTTP_STATUSCODE_206 = 206
HTTP_STATUSCODE_300 = 300
HTTP_STATUSCODE_301 = 301
HTTP_STATUSCODE_302 = 302
HTTP_STATUSCODE_303 = 303
HTTP_STATUSCODE_304 = 304
HTTP_STATUSCODE_307 = 307
HTTP_STATUSCODE_308 = 308
HTTP_STATUSCODE_400 = 400
HTTP_STATUSCODE_401 = 401
HTTP_STATUSCODE_402 = 402
HTTP_STATUSCODE_403 = 403
HTTP_STATUSCODE_404 = 404
HTTP_STATUSCODE_405 = 405
HTTP_STATUSCODE_406 = 406
HTTP_STATUSCODE_407 = 407
HTTP_STATUSCODE_408 = 408
HTTP_STATUSCODE_409 = 409
HTTP_STATUSCODE_410 = 410
HTTP_STATUSCODE_411 = 411
HTTP_STATUSCODE_412 = 412
HTTP_STATUSCODE_413 = 413
HTTP_STATUSCODE_414 = 414
HTTP_STATUSCODE_415 = 415
HTTP_STATUSCODE_416 = 416
HTTP_STATUSCODE_417 = 417
HTTP_STATUSCODE_418 = 418
HTTP_STATUSCODE_422 = 422
HTTP_STATUSCODE_425 = 425
HTTP_STATUSCODE_426 = 426
HTTP_STATUSCODE_428 = 428
HTTP_STATUSCODE_429 = 429
HTTP_STATUSCODE_431 = 431
HTTP_STATUSCODE_451 = 451
HTTP_STATUSCODE_500 = 500
HTTP_STATUSCODE_501 = 501
HTTP_STATUSCODE_502 = 502
HTTP_STATUSCODE_503 = 503
HTTP_STATUSCODE_504 = 504
HTTP_STATUSCODE_505 = 505
HTTP_STATUSCODE_506 = 506
HTTP_STATUSCODE_507 = 507
HTTP_STATUSCODE_508 = 508
HTTP_STATUSCODE_510 = 510
HTTP_STATUSCODE_511 = 511

__code_msgs: Dict[int, str] = dict()

__code_msgs[HTTP_STATUSCODE_100] = "Continue"
__code_msgs[HTTP_STATUSCODE_101] = "Switching Protocols"
__code_msgs[HTTP_STATUSCODE_103] = "Early Hints"
__code_msgs[HTTP_STATUSCODE_200] = "OK"
__code_msgs[HTTP_STATUSCODE_201] = "Created"
__code_msgs[HTTP_STATUSCODE_202] = "Accepted"
__code_msgs[HTTP_STATUSCODE_203] = "Non-Authoritative Information"
__code_msgs[HTTP_STATUSCODE_204] = "No Content"
__code_msgs[HTTP_STATUSCODE_205] = "Reset Content"
__code_msgs[HTTP_STATUSCODE_206] = "Partial Content"
__code_msgs[HTTP_STATUSCODE_300] = "Multiple Choices"
__code_msgs[HTTP_STATUSCODE_301] = "Moved Permanently"
__code_msgs[HTTP_STATUSCODE_302] = "Found"
__code_msgs[HTTP_STATUSCODE_303] = "See Other"
__code_msgs[HTTP_STATUSCODE_304] = "Not Modified"
__code_msgs[HTTP_STATUSCODE_307] = "Temporary Redirect"
__code_msgs[HTTP_STATUSCODE_308] = "Permanent Redirect"
__code_msgs[HTTP_STATUSCODE_400] = "Bad Request"
__code_msgs[HTTP_STATUSCODE_401] = "Unauthorized"
__code_msgs[HTTP_STATUSCODE_402] = "Payment Required"
__code_msgs[HTTP_STATUSCODE_403] = "Forbidden"
__code_msgs[HTTP_STATUSCODE_404] = "Not Found"
__code_msgs[HTTP_STATUSCODE_405] = "Method Not Allowed"
__code_msgs[HTTP_STATUSCODE_406] = "Not Acceptable"
__code_msgs[HTTP_STATUSCODE_407] = "Proxy Authentication Required"
__code_msgs[HTTP_STATUSCODE_408] = "Request Timeout"
__code_msgs[HTTP_STATUSCODE_409] = "Conflict"
__code_msgs[HTTP_STATUSCODE_410] = "Gone"
__code_msgs[HTTP_STATUSCODE_411] = "Length Required"
__code_msgs[HTTP_STATUSCODE_412] = "Precondition Failed"
__code_msgs[HTTP_STATUSCODE_413] = "Payload Too Large"
__code_msgs[HTTP_STATUSCODE_414] = "URI Too Long"
__code_msgs[HTTP_STATUSCODE_415] = "Unsupported Media Type"
__code_msgs[HTTP_STATUSCODE_416] = "Range Not Satisfiable"
__code_msgs[HTTP_STATUSCODE_417] = "Expectation Failed"
__code_msgs[HTTP_STATUSCODE_418] = "I'm a teapot"
__code_msgs[HTTP_STATUSCODE_422] = "Unprocessable Entity"
__code_msgs[HTTP_STATUSCODE_425] = "Too Early"
__code_msgs[HTTP_STATUSCODE_426] = "Upgrade Required"
__code_msgs[HTTP_STATUSCODE_428] = "Precondition Required"
__code_msgs[HTTP_STATUSCODE_429] = "Too Many Requests"
__code_msgs[HTTP_STATUSCODE_431] = "Request Header Fields Too Large"
__code_msgs[HTTP_STATUSCODE_451] = "Unavailable For Legal Reasons"
__code_msgs[HTTP_STATUSCODE_500] = "Internal Server Error"
__code_msgs[HTTP_STATUSCODE_501] = "Not Implemented"
__code_msgs[HTTP_STATUSCODE_502] = "Bad Gateway"
__code_msgs[HTTP_STATUSCODE_503] = "Service Unavailable"
__code_msgs[HTTP_STATUSCODE_504] = "Gateway Timeout"
__code_msgs[HTTP_STATUSCODE_505] = "HTTP Version Not Supported"
__code_msgs[HTTP_STATUSCODE_506] = "Variant Also Negotiates"
__code_msgs[HTTP_STATUSCODE_507] = "Insufficient Storage"
__code_msgs[HTTP_STATUSCODE_508] = "Loop Detected"
__code_msgs[HTTP_STATUSCODE_510] = "Not Extended"
__code_msgs[HTTP_STATUSCODE_511] = "Network Authentication Required"


def getstatusmsg(code: int) -> str:
    msg = __code_msgs.get(code, '--')
    return msg


def statusline(code: int) -> str:
    msg = __code_msgs.get(code, '--')
    return '%d %s' % (code, msg)


HTTP_HEADER_CONTENTTYPE = "Content-Type"
HTTP_HEADER_CONTENTLENGTH = "Content-Length"
HTTP_HEADER_LOCATION = "Location"


# https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Basics_of_HTTP/MIME_types
# text 	表明文件是普通文本，理论上是人类可读
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

MIMETYPE_MULTIPART_FORM_DATA = "multipart/form-data"
MIMETYPE_MULTIPART_BYTERANGES = "multipart/byteranges"
# Content-Type: multipart/form-data
#boundary = aBoundaryString
# (other headers associated with the multipart document as a whole)
#
# --aBoundaryString
# Content-Disposition: form-data
#name = "myFile"
#filename = "img.jpg"
# Content-Type: image/jpeg
#
# (data)
# --aBoundaryString
# Content-Disposition: form-data
#name = "myField"
#
# (data)
# --aBoundaryString
# (more subparts)
# --aBoundaryString--


# multipart/byteranges用于把部分的响应报文发送回浏览器
# HTTP/1.1 206 Partial Content
# Accept-Ranges: bytes
# Content-Type: multipart/byteranges
# boundary = 3d6b6a416f9b5
# Content-Length: 385
#
# --3d6b6a416f9b5
# Content-Type: text/html
# Content-Range: bytes 100-200/1270
#
# eta http-equiv = "Content-type" content = "text/html; charset=utf-8" / >
# <meta name = "vieport" content
# --3d6b6a416f9b5
# Content-Type: text/html
# Content-Range: bytes 300-400/1270
#
# -color:  # f0f0f2;
#    margin: 0
#    padding: 0
#    font-family: "Open Sans", "Helvetica
# --3d6b6a416f9b5--
