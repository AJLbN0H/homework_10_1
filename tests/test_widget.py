from src.widget import mask_account_card, get_date
import pytest

def test_mask_number_card(name_and_number_card):
    assert mask_account_card('Visa Platinum 7000792289606361') == name_and_number_card

def test_mask_account_number(name_and_number_account):
    assert mask_account_card('Счет 73654108430135874305') == name_and_number_account

@pytest.mark.parametrize('unmasked_card_or_account, masked_card_or_account', [
    ('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
    ('MasterCard 7158300734726758', 'MasterCard 7158 30** **** 6758'),
    ('Visa Classic 6831982476737658', 'Visa Classic 6831 98** **** 7658'),
    ('Visa Platinum 8990922113665229', 'Visa Platinum 8990 92** **** 5229'),
    ('Visa Gold 5999414228426353', 'Visa Gold 5999 41** **** 6353'),
    ('Счет 64686473678894779589', 'Счет **9589'),
    ('Счет 35383033474447895560', 'Счет **5560'),
    ('Счет 73654108430135874305', 'Счет **4305'),
])
def test_card_number_or_account_number(unmasked_card_or_account, masked_card_or_account):
    assert mask_account_card(unmasked_card_or_account) == masked_card_or_account

@pytest.mark.parametrize('unmasked_card_or_account, invalid_masked_card_or_account', [
    ('Maestro 1596837868---705195756567', 'Номер карты должен содержать 16 цифр'),
    ('MasterCard 715830073', 'Номер карты должен содержать 16 цифр'),
    ('MasterCard ', 'Номер карты должен содержать 16 цифр'),
    ('Mast ', 'Номер карты должен содержать 16 цифр'),
    ('', 'Введите тип и номер карты или номер счета'),
    ('Счет 646864736788___94779', 'Номер счета должен содержать 20 цифр'),
    ('Счет 3538303347444789556065776', 'Номер счета должен содержать 20 цифр'),
    ('Счет ', 'Номер счета должен содержать 20 цифр'),
    ('Сч', 'Номер счета должен содержать 20 цифр'),
])
def test_invalid_card_number_or_account_number(unmasked_card_or_account, invalid_masked_card_or_account):
    assert mask_account_card(unmasked_card_or_account) == invalid_masked_card_or_account


def test_get_date(date):
    assert get_date('2024-03-11T02:26:18.671407') == date