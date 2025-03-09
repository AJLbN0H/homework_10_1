import os
import requests
from typing import Union

from dotenv import load_dotenv
load_dotenv()

def convert_usd_and_eur_in_rub(amount_transaction: Union[int], code_transaction: Union[str]) -> dict:

  header = {
    "apikey": os.getenv('API_KEY')
  }

  url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={code_transaction}&amount={amount_transaction}"
  response = requests.request("GET", url, headers=header)
  result_convert = response.json()

  #result = response.text
  #print(result)

  return result_convert