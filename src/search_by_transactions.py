from typing import Iterable, Union
import re
from collections import Counter
from src.utils import json_file
from src.utils_csv_and_xlsx import csv_file, xlsx_file


def search_by_list_description(transactions: Iterable[list], search_string: Union[str]) -> list:
    """Функция, которая принимает список словарей с данными о банковских операциях и строку поиска, а возвращает список
    словарей с операциями, у которых в описании есть данная строка"""
    pattern = re.compile(rf"{search_string}", re.IGNORECASE)

    result = [transaction for transaction in transactions if pattern.search(transaction.get("description", ""))]

    return result


def counting_transaction_categories(transactions: Iterable[list], categories: list[str]) -> dict[str, int]:
    """Функция, которая принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории"""
    counter_description = Counter(list())

    for category in categories:
        string_categories = "".join(category)

        transact = (search_by_list_description(transactions, string_categories))

        for cat in range(len(transact)):
            counter_description.update([category])

    return dict(counter_description)


if __name__ == "__main__":
    user_transaction_list = json_file("..\\data\\operations.json")

    user_search_string = "Открытие вклада"
    print(search_by_list_description(user_transaction_list, user_search_string))

    user_search_categories = ["Открытие вклада", "Перевод организации", "Перевод со счета на счет"]
    print(counting_transaction_categories(user_transaction_list, user_search_categories))
