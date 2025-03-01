from typing import Iterable, Union


def filter_by_currency(user_transaction: Iterable[dict], currency: Union[str]) -> iter:
    """Функция-генератор возвращающая итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной"""
    for transaction in user_transaction:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(user_transaction: Iterable[dict]) -> iter:
    """Функция-генератор возвращающая описание каждой операции по очереди"""
    for transaction in user_transaction:
        yield transaction["description"]


def card_number_generator(start: Union[int], stop: Union[int]) -> str:
    """Функция-генератор генерирующая номер карты в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999"""
    for num in range(start, stop + 1):
        part_1 = (num // 1000000000000) % 10000
        part_2 = (num // 100000000) % 10000
        part_3 = (num // 10000) % 10000
        part_4 = num % 10000
        yield f"{part_1:04} {part_2:04} {part_3:04} {part_4:04}"

