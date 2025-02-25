import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(transaction):
    assert (
        filter_by_state(
            [
                {
                    "id": 41428829,
                    "state": "EXECUTED",
                    "date": "2019-07-03T18:35:29.512364",
                }
            ]
        )
        == transaction
    )


@pytest.mark.parametrize(
    "transaction, if_executed",
    [
        (
            [
                {
                    "id": 41428829,
                    "state": "EXECUTED",
                    "date": "2019-07-03T18:35:29.512364",
                }
            ],
            [
                {
                    "id": 41428829,
                    "state": "EXECUTED",
                    "date": "2019-07-03T18:35:29.512364",
                }
            ],
        ),
        (
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                }
            ],
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                }
            ],
        ),
        (
            [
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                }
            ],
            "Транзакции отсутствуют",
        ),
        (
            [
                {
                    "id": 615064591,
                    "state": "CANCELED",
                    "date": "2018-10-14T08:21:33.419441",
                }
            ],
            "Транзакции отсутствуют",
        ),
        (
            [{"id": 594226727, "state": "", "date": "2018-09-12T21:27:25.241689"}],
            "Транзакции отсутствуют",
        ),
        (
            [{"id": 594226727, "date": "2018-09-12T21:27:25.241689"}],
            "Транзакции отсутствуют",
        ),
    ],
)
def test_parametrize_filter_by_state(transaction, if_executed):
    assert filter_by_state(transaction) == if_executed


def test_filter_by_state_one(transactions_are_missing):
    assert (
        filter_by_state(
            [
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                }
            ]
        )
        == transactions_are_missing
    )


def test_filter_by_state_no_transaction(no_transaction):
    assert filter_by_state(None) == no_transaction
    assert filter_by_state("") == no_transaction


def test_sort_by_date(sort_transactions_in_descending_order):
    assert (
        sort_by_date(
            [
                {
                    "id": 41428829,
                    "state": "EXECUTED",
                    "date": "2019-07-03T18:35:29.512364",
                },
                {
                    "id": 41428829,
                    "state": "EXECUTED",
                    "date": "2019-07-03T18:35:29.512364",
                },
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                },
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                },
                {
                    "id": 615064591,
                    "state": "CANCELED",
                    "date": "2018-10-14T08:21:33.419441",
                },
            ]
        )
        == sort_transactions_in_descending_order
    )


def test_reverse_sort_by_date(sort_transactions_in_ascending_order):
    assert (
        sort_by_date(
            [
                {
                    "id": 41428829,
                    "state": "EXECUTED",
                    "date": "2019-07-03T18:35:29.512364",
                },
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                },
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                },
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                },
                {
                    "id": 615064591,
                    "state": "CANCELED",
                    "date": "2018-10-14T08:21:33.419441",
                },
                {
                    "id": 615064591,
                    "state": "CANCELED",
                    "date": "2018-10-14T08:21:33.419441",
                },
            ],
            reverse=False,
        )
        == sort_transactions_in_ascending_order
    )


def test_test_sort_without_date(no_transaction):
    assert sort_by_date(None) == no_transaction
    assert sort_by_date("") == no_transaction
