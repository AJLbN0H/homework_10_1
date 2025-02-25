from src.masks import get_mask_account, get_mask_card_number


def test_one_get_mask_card_number(one_card_number):
    assert get_mask_card_number("7000792289606361") == one_card_number


def test_two_get_mask_mix_card_number(two_mix_card_number):
    assert get_mask_card_number("7123 7882_8960-9961") == two_mix_card_number


def test_invalid_card_number_length(invalid_card_number_length):
    assert get_mask_card_number("71237882896099611") == invalid_card_number_length
    assert get_mask_card_number("712378828960996") == invalid_card_number_length


def test_get_masked_without_card_number(no_card_number):
    assert get_mask_card_number("") == no_card_number
    assert get_mask_card_number(None) == no_card_number


def test_get_mask_account(account_number):
    assert get_mask_account("73654108430135874305") == account_number


def test_get_mask_mix_account(account_number):
    assert get_mask_account("7365 4108_4301-3587*4305") == account_number


def test_get_smaller_mask_account(invalid_account_number_length):
    assert get_mask_account("7365410843013587430") == invalid_account_number_length
    assert get_mask_account("736541084301358743055") == invalid_account_number_length


def test_get_mask_no_account(no_account_number):
    assert get_mask_account("") == no_account_number
    assert get_mask_account(None) == no_account_number
