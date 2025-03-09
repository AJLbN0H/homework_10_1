from typing import Union
import json

API_KEY = '0YCpu6Z1zUZ4EcGkYsr508iGmNnm4qaz'

#user_path_to_json = '..\\data\\t.json'
#user_path_to_json = '..\\data\\test_2.json'
#user_path_to_json = '..\\data\\test.json'

user_path_to_json = '..\\data\\operations.json'
#user_path_to_json = str(input())


def json_file(path_to_json: Union[str]) -> list:
    """Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    transaction_list = []

    try:
        with open(path_to_json, 'r', encoding='utf-8') as f:
            transaction_list = json.load(f)
            if type(transaction_list) is not list:
                return []
    except FileNotFoundError:
        return []
    except ValueError:
        return []
    return transaction_list

transactions = json_file(user_path_to_json)
print(transactions)


def transaction_amount(transaction) -> float:
    """Функция которая принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях, тип данных — float.
     Если транзакция была в USD или EUR, происходит обращение к внешнему API для получения текущего курса валют и
     конвертации суммы операции в рубли"""
    sum_amount = 0.0

    if transaction['operationAmount']['currency']['code'] == 'RUB':
        sum_amount = transaction['operationAmount']['amount']

    return sum_amount



print(transaction_amount(transactions[0]))