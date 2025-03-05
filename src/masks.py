from typing import Union

user_card_number = None
# user_card_number = str(input())


def get_mask_card_number(card_number: Union[None, str]) -> str:
    """Функция маскировки номера банковской карты"""
    if card_number is None or card_number == "":
        return "Вы не ввели номер карты"
    else:
        cleaned_card_number = ""
        for num in card_number:
            if num.isdigit():
                cleaned_card_number += num
        if len(cleaned_card_number) != 16:
            return "Номер карты должен содержать 16 цифр"
        else:
            return f"{cleaned_card_number[0:4]} {cleaned_card_number[4:6]}** **** {cleaned_card_number[-4::]}"


print(get_mask_card_number(user_card_number))


def get_mask_account(account_number: Union[None, str]) -> str:
    """Функция маскировки номера банковского счета"""
    if account_number is None or account_number == "":
        return "Вы не ввели номер счета"
    else:
        cleaned_account_number = ""
        for num in account_number:
            if num.isdigit():
                cleaned_account_number += num
        if len(cleaned_account_number) != 20:
            return "Номер счета должен содержать 20 цифр"
        else:
            return f"**{account_number[-4::]}"


if __name__ == "__masks__":
    user_card_number = None
    # user_card_number = str(input())
    print(get_mask_card_number(user_card_number))

    user_account_number = None
    # user_account_number = str(input())
    print(get_mask_account(user_account_number))
