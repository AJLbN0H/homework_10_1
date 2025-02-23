import pytest

@pytest.fixture
def one_card_number():
    return '7000 79** **** 6361'

@pytest.fixture
def two_card_number():
    return '7123 78** **** 9961'

@pytest.fixture
def invalid_card_number_length():
    return 'Номер карты должен содержать 16 цифр'

@pytest.fixture
def no_card_number():
    return "Вы не ввели номер карты"