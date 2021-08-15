# -*- coding:utf8 -*-
### 抓取豆瓣top标题
## 步骤：
# 1. 获取页面(request)
# 2. 把页面解析html(bs4)
# 3. 在解析后的页面中抓取指定内容
# 3. 使用for循环遍历出来  写入文件


import requests
import bs4

# import io
# import sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')


# 反爬虫
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/88.0.4324.190 Safari/537.36"}

res = requests.get("https://www.cnblogs.com/unixcs", headers=headers)  # 发起请求

# # print(res.text)           # 读取页面
# # print(res.status_code)    # 读取编码

soup = bs4.BeautifulSoup(res.text,
                         "html.parser")  # bs4.BeautifulSoup(页面对象.text，解析html)    # “html parser”是html解释器，帮你解析获取到的网页。

# 页数
# depth = soup.find('div', class_='pager').previous_sibling.previous_sibling.text


title = soup.find_all("div", class_="postTitle")  # 默认读取第一个参数(抓取标题)
content = soup.find_all("div", class_="c_b_p_desc")  # 默认读取第一个参数(抓取内容)

for each in title:  # 遍历出来
    # print(each.a.span.text, end="")   # 删除尾部 空格/换行符
    a = each.a.span.text.strip()  # strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
    print(a)  # 输出
list = []
for i in content:
    v = i.text.strip()
    print(v)
    list.append(v)


with open("blogs.txt", "w", encoding="utf-8") as f:
    for i in list:
        f.write(i)
        # f.write('\n')
