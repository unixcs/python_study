import requests
import json


def get_url(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/92.0.4515.131 Safari/537.36",
        "referer": "https://music.163.com/song?id=1400453707"}

    params = {"C8Hf0yMal/Wj4F1IGuIqzI++320zdK7b2mydxGaD56u3VSMbtQGgTHytiVPFq8"
              "/rRvGiVvhxZJSA4CWNaoENCiqgWLY8j1y9dcMIVUeAkb1C8LfLuSB9jN4czULefhmt9mhAWSH99B16pgrljLpmH"
              "/ZahBlniIWwHoIBZ8b6CrvQmvu2jj8JCN8d5R0LX/kdVYpn2crUDmtgsyjEQ0gVx0rbTluKF9EYxCHaFjyqRcm/+2rL"
              "+TxbwoYTCif8p7XwGozNOoZ+WxiT6Bi/AWRIeWa9nSDtI2NHfGejyU8HK5LgjbSEvOHwuFQNuWw8Vf3z5EUuN+KDTbF"
              "+diNOhaitevHWpOEX/p3EfArfg5/GoCE="}
    encSecKey = {"57e23db86f21952f8470c983130bb91adc9ac744cfa3c5cb3371155c2a7de05e1155a14ed969ba9f4675bc28e9a19b7aa41cf20dfb8a648d9c709c52f59ca3ec601f7c63e3dcea611cf41696bd07edff89f8ac669cb008d43ad656dfdedf4b45b23d2eb155925a20310e78eb387874f3d8e1fbf615bcb1f3a1977e7c10fd93c3"}
    data = {
        "params": params,
        "encSecKey": encSecKey

    }

    urls = "https://music.163.com/api/comment/resource/comments/get?csrf_token=af88b3fcf2a48d56e3446bf940655558"

    res = requests.get(urls, headers=headers, data=data)

    return res


def main():
    url = input("请输入音乐地址")
    res = get_url(url)

    with open("music.txt", "w", encoding="utf-8") as f:
        f.write(res.text)


main()
