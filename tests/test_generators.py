from src.generators import filter_by_currency, transaction_descriptions


def test_filter_by_currency_usd(all_transactions):
    usd_transactions = filter_by_currency(all_transactions, "USD")
    assert next(usd_transactions) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(usd_transactions) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }
    assert next(usd_transactions) == {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    }
    assert (
        next(usd_transactions, "Транзакций с данной валютой нет или вы ее не указали")
        == "Транзакций с данной валютой нет или вы ее не указали"
    )


def test_filter_by_currency_rub(all_transactions):
    usd_transactions = filter_by_currency(all_transactions, "RUB")
    assert next(usd_transactions) == {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    }
    assert next(usd_transactions) == {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    }
    assert (
        next(usd_transactions, "Транзакций с данной валютой нет или вы ее не указали")
        == "Транзакций с данной валютой нет или вы ее не указали"
    )


def test_filter_by_currency(all_transactions):
    transactions = filter_by_currency(all_transactions, "")
    assert (
        next(transactions, "Транзакций с данной валютой нет или вы ее не указали")
        == "Транзакций с данной валютой нет или вы ее не указали"
    )


def test_filter_by_currency_no_transactions(no_transactions):
    transactions = filter_by_currency(no_transactions, "")
    assert next(transactions, "Список транзакций отсутсвует") == "Список транзакций отсутсвует"


def test_transaction_descriptions(all_transactions):
    transactions_info = transaction_descriptions(all_transactions)
    assert next(transactions_info) == "Перевод организации"
    assert next(transactions_info) == "Перевод со счета на счет"
    assert next(transactions_info) == "Перевод со счета на счет"
    assert next(transactions_info) == "Перевод с карты на карту"
    assert next(transactions_info) == "Перевод организации"
    assert (
        next(transactions_info, "Транзакций больше нет или нет информации о транзакции")
        == "Транзакций больше нет или нет информации о транзакции"
    )


def test_transaction_descriptions_no_transactions(no_transactions):
    transactions_info = transaction_descriptions(no_transactions)
    assert (
        next(transactions_info, "Транзакций больше нет или нет информации о транзакции")
        == "Транзакций больше нет или нет информации о транзакции"
    )
