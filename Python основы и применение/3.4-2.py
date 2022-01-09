import csv
import re
from collections import Counter

date = r'(.{6}2015.+)'
crime_type = []
with open('Crimes.csv') as file:
    reader = csv.reader(file)
    for i in reader:  # Перебираем строки, выбираем нужную даду, добавляем преступление в список
        match = re.findall(date, i[2])
        if len(match) > 0:
            crime_type.append(i[5])

cnt = Counter(crime_type)  # Получаем число повторений
for key, values in cnt.items():  # Перебираем словарь, выводим ключ по максимальному значению повторений
    if values == max(cnt.values()):
        print(key)
