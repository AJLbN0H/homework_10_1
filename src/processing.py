from typing import Iterable


user_transaction_list = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

def filter_by_state(user_dict: Iterable[dict], state:str='EXECUTED') -> Iterable[dict]:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state соответствует указанному значению."""
    dict_executed = []
    for element in user_dict:
        if element['state'] == state:
            dict_executed.append(element)
    return dict_executed


print(filter_by_state(user_transaction_list))


def sort_by_date(user_dict: Iterable[dict], reverse: bool = True) -> Iterable[dict]:
    """Функция возвращает список отсортированный по дате"""
    return sorted(user_dict, key = lambda x: x['date'], reverse=reverse)


print(sort_by_date(user_transaction_list))
