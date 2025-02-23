user_card_number = None
from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """Функция маскировки номера банковской карты"""
    if card_number is None or card_number == "":
        return "Вы не ввели номер карты"
    else:
        str_card_number = str(card_number)
        cleaned_number = ""
        for num in str_card_number:
            if num.isdigit():
                cleaned_number += num
        if len(cleaned_number) != 16:
            return "Номер карты должен содержать 16 цифр"
        else:
            masked_number = f"{str_card_number[0:4]} {str_card_number[4:6]}** **** {str_card_number[-4::]}"
            return masked_number

print(get_mask_card_number(user_card_number))

user_account_number = None


def get_mask_account(account_number: Union[int, str]) -> str:
    """Функция маскировки номера банковского счета"""
    str_account_number = str(account_number)

    return f"**{str_account_number[-4::]}"


print(get_mask_account(user_account_number))
