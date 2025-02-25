from typing import Union

from src.masks import get_mask_account, get_mask_card_number

user_card_number_or_account_number = None
# user_card_number_or_account_number = str(input())


def mask_account_card(card_number_or_account_number: Union[str]) -> str:
    """Замаскировывает номер банковской карты или счета"""
    if card_number_or_account_number is None or card_number_or_account_number == "":
        return "Введите тип и номер карты или номер счета"
    else:
        split_card_number_or_account_number = card_number_or_account_number.split()
        number = split_card_number_or_account_number[-1]

        if "с" in card_number_or_account_number.lower() or len(number) == 20:
            masked_number = get_mask_account(number)  # f"**{number[-4::]}"
            if masked_number == "Номер счета должен содержать 20 цифр":
                return masked_number
            else:
                split_card_number_or_account_number[-1] = masked_number
                return " ".join(split_card_number_or_account_number)

        else:
            masked_number = get_mask_card_number(number)  # f"{number[0:4]} {number[4:6]}** **** {number[-4::]}"
            if masked_number == "Номер карты должен содержать 16 цифр":
                return masked_number
            else:
                split_card_number_or_account_number[-1] = masked_number
                return " ".join(split_card_number_or_account_number)


print(mask_account_card(user_card_number_or_account_number))


user_date = None
# user_date = str(input())


def get_date(date: Union[str]) -> str:
    """Возврощает строку с датой"""
    if date is None or date == "":
        return "Вы не ввели дату"
    else:
        date = date[:10].split("-")
        return ".".join(reversed(date))


print(get_date(user_date))
