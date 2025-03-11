import pytest


@pytest.fixture
def one_card_number():
    return "Замаскированный номер вашей карты выглядит вот так: 7000 79** **** 6361"


@pytest.fixture
def two_mix_card_number():
    return "Замаскированный номер вашей карты выглядит вот так: 7123 78** **** 9961"


@pytest.fixture
def invalid_card_number_length():
    return "Номер карты должен содержать 16 цифр"


@pytest.fixture
def no_card_number():
    return "Вы не ввели номер карты"


@pytest.fixture
def account_number():
    return "Замаскированный номер вашего счета выглядит вот так: **4305"


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


@pytest.fixture
def all_transactions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


@pytest.fixture
def no_transactions():
    return []
