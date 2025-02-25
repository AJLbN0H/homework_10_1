from typing import Iterable

user_transaction_list = None


def filter_by_state(user_dict: Iterable[dict], state: str = "EXECUTED") -> Iterable[dict]:
    """Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению."""
    if user_dict is None or user_dict == "":
        return "Вы не ввели данные по транзакциям"
    try:
        dict_executed = []
        for element in user_dict:
            if element["state"] == state:
                dict_executed.append(element)
        if dict_executed == []:
            return "Транзакции отсутствуют"
        else:
            return dict_executed
    except KeyError:
        return "Транзакции отсутствуют"


# print(filter_by_state(user_transaction_list))


def sort_by_date(user_dict: Iterable[dict], reverse: bool = True) -> Iterable[dict]:
    """Функция возвращает список отсортированный по дате"""
    if user_dict is None or user_dict == "":
        return "Вы не ввели данные по транзакциям"
    else:
        seen_dates = set()
        unique_transaction = []

        for transaction in user_dict:
            if transaction["date"] not in seen_dates:
                seen_dates.add(transaction["date"])
                unique_transaction.append(transaction)

        return sorted(unique_transaction, key=lambda x: x["date"], reverse=reverse)


print(sort_by_date(user_transaction_list))
