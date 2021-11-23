

from typing import Any, Dict
from urllib import request, parse
import json

import brotli

from servlet.httprequest import HttpRequest
from servlet.httpresponse import HttpResponse
from servlet import http

from . import httpcli

# {
#    "code": 0, "message": "0", "ttl": 1,
#    "data": {
#        "mid": 495979610,
#        "name": "向杨Alan君",
#        "sex": "保密",
#        "face": "http://i1.hdslb.com/bfs/face/cd83dfc2a3303544eed398816dd7cfcac2851e29.jpg",
#        "face_nft": 0,
#        "sign": "芝加哥大学社会学博士\n11年从教英语精读、演讲与词汇\n",
#        "rank": 10000,
#        "level": 4,
#        "jointime": 0,
#        "moral": 0,
#        "silence": 0,
#        "coins": 0,
#        "fans_badge": false,
#        "fans_medal": {
#            "show": false,
#            "wear": false,
#            "medal": null
#        },
#        "official": {
#            "role": 0,
#            "title": "",
#            "desc": "",
#            "type": -1
#        },
#        "vip": {
#            "type": 2,
#            "status": 1,
#            "due_date": 1641052800000,
#            "vip_pay_type": 1,
#            "theme_type": 0,
#            "label": {
#                "path": "",
#                "text": "年度大会员",
#                "label_theme": "annual_vip",
#                "text_color": "#FFFFFF",
#                "bg_style": 1,
#                "bg_color": "#FB7299",
#                "border_color": ""
#            },
#            "avatar_subscript": 1,
#            "nickname_color": "#FB7299",
#            "role": 3,
#            "avatar_subscript_url": "http://i0.hdslb.com/bfs/vip/icon_Certification_big_member_22_3x.png"
#        },
#        "pendant": {
#            "pid": 0,
#            "name": "",
#            "image": "",
#            "expire": 0,
#            "image_enhance": "",
#            "image_enhance_frame": ""
#        },
#        "nameplate": {
#            "nid": 0,
#            "name": "",
#            "image": "",
#            "image_small": "",
#            "level": "",
#            "condition": ""
#        },
#        "user_honour_info": {
#            "mid": 0,
#            "colour": null,
#            "tags": []
#        },
#        "is_followed": false,
#        "top_photo": "http://i1.hdslb.com/bfs/space/cb1c3ef50e22b6096fde67febe863494caefebad.png",
#        "theme": {},
#        "sys_notice": {},
#        "live_room": {
#            "roomStatus": 1,
#            "liveStatus": 0,
#            "url": "https://live.bilibili.com/22519112",
#            "title": "设备测试",
#            "cover": "http://i0.hdslb.com/bfs/live/user_cover/a75f044b2d62860c1740cf9fae5c0a3ae0d390d9.jpg",
#            "online": 5,
#            "roomid": 22519112,
#            "roundStatus": 0,
#            "broadcast_type": 0
#        },
#        "birthday": "",
#        "school": {
#            "name": ""
#        },
#        "profession": {
#            "name": ""
#        },
#        "tags": null,
#        "series": {
#            "user_upgrade_status": 3,
#            "show_upgrade_window": false
#        }
#    }
# }

