user_card_number_or_account_number = None
from typing import Union

#user_card_number_or_account_number = str(input())


def mask_account_card(card_number_or_account_number: Union[str]) -> str:
    """Замаскировывает номер банковской карты или счета"""
    if card_number_or_account_number is None or card_number_or_account_number == '':
        return 'Введите тип и номер карты или номер счета'
    else:
        split_card_number_or_account_number = card_number_or_account_number.split()
        number = split_card_number_or_account_number[-1]

        if "Счет" in card_number_or_account_number:
            masked_number = f"**{number[-4::]}"
        else:
            masked_number = f"{number[0:4]} {number[4:6]}** **** {number[-4::]}"

    split_card_number_or_account_number[-1] = masked_number
    return " ".join(split_card_number_or_account_number)


print(mask_account_card(user_card_number_or_account_number))

#user_date = None
#user_date = str(input())


#def get_date(date: Union[str]) -> str:
    #"""Возврощает строку с датой"""

    #return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"


#print(get_date(user_date))
