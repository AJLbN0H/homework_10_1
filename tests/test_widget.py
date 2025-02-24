from src.widget import mask_account_card


def test_mask_number_card(name_and_number_card):
    assert mask_account_card('Visa Platinum 7000792289606361') == name_and_number_card

def test_mask_account_number(name_and_number_account):
    assert mask_account_card('Счет 73654108430135874305') == name_and_number_account