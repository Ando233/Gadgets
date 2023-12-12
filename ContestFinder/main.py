import json
import httpx
import requests
from bs4 import BeautifulSoup
from prettytable import *
import re
import time as tm
from datetime import datetime
import pytz

data = []

def uniform_name(name, type):
    if type == 2:
        if name.find("AtCoder Beginner Contest") != -1:
            name = "AtCoder Beginner Contest"
        if name.find("AtCoder Grand Contest") != -1:
            name = "AtCoder Grand Contest"
        if name.find("AtCoder Regular Contest") != -1:
            name = "AtCoder Regular Contest"
    name = re.sub('[\r\t\n]', '', name)[0:35]

    return name


# type 0cf 1nk 2atc
def uniform_time(time, type):
    time = re.sub('[\r\t\n]', '', time)
    if type == 0:
        time = datetime.strptime(time, "%b/%d/%Y %H:%M")
    if type == 1:
        time = time.split('：')[1].split("至")[0].strip(' ')
        time = datetime.strptime(time, "%Y-%m-%d %H:%M")
    if type == 2:
        time = time.split('+')[0]
        time = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")

    return time



def get_cf_contest():
    # codeforces
    url = "https://codeforces.com/contests"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    contest_rows = soup.find("table").find_all("tr")
    for row in contest_rows[1:]:
        cells = row.find_all("td")
        name = cells[0].get_text()
        name = uniform_name(name, 0)
        time = cells[2].get_text()
        time = uniform_time(time, 0)

        data.append({"name": name, "time": time, "source": "codeforces"})


def get_nk_contest():
    # 牛客
    url = "https://ac.nowcoder.com/acm/contest/vip-index"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    contest_rows = soup.find("div", {"class": "platform-mod"}).find_all("div", {"class": "platform-item-cont"})
    for row in contest_rows:
        name = row.find("a").get_text()
        name = uniform_name(name, 1)
        time = row.find("li", {"class": "match-time-icon"}).get_text()
        time = uniform_time(time, 1)

        data.append({"name": name, "time": time, "source": "牛客"})


def get_atc_contest():
    # atcoder
    url = "https://atcoder.jp/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    contest_rows = soup.find("div", {"id": "contest-table-upcoming"}).find_all("tr")
    for row in contest_rows[1:]:
        cells = row.find_all("td")
        name = cells[1].find("a").get_text()
        name = uniform_name(name, 2)
        time = cells[0].find("time").get_text()
        time = uniform_time(time, 2)

        data.append({"name": name, "time": time, "source": "atcoder"})


def get_lc_contest():
    url_data = "https://leetcode-cn.com/graphql"
    payload = {
        "operationName": "null",
        "query": "{\n  contestUpcomingContests {\n    containsPremium\n    title\n    cardImg\n    titleSlug\n    description\n    startTime\n    duration\n    originStartTime\n    isVirtual\n    isLightCardFontColor\n    company {\n      watermark\n      __typename\n    }\n    __typename\n  }\n}\n",
        "variables": {}
    }
    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip,deflate,br",
        "accept-language": "zh,zh-TW;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6",
        "cache-control": "no-cache",
        # "content-length": "329",
        "content-type": "application/json",
        # "cookie": response.cookies,
        "origin": "https://leetcode-cn.com",
        "pragma": "no-cache",
        "referer": "https://leetcode-cn.com/contest/",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36",
        # 'x-csrftoken': response.cookies
    }

    response = httpx.Client().post(url=url_data, data=json.dumps(payload), headers=headers)

    url_text = response.content.decode()
    contest_rows = json.loads(url_text)["data"]["contestUpcomingContests"]
    for row in contest_rows:
        name = row["title"]
        time = row["startTime"]
        time = datetime.fromtimestamp(time)

        data.append({"name": name, "time": time, "source": "leetcode"})


# def get_lg_contest():


def print_table():
    data.sort(key=lambda x: x['time'])
    tb = PrettyTable(["name", "time", "source"])
    columns = list(data[0].keys())
    for row in data:
        tb.add_row([row[column] for column in columns])
    print(tb)


if __name__ == '__main__':
    get_cf_contest()
    get_nk_contest()
    get_atc_contest()
    get_lc_contest()
    # get_lg_contest()
    print_table()
