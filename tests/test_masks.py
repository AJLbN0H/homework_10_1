from src.masks import get_mask_card_number, get_mask_account


def test_one_get_mask_card_number(one_card_number):
    assert get_mask_card_number(7000792289606361) == one_card_number

def test_two_get_mask_card_number(two_card_number):
    assert get_mask_card_number(7123788289609961) == two_card_number

def test_invalid_card_number_length(invalid_card_number_length):
    assert get_mask_card_number(71237882896099611) == invalid_card_number_length
    assert get_mask_card_number(712378828960996) == invalid_card_number_length

def test_get_masked_without_card_number(no_card_number):
    assert get_mask_card_number("") == no_card_number
    assert get_mask_card_number(None) == no_card_number


def test_get_mask_account(account_number):
    assert get_mask_account(73654108430135874305) == account_number