import requests
import time
from config import *

API_URL: str = 'https://api.telegram.org/bot'
BOT_TOKEN: str = TOKEN
API_CATS_URL: str = 'https://api.thecatapi.com/v1/images/search'
ERROR_TEXT: str = 'Here is gonna be a cat :('
MAX_COUNTER: int = 100

offset: int = -2
counter: int = 0
chat_id: int
cat_link: str

while counter < MAX_COUNTER:

    print('attempt =', counter)

    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset+1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            cat_response = requests.get(API_CATS_URL)
            if cat_response.status_code == 200:
                cat_link = cat_response.json()[0]['url']
                print(cat_link)
                requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
            else:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')

    time.sleep(1)
    counter += 1
