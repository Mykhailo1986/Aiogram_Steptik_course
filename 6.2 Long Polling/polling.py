import requests
import time
import sys
sys.path.append(".")
from config import TOKEN


API_URL: str = 'https://api.telegram.org/bot'
BOT_TOKEN: str = TOKEN
offset: int = -2
updates: dict


def do_something() -> None:
    print('Був апдейт')


while True:
    start_time = time.time()
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            do_something()

    time.sleep(3)
    end_time = time.time()
    print(f'Час між запитами до Telegram Bot API: {end_time - start_time}')