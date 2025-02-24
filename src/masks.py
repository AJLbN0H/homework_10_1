user_card_number = None
#user_card_number = str(input())
from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """Функция маскировки номера банковской карты"""
    if card_number is None or card_number == "":
        return "Вы не ввели номер карты"
    else:
        cleaned_number = ""
        for num in card_number:
            if num.isdigit():
                cleaned_number += num
        if len(cleaned_number) != 16:
            return "Номер карты должен содержать 16 цифр"
        else:
            masked_number = f"{cleaned_number[0:4]} {cleaned_number[4:6]}** **** {cleaned_number[-4::]}"
            return masked_number

print(get_mask_card_number(user_card_number))

user_account_number = None
#user_account_number = str(input())


def get_mask_account(account_number: Union[int, str]) -> str:
    """Функция маскировки номера банковского счета"""
    if account_number is None or account_number == '':
        return 'Вы не ввели номер счета'
    else:
        if len(account_number) < 6:
            return 'Неверно указан номер счета'
        else:
            return f"**{account_number[-4::]}"


print(get_mask_account(user_account_number))
