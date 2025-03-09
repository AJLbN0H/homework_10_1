import os
from typing import Iterable

import requests
from dotenv import load_dotenv

load_dotenv()


def convert_usd_and_eur_in_rub(list_transaction: Iterable[dict]) -> dict:
    """Функция конвератации из USD или EUR в RUB"""

    code_transaction = list_transaction["operationAmount"]["currency"]["code"]
    amount_transaction = list_transaction["operationAmount"]["amount"]
    header = {"apikey": os.getenv("API_KEY")}

    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={code_transaction}&amount={amount_transaction}"
    response = requests.request("GET", url, headers=header)
    result_convert = response.json()

    return result_convert
