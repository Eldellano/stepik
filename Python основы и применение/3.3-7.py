import re
import requests

url = input().strip()
pattern_link = r'(?:<a[^>]*href\s?=\s?[\'\"]?)(?:www\.)?(.+?:\/\/\-?)?([\w+\.\-]+)'
lst_out = []


def get_link(url):
    res = requests.get(url)
    match = re.findall(pattern_link, str(res.text))
    parse_link(match)


def parse_link(lst):
    for i in lst:
        if i[1] == '..':
            continue
        elif i[1] not in lst_out:
            lst_out.append(i[1])
    out(lst_out)


def out(lst):
    lst.sort()
    for i in lst:
        print(i)


get_link(url)
