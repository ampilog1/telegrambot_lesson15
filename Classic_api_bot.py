import requests
import pprint

TOKEN = '5787565526:AAEFoKR2CtyJqwFMUDmK9Cf2qvcMdILuEVg'
MAIN_URL = f'https://api.telegram.org/bot{TOKEN}'
url = f'{MAIN_URL}/getMe'
# result = requests.get(url)
# print(result.json())


url = f'{MAIN_URL}/getUpdates'

result = requests.get(url)
# pprint.pprint(result.json())
messages = result.json()['result']
# pprint.pprint(messages)
for message in messages:
    chat_id = message['message']['chat']['id']
    url = f'{MAIN_URL}/sendMessage'
    params = {
        'chat_id': chat_id,
        'text': 'Добрый день, Дмитрий!'
    }
    result = requests.post(url, params=params)
