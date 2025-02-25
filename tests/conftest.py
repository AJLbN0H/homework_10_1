import pytest


@pytest.fixture
def one_card_number():
    return "7000 79** **** 6361"


@pytest.fixture
def two_mix_card_number():
    return "7123 78** **** 9961"


@pytest.fixture
def invalid_card_number_length():
    return "Номер карты должен содержать 16 цифр"


@pytest.fixture
def no_card_number():
    return "Вы не ввели номер карты"


@pytest.fixture
def account_number():
    return "**4305"


@pytest.fixture
def invalid_account_number_length():
    return "Номер счета должен содержать 20 цифр"


@pytest.fixture
def smaller_account_number():
    return "**8947"


@pytest.fixture
def no_account_number():
    return "Вы не ввели номер счета"


@pytest.fixture
def type_and_number_card():
    return "Visa Platinum 7000 79** **** 6361"


@pytest.fixture
def type_and_number_account():
    return "Счет **4305"


@pytest.fixture
def date():
    return "11.03.2024"


@pytest.fixture
def no_date():
    return "Вы не ввели дату"


@pytest.fixture
def transaction():
    return [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}]


@pytest.fixture
def transactions_are_missing():
    return "Транзакции отсутствуют"


@pytest.fixture
def no_transaction():
    return "Вы не ввели данные по транзакциям"


@pytest.fixture
def sort_transactions_in_descending_order():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def sort_transactions_in_ascending_order():
    return [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]
