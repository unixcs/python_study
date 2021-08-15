# coding:utf-8
import requests
import bs4
#
# import io
# import sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')

# 抓取网页
def open_url(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0"}
    res = requests.get(url, headers=headers)

    return res


# 得到总页数
def find_depth(res):
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    depth = soup.find('span', class_='next').previous_sibling.previous_sibling.text

    return int(depth)


# 解析网页，提取内容
def find_movies(res):
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    names = []
    target = soup.find_all('div', class_='hd')
    for i in target:
        names.append(i.a.span.text)

    ranks = []
    target = soup.find_all('span', class_='rating_num')
    for i in target:
        ranks.append(i.text)

    messages = []
    target = soup.find_all('div', class_='bd')
    for i in target:
        try:
            messages.append(i.p.text.split('\n')[1].strip() + i.p.text.split('\n')[2].strip())
        except:
            continue

    result = []
    length = len(names)     # 电影名 总数量
    for i in range(length):
        result.append(names[i] + ',' + ranks[i] + ',' + messages[i] + '\n')

    return result           # 电影名 + 评分 + 介绍


def main():
    host = "https://movie.douban.com/top250"    # 目标url
    res = open_url(host)                        # 抓取网页
    depth = find_depth(res)                     # 获取总页数
    print(depth)

    result = []
    for i in range(depth):
        url = host + '/?start=' + str(25 * i)
        res = open_url(url)
        print(url)
        result.extend(find_movies(res))

        # 输出每个一电影的 result参数
        # for l in range(25*i,25*(i+1)):
        #     print(l)
        #     print(result[l])
        #     print("----"*10)
    with open("豆瓣TOP250电影.txt", 'w', encoding='utf-8') as f:
        for each in result:
            f.write(each)


if __name__ == "__main__":
    main()