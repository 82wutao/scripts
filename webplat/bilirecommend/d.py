# https://www.bilibili.com/video/BV1Vg411N7Yf?spm_id_from=333.851.b_7265636f6d6d656e64.2
from typing import Dict
import httpcli

query = {
    "spm_id_from": "333.851.b_7265636f6d6d656e64.2",
}
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


def show(status: int, reason: str, headers: Dict[str, str], body: bytes):
    print(headers["Content-Type"])
    print(headers["Content-Encoding"])
    t = body.decode('utf-8')
    print(t)
    pass


httpcli.https_get("www.bilibili.com", 443,
                  "video/BV1Vg411N7Yf", query, __headers, show)