__headers = {
    "Accept":     "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding":    "gzip, deflate, br",
    "Accept-Language":   "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Connection":  "keep-alive",
    "Host":  "api.bilibili.com",  # Host: api.bilibili.com
    #        "Cookie": "buvid3 = FA8FC64B-D1EA-4AD1-93C0-2ED8D08EC08640937infoc; fingerprint = b29830b38982174ee0962d880920b808; buvid_fp = FA8FC64B-D1EA-4AD1-93C0-2ED8D08EC08640937infoc; buvid_fp_plain = FA8FC64B-D1EA-4AD1-93C0-2ED8D08EC08640937infoc; CURRENT_FNVAL = 976; blackside_state = 1; rpdid = |(u)~lkRlRJR0J'uYkl | R)Y~~; PVID=3; CURRENT_QUALITY=80; _uuid=C76D5032-A91A-7C2B-B21B-C17FB9250EEF06762infoc; bp_video_offset_25884693=595932141167186350; CURRENT_BLACKGAP=1; bp_t_offset_25884693=595936762547843957; sid=4qj6r4p0; SESSDATA=0bd228ec % 2C1647445844 % 2C79440 % 2A91; bili_jct=8a822b98fdb4da2bee1ac628fbb5a2fb; DedeUserID=25884693; DedeUserID__ckMd5=5b87d86fc9837a3b; LIVE_BUVID=AUTO3416329243207348; fingerprint3=4aca6b31a9ddeb80a9c2772c704d5c45; fingerprint_s=45d4a0701fecf7f417e896135ac54a0c; video_page_version=v_old_home_20; innersign=1; bsource=search_baidu",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "TE": "trailers",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv: 94.0) Gecko/20100101 Firefox/94.0"
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
        # nonlocal ret
        # ret = json.loads(txt)
        assignment(json.loads(txt))
    return _hdl


def upinfo(mid: str) -> Dict[str, Any]:
    query = {}
    query['mid'] = mid
    query['jsonp'] = 'jsonp'
    upinfo_api = "/x/space/acc/info"

    ret = {}

    def ass(res):
        nonlocal ret
        ret = res
        pass

    cb = hdl(ass)
    httpcli.https_get("api.bilibili.com", 443,
                      upinfo_api, query, __headers, cb)

    return ret


def uprelation(mid: str) -> Dict[str, Any]:
    query = {}
    query['mid'] = mid
    query['jsonp'] = 'jsonp'
    stat_api = "x/space/upstat"
    ret = {}

    def ass(res):
        nonlocal ret
        ret = res
        pass

    cb = hdl(ass)
    httpcli.https_get("api.bilibili.com", 443,
                      stat_api, query, __headers, cb)

    return ret


def upstat(mid: str) -> Dict[str, Any]:
    query = {}
    query['vmid'] = mid
    query['jsonp'] = 'jsonp'
    stat_api = "x/relation/stat"

    ret = {}

    def ass(res):
        nonlocal ret
        ret = res
        pass

    cb = hdl(ass)
    httpcli.https_get("api.bilibili.com", 443,
                      stat_api, query, __headers, cb)

    return ret


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
    up = upinfo(mid)
    rel = uprelation(mid)
    stat = upstat(mid)
    # https://api.bilibili.com/x/space/arc/search?mid=495979610&pn=1&ps=25&index=1&jsonp=jsonp
    vedios = bilibili_api()
    name = up['data']['name']
    url = up['data']['face']
    # {"code":0,"message":"0","ttl":1,"data":{"mid":495979610,"following":63,"whisper":0,"black":0,"follower":18042}}
    fans_num = rel['data']['follower']
    # {"code":0,"message":"0","ttl":1,"data":{"archive":{"view":1158167},"article":{"view":14399},"likes":60077}}
    likes_num = stat['data']['likes']
    plays_num = stat['data']['archive']['view']
    #{"code":0,"message":"0","ttl":1,"data":{"list":{"tlist":null,"vlist":[{"comment":8,"typeid":124,"play":1129,"pic":"http://i2.hdslb.com/bfs/archive/d2424493409ae30b93f294387c0964b9289c5923.jpg","subtitle":"","description":"https://www.youtube.com/watch?v=UI_QcD030Xw\n“I act as if God exists… and I’m terrified that he might”.\n\nJordan Peterson is asked whether he believes in God. He says that he doesn’t like the question - saying “I think it’s private”.","copyright":"2","title":"你信教吗？这个问题为什么有毒","review":0,"author":"向杨Alan君","mid":495979610,"created":1637570385,"length":"02:08","video_review":0,"aid":721850589,"bvid":"BV15S4y1R7LF","hide_click":false,"is_pay":0,"is_union_video":0,"is_steins_gate":0,"is_live_playback":0},{"comment":4,"typeid":124,"play":1331,"pic":"http://i0.hdslb.com/bfs/archive/88220b559728a5030b92fd26cdc63bcd51440e41.jpg","subtitle":"","description":"https://www.youtube.com/watch?v=VbVwV8_TEkM","copyright":"2","title":"当理性搁浅：信仰为何使人战栗？","review":0,"author":"向杨Alan君","mid":495979610,"created":1637508214,"length":"02:40","video_review":2,"aid":549254572,"bvid":"BV1eq4y1u7GJ","hide_click":false,"is_pay":0,"is_union_video":0,"is_steins_gate":0,"is_live_playback":0},{"comment":71,"typeid":124,"play":13649,"pic":"http://i1.hdslb.com/bfs/archive/23c2050a87630e1efdf500a521b36245db8f379a.jpg","subtitle":"","description":"https://www.youtube.com/watch?v=Z4yOfk6IHGc\u0026t=34s\n我说，你该是你父亲葬礼上最坚强的人","copyright":"2","title":"硬球心理学：别天真！把幸福当做人生目标，不幸将随时把你打入地狱","review":0,"author":"向杨Alan君","mid":495979610,"created":1637483662,"length":"04:25","video_review":18,"aid":506803200,"bvid":"BV15g411N7go","hide_click":false,"is_pay":0,"is_union_video":0,"is_steins_gate":0,"is_live_playback":0},{"comment":446,"typeid":124,"play":65430,"pic":"http://i0.hdslb.com/bfs/archive/9ab62eb37915c498faff2e0bbda46109d5acefc3.jpg","subtitle":"","description":"https://www.youtube.com/watch?v=k5ukKf4vi6g\u0026t=2s\na friend is a gift you give yourself","copyright":"2","title":"择友观影响生活质量：学会辨别身边有毒的朋友","review":0,"author":"向杨Alan君","mid":495979610,"created":1636972818,"length":"02:54","video_review":74,"aid":294223714,"bvid":"BV1LF411h7Hy","hide_click":false,"is_pay":0,"is_union_video":0,"is_steins_gate":0,"is_live_playback":0},{"comment":123,"typeid":124,"play":42070,"pic":"http://i0.hdslb.com/bfs/archive/b4bba5ec1b1f9673f79af33002d47056367ada7e.jpg","subtitle":"","description":"https://www.youtube.com/watch?v=_NQGQImrpx4\u0026t=38s\n克服社交焦虑，走出经验主义束缚。\nFor many this should be one of the most insightful points in Dr. Peterson’s lectures. In less than five minutes he puts the key to overcoming social anxiety in plain words.","copyright":"2","title":"硬球心理学：假如你有社交恐惧症？","review":0,"author":"向杨Alan君","mid":495979610,"created":1636880354,"length":"04:41","video_review":34,"aid":591677245,"bvid":"BV19q4y1z7pg","hide_click":false,"is_pay":0,"is_union_video":0,"is_steins_gate":0,"is_live_playback":0},{"comment":8,"typeid":208,"play":3628,"pic":"http://i2.hdslb.com/bfs/archive/4367f30fb1a5d29e275bf320de7b35a12ce47111.jpg","subtitle":"","description":"https://www.youtube.com/watch?v=e-I5u5hyoxY\n彼得森的演讲三板斧","copyright":"2","title":"龙虾教授的演讲经：做一台无情的输出机器？","review":0,"author":"向杨Alan君","mid":495979610,"created":1636723891,"length":"05:47","video_review":3,"aid":934163439,"bvid":"BV1cT4y1R76v","hide_click":false,"is_pay":0,"is_union_video":0,"is_steins_gate":0,"is_live_playback":0},{"comment":89,"typeid":124,"play":24316,"pic":"http://i2.hdslb.com/bfs/archive/46c7bc9d87012d028d7dc9cf14e8d781964d4fa5.jpg","subtitle":"","description":"加长版，从原来的5分钟扩展到10分钟","copyright":"1","title":"【加长版】当残忍成为一种可控的威慑力","review":0,"author":"向杨Alan君","mid":495979610,"created":1636464147,"length":"10:49","video_review":36,"aid":336609957,"bvid":"BV1fR4y147Tq","hide_click":false,"is_pay":0,"is_union_video":0,"is_steins_gate":0,"is_live_playback":0},{"comment":1423,"typeid":124,"play":460580,"pic":"http://i0.hdslb.com/bfs/archive/277a20f42b481f8901045c92417a610176caa6bd.jpg","subtitle":"","description":"https://www.youtube.com/watch?v=nJLuSbfme6Q\n龙虾教授解释了为什么有能力残忍而选择不残忍，对自己的人格发展很重要。","copyright":"2","title":"学会残忍对人格发展至关重要：深度理解自己的阴暗面","review":0,"author":"向杨Alan君","mid":495979610,"created":1636117433,"length":"05:31","video_review":575,"aid":591426539,"bvid":"BV1Eq4y1r7Gj","hide_click":false,"is_pay":0,"is_union_video":0,"is_steins_gate":0,"is_live_playback":0},{"comment":13,"typeid":124,"play":6574,"pic":"http://i1.hdslb.com/bfs/archive/e96cedb12665ee046b38f81cb44121b203c88ad7.jpg","subtitle":"","description":"https://www.youtube.com/watch?v=Ym6whrAw8wU\n詹姆斯·格里克于1954年出生于纽约市。他于1976年毕业于哈佛大学，并帮助创立了明尼阿波利斯的另类周报《大都会》。然后他在《纽约时报》担任了十年的编辑和记者。\n\n他的第一本书《混沌》是入围国家图书奖和普利策奖，也是全国畅销书。接下来的书包括最畅销的传记《天才：理查德·费曼和艾萨克·牛顿的生活与科学》，这两本书都入围了普利策奖，还有《更快》和《刚刚发生了什么》。这些作品已被翻译成25种语言。","copyright":"2","title":"天才是否有所谓的本质？比较牛顿和费曼的异同","review":0,"author":"向杨Alan君","mid":495979610,"created":1635852720,"length":"02:36","video_review":6,"aid":378968396,"bvid":"BV1af4y1u7hW","hide_click":false,"is_pay":0,"is_union_video":0,"is_steins_gate":0,"is_live_playback":0},{"comment":249,"typeid":124,"play":77293,"pic":"http://i0.hdslb.com/bfs/archive/281b442f14439d424a86dd0f291687790dc2f087.jpg","subtitle":"","description":"https://www.youtube.com/watch?v=82Fm1ZJ1CGQ\nThe willingness to be a fool is the precursor to transformation.","copyright":"2","title":"从把事情搞砸开始：追求清晰度，而非确定性","review":0,"author":"向杨Alan君","mid":495979610,"created":1635662264,"length":"06:56","video_review":147,"aid":718966292,"bvid":"BV1CQ4y1S7GU","hide_click":false,"is_pay":0,"is_union_video":0,"is_steins_gate":0,"is_live_playback":0},{"comment":7,"typeid":124,"play":1368,"pic":"http://i0.hdslb.com/bfs/archive/d56ca0462e12931a5892deb9669e2b916e332a1e.jpg","subtitle":"","description":"","copyright":"1","title":"如何培养自己阅读英文原版书的能力？从理论和实践层面讲透","review":0,"author":"向杨Alan君","mid":495979610,"created":1635604651,"length":"85:43","video_review":2,"aid":336420446,"bvid":"BV1RR4y177xL","hide_click":false,"is_pay":0,"is_union_video":0,"is_steins_gate":0,"is_live_playback":0},{"comment":181,"typeid":124,"play":66654,"pic":"http://i0.hdslb.com/bfs/archive/01459fecb12dcb97f43a47f2ca52f58087c10c2a.jpg","subtitle":"","description":"https://www.youtube.com/watch?v=L0FCwYKkZ4o\u0026t=23s\n\"Habitable order is generated by spoken truth. I think that's the truest thing I know.\"","copyright":"2","title":"注意力比思考更重要：为何要放弃生活剧本？","review":0,"author":"向杨Alan君","mid":495979610,"created":1634717595,"length":"07:35","video_review":83,"aid":848712848,"bvid":"BV1BL4y1B7VV","hide_click":false,"is_pay":0,"is_union_video":0,"is_steins_gate":0,"is_live_playback":0},{"comment":12,"typeid":228,"play":5500,"pic":"http://i1.hdslb.com/bfs/archive/2ab8c5b118dbe37ef85afe1c8e72bef852fdfe72.jpg","subtitle":"","description":"https://www.youtube.com/watch?v=9Gl2hbvPiQY\n\"You have to narrow yourself first, and then you can broaden outward.\"","copyright":"2","title":"如何看待专业上的瓶颈期？未经收敛，何谈自由","review":0,"author":"向杨Alan君","mid":495979610,"created":1634634224,"length":"03:34","video_review":1,"aid":378660091,"bvid":"BV1bf4y1g78h","hide_click":false,"is_pay":0,"is_union_video":0,"is_steins_gate":0,"is_live_playback":0},{"comment":127,"typeid":228,"play":80310,"pic":"http://i1.hdslb.com/bfs/archive/53cfee23003f730f73dba5cf9213faf3d3026d0b.jpg","subtitle":"","description":"https://www.youtube.com/watch?v=MJwGovFSGb8\n\"The important thing is to start improving incrementally because incremental improvement pays off like compound interest.\"","copyright":"2","title":"如何提升专注力？从早餐和微习惯入手","review":0,"author":"向杨Alan君","mid":495979610,"created":1634126418,"length":"05:35","video_review":74,"aid":208604765,"bvid":"BV1Kh411n7e9","hide_click":false,"is_pay":0,"is_union_video":0,"is_steins_gate":0,"is_live_playback":0},{"comment":7,"typeid":228,"play":470,"pic":"http://i1.hdslb.com/bfs/archive/ee59cf0dd34eeb3aa8ea80e6cc690ebc0e42dcb1.jpg","subtitle":"","description":"当然，除了上述三个原因，还有一个：阅读能帮你跳出当下既有的生活，了解探索其它更多的活法和可能性。","copyright":"1","title":"人天生不擅“阅读”，为何还要逆天而读？","review":0,"author":"向杨Alan君","mid":495979610,"created":1634021594,"length":"05:46","video_review":1,"aid":721122199,"bvid":"BV1MQ4y1z7jb","hide_click":false,"is_pay":0,"is_union_video":0,"is_steins_gate":0,"is_live_playback":0},{"comment":44,"typeid":228,"play":24526,"pic":"http://i2.hdslb.com/bfs/archive/4671868fff421595281455172cfcb83f186d24b2.jpg","subtitle":"","description":"https://www.youtube.com/watch?v=IFmQ5waavJY\u0026t=107s\n更多读书能力训练和学习视频，可以添加我的公众号：xy88chicago","copyright":"2","title":"为什么你总是无法集中注意力读书学习？自控力败给了潜意识","review":0,"author":"向杨Alan君","mid":495979610,"created":1633787018,"length":"05:38","video_review":18,"aid":975898025,"bvid":"BV1b44y1t7cj","hide_click":false,"is_pay":0,"is_union_video":0,"is_steins_gate":0,"is_live_playback":0},{"comment":81,"typeid":228,"play":46890,"pic":"http://i0.hdslb.com/bfs/archive/c5ab1da21140b6a5cadc0b7dc29b5e1ae6add2bc.jpg","subtitle":"","description":"https://www.youtube.com/watch?v=HOXwDWCoqQg\n问：学生如何学会犀利表达观点？\n答：学会写作","copyright":"2","title":"最高层次的思维锤炼：挑有争议的问题，然后严肃地写作","review":0,"author":"向杨Alan君","mid":495979610,"created":1633583344,"length":"06:28","video_review":33,"aid":590928334,"bvid":"BV1Qq4y1R7FB","hide_click":false,"is_pay":0,"is_union_video":0,"is_steins_gate":0,"is_live_playback":0},{"comment":1,"typeid":228,"play":226,"pic":"http://i2.hdslb.com/bfs/archive/d4eb2f18065cba58e5784badbe5f4b188f985c91.jpg","subtitle":"","description":"https://www.youtube.com/watch?v=9ix7TUGVYIo\n各种泪目的细节暗示","copyright":"2","title":"爷青回，《黑客帝国4：矩阵重生》电影预告","review":0,"author":"向杨Alan君","mid":495979610,"created":1632028381,"length":"02:53","video_review":0,"aid":208079055,"bvid":"BV1mh411p7YG","hide_click":false,"is_pay":0,"is_union_video":0,"is_steins_gate":0,"is_live_playback":0},{"comment":7,"typeid":228,"play":1549,"pic":"http://i0.hdslb.com/bfs/archive/737ce488675bb28beca8c37fc64a868bec275e71.jpg","subtitle":"","description":"https://www.youtube.com/watch?v=Ll0opgJ9_Ck\n30多岁生育和20多岁生育，培养孩子的模式会很不一样。如何做到不过度保护孩子，而且自己活的轻松。最关键的问题是，我们能否做到让自己爱的人活得轻松？","copyright":"2","title":"培养孩子：过度保护，不如“不称职得恰到好处”","review":0,"author":"向杨Alan君","mid":495979610,"created":1630238969,"length":"03:20","video_review":1,"aid":975209153,"bvid":"BV1J44y187h4","hide_click":false,"is_pay":0,"is_union_video":0,"is_steins_gate":0,"is_live_playback":0},{"comment":200,"typeid":228,"play":62770,"pic":"http://i2.hdslb.com/bfs/archive/65db970993f85d2afba3570a2897a6f548b421e3.jpg","subtitle":"","description":"https://www.youtube.com/watch?v=lMvvdz7YJ-Q\n不光是数理化，人文社科学习也要警惕“笔记陷阱”","copyright":"2","title":"告别无脑学习：勤做笔记，如何成了一种陋习？","review":0,"author":"向杨Alan君","mid":495979610,"created":1629981725,"length":"02:38","video_review":66,"aid":505101989,"bvid":"BV1Eg411L7Mm","hide_click":false,"is_pay":0,"is_union_video":0,"is_steins_gate":0,"is_live_playback":0},{"comment":0,"typeid":228,"play":218,"pic":"http://i1.hdslb.com/bfs/archive/b6e5fa2138abf510496bed87499a9c2deb34cfdc.jpg","subtitle":"","description":"希腊悲剧身上的酒神日神婚盟","copyright":"1","title":"领读尼采原著《悲剧的诞生》：四、二元冲动的斗争与和解","review":0,"author":"向杨Alan君","mid":495979610,"created":1628935822,"length":"21:05","video_review":0,"aid":674805570,"bvid":"BV19U4y1772a","hide_click":false,"is_pay":0,"is_union_video":0,"is_steins_gate":0,"is_live_playback":0},{"comment":2,"typeid":228,"play":136,"pic":"http://i1.hdslb.com/bfs/archive/17dfde40ffc1d44663b4a262c797ea39a6357a59.jpg","subtitle":"","description":"","copyright":"1","title":"领读尼采原著《悲剧的诞生》：三、用日神艺术美化生存的必要","review":0,"author":"向杨Alan君","mid":495979610,"created":1628924537,"length":"18:51","video_review":0,"aid":334874165,"bvid":"BV1UA411w7Zv","hide_click":false,"is_pay":0,"is_union_video":0,"is_steins_gate":0,"is_live_playback":0},{"comment":0,"typeid":228,"play":91,"pic":"http://i2.hdslb.com/bfs/archive/a1b2f2d2e3df5382c5bbab5c076db4497a3894e0.jpg","subtitle":"","description":"日神和酒神如何在希腊人的造型艺术中缔结合约","copyright":"1","title":"领读尼采原著《悲剧的诞生》：二、希腊人身上的二元艺术冲动","review":0,"author":"向杨Alan君","mid":495979610,"created":1628922119,"length":"18:44","video_review":0,"aid":674839313,"bvid":"BV1PU4y1E7Vr","hide_click":false,"is_pay":0,"is_union_video":0,"is_steins_gate":0,"is_live_playback":0},{"comment":1,"typeid":228,"play":246,"pic":"http://i1.hdslb.com/bfs/archive/4c9c567c908ac44fe1a8b4af66f5e687fd783eff.jpg","subtitle":"","description":"读懂早期的尼采，在《悲剧的诞生》中领悟悲剧的死亡","copyright":"1","title":"领读尼采原著《悲剧的诞生》：一、自然本身的二元艺术冲动","review":0,"author":"向杨Alan君","mid":495979610,"created":1628920155,"length":"28:14","video_review":0,"aid":249799029,"bvid":"BV1Jv411T7vp","hide_click":false,"is_pay":0,"is_union_video":0,"is_steins_gate":0,"is_live_playback":0},{"comment":0,"typeid":228,"play":198,"pic":"http://i1.hdslb.com/bfs/archive/f190025014ef451f006867623a45215f3f3f9bdb.jpg","subtitle":"","description":"https://www.youtube.com/watch?v=BCW4bf7YLU0\u0026t=2s","copyright":"2","title":"芝加哥大学魅力篇：智慧的起源","review":0,"author":"向杨Alan君","mid":495979610,"created":1628248928,"length":"01:46","video_review":0,"aid":632189557,"bvid":"BV11b4y1z7kq","hide_click":false,"is_pay":0,"is_union_video":0,"is_steins_gate":0,"is_live_playback":0}]},"page":{"pn":1,"ps":25,"count":68},"episodic_button":{"text":"播放全部","uri":"//www.bilibili.com/medialist/play/495979610?from=space"}}}

    out = snippets % (name, id, url, fans_num, likes_num,
                      plays_num, recharges_num, works_num)
    http_response.responsex(http.HTTP_STATUSCODE_200,
                            out)
