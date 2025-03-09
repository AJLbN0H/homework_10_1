import json
from typing import Iterable, Union

from src.external_api import convert_usd_and_eur_in_rub

user_path_to_json = ""
# user_path_to_json = str(input())


def json_file(path_to_json: Union[str]) -> list:
    """Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""

    transaction_list = []

    try:
        with open(path_to_json, "r", encoding="utf-8") as f:
            transaction_list = json.load(f)
            if type(transaction_list) is not list:
                return []

    except FileNotFoundError:
        return transaction_list
    except ValueError:
        return transaction_list

    return transaction_list


transactions = json_file(user_path_to_json)
# print(transactions)


def transaction_amount(transactions_: Iterable[list]) -> float:
    """Функция которая принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях, тип данных — float
    Если транзакция была в USD или EUR, происходит обращение к внешнему API для получения текущего курса валют и
    конвертации суммы операции в рубли"""

    try:
        transaction = transactions_[0]
    except IndexError:
        return "Список транзакций пуст"
    except KeyError:
        return "Список транзакций пуст"

    sum_amount = 0.0

    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        sum_amount = float(transaction["operationAmount"]["amount"])
    else:
        convert_amount = convert_usd_and_eur_in_rub(transaction)
        sum_amount = convert_amount["result"]

    return sum_amount


transaction_amount(transactions)
# print(transaction_amount(transactions))
