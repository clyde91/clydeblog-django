import requests
import re
import time


def push_urls(urls):
    url = "http://data.zz.baidu.com/urls?site=https://www.clydeblog.com&token=HlDFQbjTdkpCQEpW"

    headers = {
        'User-Agent': 'curl/7.12.1',
        'Host': 'data.zz.baidu.com',
        'Content - Type': 'text / plain',
        'Content - Length': '83',
        'charset': 'gbk',
    }

    try:
        response = requests.post(url, headers=headers, data=urls, timeout=5).text
        return response
    except Exception as e:
        print(e)


def auto_push_urls():
    remain_push_count = 100000
    push_count = 0
    start_number = 608006

    actual_push_url = 0

    # open a sitemap
    try:
        with open("sitemap.xml", "r", encoding="utf-8") as f:
            source_links = f.readlines()

    except Exception as e:

        print(e)

    else:
        for link in source_links[start_number]:

            url = re.findall('<loc>(.*?)</loc>', link)

            if url != []:
                target_url = url[0].encode("utf-8")
                response = push_urls(target_url)
                #                 print(url[0])
                print(f"psuh a url:{target_url}, {response}")

                push_count += 1
                actual_push_url += 1

                if push_count > remain_push_count:
                    break

    return actual_push_url


if __name__ == "__main__":
    print("start pushing urls ...")

    pushed_url_number = auto_push_urls()

    print(f"complete pushing urls: {pushed_url_number} ...")