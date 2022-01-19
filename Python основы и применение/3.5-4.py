import requests
import json

client_id = '803283e11d63896eb274'
client_secret = 'f906fc05c0bc7262579a597f1c0b1a15'
name_lst = []

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]


def get_name(token, id):
    headers = {"X-Xapp-Token": token}
    r = requests.get(f"https://api.artsy.net/api/artists/{id}", headers=headers)

    name_lst.append([r.json()['birthday'], r.json()['sortable_name']])


with open('dataset_24476_4.txt', 'r') as file:
    for line in file:
        get_name(token, line.strip())
name_lst.sort()

for i in name_lst:
    print(i[1])
