import requests

API_KEY = '0YCpu6Z1zUZ4EcGkYsr508iGmNnm4qaz'

#url = "https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from}&amount={amount}"

#amount = "Сумма, подлежащая конвертации"
#to = "RUB" #Трехбуквенный код валюты, в которую вы хотите конвертировать.
#from_ = "Трехбуквенный код валюты, которую вы хотите конвертировать"

#header= {
  #"apikey": API_KEY
#}

#response = requests.request("GET", url, headers=header, data = payload)

def convert_usd_and_eur_in_rub(amount_transaction, code_transaction):
  amount = amount_transaction #"Сумма, подлежащая конвертации"
  from_ = code_transaction #"Трехбуквенный код валюты, которую вы хотите конвертировать"
  header = {
    "apikey": API_KEY
  }
  url = "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={from_}&amount={amount}"
  response = requests.request("GET", url, headers=header)

  status_code = response.status_code
  result = response.text