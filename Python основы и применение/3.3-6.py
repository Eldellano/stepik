import requests
import re

url_a = input()
url_b = input()
pattern = r'<a.*?href="([^"]*)'
lst = []


def get_link(url):
    try:
        if requests.get(url).status_code == 200:
            res = requests.get(url)
            lst = re.findall(pattern, str(res.content))
            if len(lst) > 0:
                return lst
            else:
                return []
    except:
        return []


def get_link_full():
    lst_link = get_link(url_a)
    for i in lst_link:
        if requests.get(i).status_code == 200:
            lst_full_link = get_link(i)
            if url_b in lst_full_link:
                return True
    return False


if get_link_full():
    print('Yes')
else:
    print('No')
