import re
from collections import Counter
from typing import Iterable, Union


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
        str_categories = "".join(category)

        transaction = search_by_list_description(transactions, str_categories)

        for i in range(len(transaction)):
            counter_description.update([category])

    return dict(counter_description)
