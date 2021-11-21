

from re import I
import re
from servlet.httprequest import HttpRequest
from servlet.httpresponse import HttpResponse
from servlet import http


def newup(http_request: HttpRequest, http_response: HttpResponse):

    name: str = "0"
    id: str = "0"
    url: str = "0"

    fans_num: str = "0"
    likes_num: str = "0"
    plays_num: str = "0"
    recharges_num: str = "0"
    works_num: str = "0"

    snippets = '''
    <p> id %s uid %s url %s </p>
    <p> fans %s likes %s plays %s recharges %s works %s </p>
        '''
    form = http_request.getbodyasformurlencoded()
    main_page = form.get('uphome', None)
    if not main_page:
        out = snippets % (name, id, url, fans_num, likes_num,
                          plays_num, recharges_num, works_num)
        http_response.responsex(http.HTTP_STATUSCODE_200,
                                out)
        pass

    from urllib import request
    from lxml import etree

    resp = request.urlopen(main_page[0])
    resp_body = resp.read()
    txt = resp_body.decode('utf-8')
    htm = etree.HTML(txt)
    nodes = htm.xpath('//span')

    #name = ndes[0].text
    url = main_page[0]

    out = snippets % (name, id, url, fans_num, likes_num,
                      plays_num, recharges_num, works_num)
    http_response.responsex(http.HTTP_STATUSCODE_200,
                            out)
