from src.processing import filter_by_state
import pytest

def test_filter_by_state(transaction):
    assert filter_by_state(
        [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}]) == transaction

@pytest.mark.parametrize('transaction, if_executed', [
    ([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}], [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]),
    ([{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}], [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]),
    ([{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}], 'Транзакции отсутствуют'),
    ([{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}], 'Транзакции отсутствуют'),
    ([{'id': 594226727, 'state': '','date': '2018-09-12T21:27:25.241689'}], 'Транзакции отсутствуют'),
    ([{'id': 594226727, 'date': '2018-09-12T21:27:25.241689'}], 'Транзакции отсутствуют'),
])
def test_parametrize_filter_by_state(transaction, if_executed):
    assert filter_by_state(transaction) == if_executed

def test_filter_by_state_one():
    assert filter_by_state([{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}]) == 'Транзакции отсутствуют'

def test_filter_by_state_no_transaction(no_transaction):
    assert filter_by_state(None) == no_transaction
    assert filter_by_state('') == no_transaction