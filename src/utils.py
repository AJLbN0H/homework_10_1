import json
import logging
import os
from typing import Iterable, Union

from src.external_api import convert_usd_and_eur_in_rub

current_dir = os.path.dirname(os.path.abspath(__file__))
rel_file_path = os.path.join(current_dir, "..\\logs\\utils.log")
abs_file_path = os.path.abspath(rel_file_path)

logger = logging.getLogger()
file_handler = logging.FileHandler(abs_file_path, "w", encoding="utf-8")
file_formater = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def json_file(path_to_json: Union[str]) -> list:
    """Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""

    transaction_list = []

    try:
        with open(path_to_json, "r", encoding="utf-8") as f:
            transaction_list = json.load(f)
            if type(transaction_list) is not list:
                logger.error("В JSON-файле находиться неверный тип данных")
                return []

    except FileNotFoundError:
        logger.error("JSON-файла с таким именем не существует")
        return transaction_list
    except ValueError:
        logger.error("В JSON-файле находиться неверный тип данных")
        return transaction_list

    logger.info(f"Список транзакций готов: {transaction_list}")
    return transaction_list


def transaction_amount(transactions_: Iterable[list]) -> float:
    """Функция которая принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях, тип данных — float
    Если транзакция была в USD или EUR, происходит обращение к внешнему API для получения текущего курса валют и
    конвертации суммы операции в рубли"""

    try:
        transaction = transactions_[0]
    except IndexError:
        logger.error("Список транзакций пуст")
        return "Список транзакций пуст"
    except KeyError:
        logger.error("Список транзакций пуст")
        return "Список транзакций пуст"

    sum_amount = 0.0

    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        sum_amount = float(transaction["operationAmount"]["amount"])
    else:
        convert_amount = convert_usd_and_eur_in_rub(transaction)
        sum_amount = convert_amount["result"]

    logger.info(f"Сумма транзакции в рублях: {sum_amount}")
    return f"Сумма транзакции в рублях: {sum_amount}"
