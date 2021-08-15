# -*- coding:utf8 -*-
import requests
import bs4

# 反爬虫

cookie1 = """_zap=26ad836f-29d0-4bf8-b214-c777b5805a2c; d_c0="ANDYXkHtFBKPTmMC65sUXFsIWPFzJ0HLY6I=|1603422017"; z_c0="2|1:0|10:1603422088|4:z_c0|92:Mi4xSUZ0NUJRQUFBQUFBME5oZVFlMFVFaVlBQUFCZ0FsVk5oNVZfWUFBUldMYkFVNG9hOXBnZkdjS1c2RlFOdEZkWmhB|ff29f0f99ae2e6ea407fe6ee51e032df18eb1bee924a0f93d8bae35744bd7a40"; _xsrf=0CmwWsY0rmQeh4NYoOf43Zt1UVhitdFQ; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1607670113,1607670116,1607671136,1607676450; tst=h; tshl=; q_c1=a1b7f2362c7a4ceeb21f1d413814cb48|1614320573000|1603432964000; SESSIONID=siU7Dbb2fzLb45Tdo795sIKmmD9bp4sr3nqPDMFz9Qd; KLBRSID=b33d76655747159914ef8c32323d16fd|1614524285|1614524028; JOID=W14cA04iJ5Tn3ld8byskjB6FxP19XkHI1ZY6EVRIUteM724nBF-Oo47dV3pjOVXwPemzZzeXtNdKEwtbZN2DWow=; osd=UF4VC0opJ53v2lx8ZiMghx6MzPl2XkjA0Z06GFxMWdeF52osBFaGp4XdXnJnMlX5Ne24Zz6fsNxKGgNfb92KUog="""

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 "
                  "Safari/537.36 SE 2.X MetaSr 1.0", "Cookie": cookie1}

res = requests.get("https://www.zhihu.com/hot", headers=headers)  # 发起请求
soup = bs4.BeautifulSoup(res.text, "html.parser")  # 保存到text   html.parser 解析html
targets = soup.find_all("div", class_="HotItem-content")  # 读取第一个参数
i = 1
for each in targets:  # 遍历出来

    print("No.", i, ":", each.a.h2.text)  # 输出
    i += 1
