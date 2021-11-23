

from typing import Any, Dict
from urllib import request, parse
import json

import brotli

from servlet.httprequest import HttpRequest
from servlet.httpresponse import HttpResponse
from servlet import http

from . import httpcli


__headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    #    "Cookie": "b_ut=-1; i-wanna-go-back=1; _uuid=106DA1078A-6104E-A6102-A827-D484C95B345549893infoc; buvid3=411C6271-CE5B-4C3B-B277-7F960C8D923D148821infoc; innersign=1; CURRENT_FNVAL=976; video_page_version=v_old_home; blackside_state=1; sid=c3jslmbj; rpdid=|(u)~lkRYllJ0J'uYJ~Y~muYm; PVID=1",
    "Cookie": "l=v; buvid3=88C37D19-9BCA-4BB5-B024-7B9D6F8708C2167645infoc; fingerprint=b29830b38982174ee0962d880920b808; buvid_fp=FA8FC64B-D1EA-4AD1-93C0-2ED8D08EC08640937infoc; buvid_fp_plain=FA8FC64B-D1EA-4AD1-93C0-2ED8D08EC08640937infoc; CURRENT_FNVAL=976; blackside_state=1; rpdid=|(u)~lkRlRJR0J'uYkl|R)Y~~; PVID=1; CURRENT_QUALITY=80; _uuid=C76D5032-A91A-7C2B-B21B-C17FB9250EEF06762infoc; bp_video_offset_25884693=595932141167186350; CURRENT_BLACKGAP=1; bp_t_offset_25884693=595936762547843957; sid=4qj6r4p0; SESSDATA=0bd228ec%2C1647445844%2C79440%2A91; bili_jct=8a822b98fdb4da2bee1ac628fbb5a2fb; DedeUserID=25884693; DedeUserID__ckMd5=5b87d86fc9837a3b; LIVE_BUVID=AUTO3416329243207348; fingerprint3=4aca6b31a9ddeb80a9c2772c704d5c45; fingerprint_s=45d4a0701fecf7f417e896135ac54a0c; video_page_version=v_old_home; innersign=1; bsource=search_baidu",
    "Origin": "https://space.bilibili.com",
    "Referer": "https://space.bilibili.com/7953030?spm_id_from=333.788.b_765f7570696e666f.1",
    "Sec-Ch-Ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\", \"Microsoft Edge\";v=\"96\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0 Win64 x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 Edg/96.0.1054.29"
}


def hdl(assignment) -> httpcli.HandleCallback:
    def _hdl(status: int, reason: str, headers: Dict[str, str], body: bytes):
        if status != 200:
            return

        encoding = headers.get(http.HTTP_HEADER_CONTENTENCODING, None)
        type_charset = headers.get(http.HTTP_HEADER_CONTENTTYPE, None)

        cont: bytes = None
        txt: str = None
        r = True
        while r:
            if not encoding:
                cont = body
                break
            if encoding == http.HTTP_CONTENTENCODING_BR:
                cont = brotli.decompress(body)
                break
            r = False

        r = True
        while r:
            if type_charset.find("; charset") == -1:
                txt = cont.decode()
                break
            charset = type_charset.split("; charset")[1]
            txt = cont.decode(charset)
            r = False
        assignment(json.loads(txt))
    return _hdl


def bilibili_api(api: str, query: Dict[str, str]) -> Dict[str, Any]:
    ret = {}

    def ass(res):
        nonlocal ret
        ret = res
        pass

    httpcli.https_get("api.bilibili.com", 443,
                      api, query, __headers, hdl(ass))
    return ret


def newup(http_request: HttpRequest, http_response: HttpResponse):

    mid: str = "0"
    name: str = "0"
    url: str = "0"

    fans_num: str = "0"
    likes_num: str = "0"
    plays_num: str = "0"
    recharges_num: str = "0"
    works_num: str = "0"

    snippets = '''
    <p> id %s mid %s url %s </p>
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
    mid = main_page[0]
    upbase = bilibili_api("/x/space/acc/info", {
        'mid': mid,
        'jsonp': 'jsonp',
    })

    uprel = bilibili_api("/x/relation/stat", {
        'vmid': mid,
        'jsonp': 'jsonp',
    })

    upstat = bilibili_api("/x/space/upstat", {
        'mid': mid,
        'jsonp': 'jsonp',
    })
    vedios = bilibili_api("/x/space/arc/search", {
        "mid": mid,
        "pn": "1",
        "ps": "25",
        "index": "1",
        "jsonp": "jsonp",
    })
    name = upbase['data']['name']
    url = upbase['data']['face']
    fans_num = uprel['data']['follower']
    likes_num = upstat['data']['likes']
    plays_num = upstat['data']['archive']['view']
    works_num = vedios['data']['page']['count']
    out = snippets % (name, id, url, fans_num, likes_num,
                      plays_num, recharges_num, works_num)
    http_response.responsex(http.HTTP_STATUSCODE_200,
                            out)
