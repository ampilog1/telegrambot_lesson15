import requests

TOKEN = '5787565526:AAEFoKR2CtyJqwFMUDmK9Cf2qvcMdILuEVg'
MAIN_URL = f'https://api.telegram.org/bot{TOKEN}'
url = f'{MAIN_URL}/getMe'
result = requests.get(url)
print(result.json())
