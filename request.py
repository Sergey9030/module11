import requests
from pprint36 import pprint


username = 'sergey9030'  # Это я
url = f'https://api.github.com/users/{username}'

# Получаем данные
r = requests.get(url)

print('========== Результат выполнения запроса ===============')
print(f'Код статуса: {r.status_code}')
print(f'Content: {r.content}')  # Содержимое в виде байтовой последовательности
print(f'Text: {r.text}')
print(f'json(): {r.json()}')  # Содержимое в ввиде словаря
print('========== Заголовки ===============')
pprint(r.headers)

print('========== Печать данных ===============')
rj = r.json()
pprint(rj)

print('========== Выберем следующие данные ===============')
print('login ==', rj['login'])
print('id ==', rj['id'])
print('repos_url ==', rj['repos_url'])

print('========== Поcмотрим мои репозитории ===============')
rps = requests.get(rj['repos_url'])
#pprint(rps.json())  # Так ничего не понятно. Понятно, что это список.
for i in rps.json():
    print(i)

print('========== А тут куча словарей. Посмотрим какие у них ключи. ===============')
for i in rps.json()[0]:
    print(i, ':', rps.json()[0][i])

print('========== Выведем на печать имя репозитория, дату его создания и URL ==========')
for i in rps.json():
    print(f'Имя: {i['name']}; Создан: {i['created_at']}; URL: {i['html_url']};')
