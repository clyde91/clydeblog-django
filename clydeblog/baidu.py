import requests
import re
import time


def push_urls(urls):
    # 推送函数
    url = "http://data.zz.baidu.com/urls?site=https://www.clydeblog.com&token=HlDFQbjTdkpCQEpW"

    headers = {
        'User-Agent': 'curl/7.12.1',
        'Host': 'data.zz.baidu.com',
        'Content - Type': 'text / plain',
        'Content - Length': '83',
        'charset': 'gbk',
    }
    # http请求头
    try:
        response = requests.post(url, headers=headers, data=urls, timeout=5).text
        # 传输requests。url为接口地址。headers为http请求头。data为传输的数据。
        return response
    except Exception as e:
        print(e)


def auto_push_urls():
    # 自动提交xml内网站函数
    remain_push_count = 100000
    # 定义剩余可发布次数计数
    push_count = 0
    # 定义发布计数

    actual_push_url = 0
    # 定义发布的地址url

    # open a sitemap
    try:
        with open("sitemap.xml", "r", encoding="utf-8") as f:
        # 打开sitemap.xml文件。
            source_links = f.readlines()
            # 将读取每行内容存入source_links

    except Exception as e:

        print(e)

    else:
        # 无异常执行
        for link in source_links:
        # 循环每一行内容
            url = re.findall('<loc>(.*?)</loc>', link)
            # 截取<loc>(.*?)</loc>之间的网址存入url列表

            if url != []:
                # url列表不为空
                for i in url:
                    # 循环每一个网址。
                    target_url = i.encode("utf-8")
                    # 改成utf-8
                    response = push_urls(target_url)
                    # 提交该网址
                    print(f"psuh a url:{target_url}, {response}")

                    push_count += 1
                    actual_push_url += 1

                    if push_count > remain_push_count:
                        # 如果发布计数大于剩余可发布次数
                        break

    return actual_push_url


if __name__ == "__main__":
    print("start pushing urls ...")

    pushed_url_number = auto_push_urls()

    print(f"complete pushing urls: {pushed_url_number} ...")
