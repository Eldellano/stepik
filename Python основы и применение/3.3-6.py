import requests
import re

url_a = input()
url_b = input()
pattern = r'sample\d'

res_a = requests.get(url_a)
res_b = requests.get(url_b)
match_a = re.findall(pattern, str(res_a.content))
match_b_cont = re.search(pattern, str(res_b.content))
match_b = re.search(pattern, str(url_b))

for i in match_a:
    if i != match_b.group() or match_b.group() == match_b_cont.group():
        print('Yes')
    # elif match_b.group() == match_b_cont.group():
    #     print('Yes')
    else:
        print('No')
