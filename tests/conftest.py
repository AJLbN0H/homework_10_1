import pytest

@pytest.fixture
def one_card_number():
    return '7000 79** **** 6361'

@pytest.fixture
def two_mix_card_number():
    return '7123 78** **** 9961'

@pytest.fixture
def invalid_card_number_length():
    return 'Номер карты должен содержать 16 цифр'

@pytest.fixture
def no_card_number():
    return 'Вы не ввели номер карты'



@pytest.fixture
def account_number():
    return '**4305'

@pytest.fixture
def mix_account_number():
    return '**4305'

@pytest.fixture
def invalid_account_number_length():
    return 'Неверно указан номер счета'

@pytest.fixture
def smaller_account_number():
    return '**8947'

@pytest.fixture
def no_account_number():
    return 'Вы не ввели номер счета'



@pytest.fixture
def name_and_number_card():
    return 'Visa Platinum 7000 79** **** 6361'

@pytest.fixture
def name_and_number_account():
    return 'Счет **4305'