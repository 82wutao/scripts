
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
MIMETYPE_APPLICATION_JSON = "application/json"

MIMETYPE_MULTIPART_FORM_DATA = "multipart/form-data"
MIMETYPE_MULTIPART_BYTERANGES = "multipart/byteranges"

__mimetypes: Dict[str, str] = dict()
__mimetypes["323"] = "text/h323"
__mimetypes["acx"] = "application/internet-property-stream"
__mimetypes["ai"] = "application/postscript"
__mimetypes["aif"] = "audio/x-aiff"
__mimetypes["aifc"] = "audio/x-aiff"
__mimetypes["aiff"] = "audio/x-aiff"
__mimetypes["asf"] = "video/x-ms-asf"
__mimetypes["asr"] = "video/x-ms-asf"
__mimetypes["asx"] = "video/x-ms-asf"
__mimetypes["au"] = "audio/basic"
__mimetypes["avi"] = "video/x-msvideo"
__mimetypes["axs"] = "application/olescript"
__mimetypes["bas"] = "text/plain"
__mimetypes["bcpio"] = "application/x-bcpio"
__mimetypes["bin"] = "application/octet-stream"
__mimetypes["bmp"] = "image/bmp"
__mimetypes["c"] = "text/plain"
__mimetypes["cat"] = "application/vnd.ms-pkiseccat"
__mimetypes["cdf"] = "application/x-cdf"
__mimetypes["cer"] = "application/x-x509-ca-cert"
__mimetypes["class"] = "application/octet-stream"
__mimetypes["clp"] = "application/x-msclip"
__mimetypes["cmx"] = "image/x-cmx"
__mimetypes["cod"] = "image/cis-cod"
__mimetypes["cpio"] = "application/x-cpio"
__mimetypes["crd"] = "application/x-mscardfile"
__mimetypes["crl"] = "application/pkix-crl"
__mimetypes["crt"] = "application/x-x509-ca-cert"
__mimetypes["csh"] = "application/x-csh"
__mimetypes["css"] = "text/css"
__mimetypes["dcr"] = "application/x-director"
__mimetypes["der"] = "application/x-x509-ca-cert"
__mimetypes["dir"] = "application/x-director"
__mimetypes["dll"] = "application/x-msdownload"
__mimetypes["dms"] = "application/octet-stream"
__mimetypes["doc"] = "application/msword"
__mimetypes["dot"] = "application/msword"
__mimetypes["dvi"] = "application/x-dvi"
__mimetypes["dxr"] = "application/x-director"
__mimetypes["eps"] = "application/postscript"
__mimetypes["etx"] = "text/x-setext"
__mimetypes["evy"] = "application/envoy"
__mimetypes["exe"] = "application/octet-stream"
__mimetypes["fif"] = "application/fractals"
__mimetypes["flr"] = "x-world/x-vrml"
__mimetypes["gif"] = "image/gif"
__mimetypes["gtar"] = "application/x-gtar"
__mimetypes["gz"] = "application/x-gzip"
__mimetypes["h"] = "text/plain"
__mimetypes["hdf"] = "application/x-hdf"
__mimetypes["hlp"] = "application/winhlp"
__mimetypes["hqx"] = "application/mac-binhex40"
__mimetypes["hta"] = "application/hta"
__mimetypes["htc"] = "text/x-component"
__mimetypes["htm"] = "text/html"
__mimetypes["html"] = "text/html"
__mimetypes["htt"] = "text/webviewhtml"
__mimetypes["ico"] = "image/x-icon"
__mimetypes["ief"] = "image/ief"
__mimetypes["iii"] = "application/x-iphone"
__mimetypes["ins"] = "application/x-internet-signup"
__mimetypes["isp"] = "application/x-internet-signup"
__mimetypes["jfif"] = "image/pipeg"
__mimetypes["jpe"] = "image/jpeg"
__mimetypes["jpeg"] = "image/jpeg"
__mimetypes["jpg"] = "image/jpeg"
__mimetypes["js"] = "application/x-javascript"
__mimetypes["latex"] = "application/x-latex"
__mimetypes["lha"] = "application/octet-stream"
__mimetypes["lsf"] = "video/x-la-asf"
__mimetypes["lsx"] = "video/x-la-asf"
__mimetypes["lzh"] = "application/octet-stream"
__mimetypes["m13"] = "application/x-msmediaview"
__mimetypes["m14"] = "application/x-msmediaview"
__mimetypes["m3u"] = "audio/x-mpegurl"
__mimetypes["man"] = "application/x-troff-man"
__mimetypes["mdb"] = "application/x-msaccess"
__mimetypes["me"] = "application/x-troff-me"
__mimetypes["mht"] = "message/rfc822"
__mimetypes["mhtml"] = "message/rfc822"
__mimetypes["mid"] = "audio/mid"
__mimetypes["mny"] = "application/x-msmoney"
__mimetypes["mov"] = "video/quicktime"
__mimetypes["movie"] = "video/x-sgi-movie"
__mimetypes["mp2"] = "video/mpeg"
__mimetypes["mp3"] = "audio/mpeg"
__mimetypes["mpa"] = "video/mpeg"
__mimetypes["mpe"] = "video/mpeg"
__mimetypes["mpeg"] = "video/mpeg"
__mimetypes["mpg"] = "video/mpeg"
__mimetypes["mpp"] = "application/vnd.ms-project"
__mimetypes["mpv2"] = "video/mpeg"
__mimetypes["ms"] = "application/x-troff-ms"
__mimetypes["mvb"] = "application/x-msmediaview"
__mimetypes["nws"] = "message/rfc822"
__mimetypes["oda"] = "application/oda"
__mimetypes["p10"] = "application/pkcs10"
__mimetypes["p12"] = "application/x-pkcs12"
__mimetypes["p7b"] = "application/x-pkcs7-certificates"
__mimetypes["p7c"] = "application/x-pkcs7-mime"
__mimetypes["p7m"] = "application/x-pkcs7-mime"
__mimetypes["p7r"] = "application/x-pkcs7-certreqresp"
__mimetypes["p7s"] = "application/x-pkcs7-signature"
__mimetypes["pbm"] = "image/x-portable-bitmap"
__mimetypes["pdf"] = "application/pdf"
__mimetypes["pfx"] = "application/x-pkcs12"
__mimetypes["pgm"] = "image/x-portable-graymap"
__mimetypes["pko"] = "application/ynd.ms-pkipko"
__mimetypes["pma"] = "application/x-perfmon"
__mimetypes["pmc"] = "application/x-perfmon"
__mimetypes["pml"] = "application/x-perfmon"
__mimetypes["pmr"] = "application/x-perfmon"
__mimetypes["pmw"] = "application/x-perfmon"
__mimetypes["pnm"] = "image/x-portable-anymap"
__mimetypes["pot"] = "application/vnd.ms-powerpoint"
__mimetypes["ppm"] = "image/x-portable-pixmap"
__mimetypes["pps"] = "application/vnd.ms-powerpoint"
__mimetypes["ppt"] = "application/vnd.ms-powerpoint"
__mimetypes["prf"] = "application/pics-rules"
__mimetypes["ps"] = "application/postscript"
__mimetypes["pub"] = "application/x-mspublisher"
__mimetypes["qt"] = "video/quicktime"
__mimetypes["ra"] = "audio/x-pn-realaudio"
__mimetypes["ram"] = "audio/x-pn-realaudio"
__mimetypes["ras"] = "image/x-cmu-raster"
__mimetypes["rgb"] = "image/x-rgb"
__mimetypes["rmi"] = "audio/mid"
__mimetypes["roff"] = "application/x-troff"
__mimetypes["rtf"] = "application/rtf"
__mimetypes["rtx"] = "text/richtext"
__mimetypes["scd"] = "application/x-msschedule"
__mimetypes["sct"] = "text/scriptlet"
__mimetypes["setpay"] = "application/set-payment-initiation"
__mimetypes["setreg"] = "application/set-registration-initiation"
__mimetypes["sh"] = "application/x-sh"
__mimetypes["shar"] = "application/x-shar"
__mimetypes["sit"] = "application/x-stuffit"
__mimetypes["snd"] = "audio/basic"
__mimetypes["spc"] = "application/x-pkcs7-certificates"
__mimetypes["spl"] = "application/futuresplash"
__mimetypes["src"] = "application/x-wais-source"
__mimetypes["sst"] = "application/vnd.ms-pkicertstore"
__mimetypes["stl"] = "application/vnd.ms-pkistl"
__mimetypes["stm"] = "text/html"
__mimetypes["svg"] = "image/svg+xml"
__mimetypes["sv4cpio"] = "application/x-sv4cpio"
__mimetypes["sv4crc"] = "application/x-sv4crc"
__mimetypes["swf"] = "application/x-shockwave-flash"
__mimetypes["t"] = "application/x-troff"
__mimetypes["tar"] = "application/x-tar"
__mimetypes["tcl"] = "application/x-tcl"
__mimetypes["tex"] = "application/x-tex"
__mimetypes["texi"] = "application/x-texinfo"
__mimetypes["texinfo"] = "application/x-texinfo"
__mimetypes["tgz"] = "application/x-compressed"
__mimetypes["tif"] = "image/tiff"
__mimetypes["tiff"] = "image/tiff"
__mimetypes["tr"] = "application/x-troff"
__mimetypes["trm"] = "application/x-msterminal"
__mimetypes["tsv"] = "text/tab-separated-values"
__mimetypes["txt"] = "text/plain"
__mimetypes["uls"] = "text/iuls"
__mimetypes["ustar"] = "application/x-ustar"
__mimetypes["vcf"] = "text/x-vcard"
__mimetypes["vrml"] = "x-world/x-vrml"
__mimetypes["wav"] = "audio/x-wav"
__mimetypes["wcm"] = "application/vnd.ms-works"
__mimetypes["wdb"] = "application/vnd.ms-works"
__mimetypes["wks"] = "application/vnd.ms-works"
__mimetypes["wmf"] = "application/x-msmetafile"
__mimetypes["wps"] = "application/vnd.ms-works"
__mimetypes["wri"] = "application/x-mswrite"
__mimetypes["wrl"] = "x-world/x-vrml"
__mimetypes["wrz"] = "x-world/x-vrml"
__mimetypes["xaf"] = "x-world/x-vrml"
__mimetypes["xbm"] = "image/x-xbitmap"
__mimetypes["xla"] = "application/vnd.ms-excel"
__mimetypes["xlc"] = "application/vnd.ms-excel"
__mimetypes["xlm"] = "application/vnd.ms-excel"
__mimetypes["xls"] = "application/vnd.ms-excel"
__mimetypes["xlt"] = "application/vnd.ms-excel"
__mimetypes["xlw"] = "application/vnd.ms-excel"
__mimetypes["xof"] = "x-world/x-vrml"
__mimetypes["xpm"] = "image/x-xpixmap"
__mimetypes["xwd"] = "image/x-xwindowdump"
__mimetypes["z"] = "application/x-compress"
__mimetypes["zip"] = "application/zip"


def mimetype(ext: str) -> str:
    return __mimetypes.get(ext, MIMETYPE_APPLICATION_OCTET_STREAM)

# Content-Type: multipart/form-data
# boundary = aBoundaryString
# (other headers associated with the multipart document as a whole)
#
# --aBoundaryString
# Content-Disposition: form-data
# name = "myFile"
# filename = "img.jpg"
# Content-Type: image/jpeg
#
# (data)
# --aBoundaryString
# Content-Disposition: form-data
# name = "myField"
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
# eta http-equiv = "Content-type"content = "text/html; charset=utf-8"/ >
# <meta name = "vieport"content
# --3d6b6a416f9b5
# Content-Type: text/html
# Content-Range: bytes 300-400/1270
#
# -color:  # f0f0f2;
#    margin: 0
#    padding: 0
#    font-family: "Open Sans", "Helvetica
# --3d6b6a416f9b5--
