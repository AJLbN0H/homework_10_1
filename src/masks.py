import logging
from typing import Union

logger = logging.getLogger()
file_handler = logging.FileHandler("..\\logs\\masks.log", "w", encoding="utf-8")
file_formater = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: Union[None, str]) -> str:
    """Функция маскировки номера банковской карты"""

    if card_number is None or card_number == "":
        logger.error("Вы не ввели номер карты")
        return "Вы не ввели номер карты"
    else:
        cleaned_card_number = ""

        for num in card_number:
            if num.isdigit():
                cleaned_card_number += num

        if len(cleaned_card_number) != 16:
            logger.error("Номер карты должен содержать 16 цифр")
            return "Номер карты должен содержать 16 цифр"
        else:
            logger.info(
                f"Замаскированный номер вашей карты выглядит вот так: "
                f"{cleaned_card_number[0:4]} {cleaned_card_number[4:6]}** **** {cleaned_card_number[-4::]}"
            )
            return f"{cleaned_card_number[0:4]} {cleaned_card_number[4:6]}** **** {cleaned_card_number[-4::]}"


def get_mask_account(account_number: Union[None, str]) -> str:
    """Функция маскировки номера банковского счета"""

    if account_number is None or account_number == "":
        logger.error("Вы не ввели номер счета")
        return "Вы не ввели номер счета"
    else:
        cleaned_account_number = ""

        for num in account_number:
            if num.isdigit():
                cleaned_account_number += num

        if len(cleaned_account_number) != 20:
            logger.error("Номер счета должен содержать 20 цифр")
            return "Номер счета должен содержать 20 цифр"
        else:
            logger.info(f"Замаскированный номер вашего счета выглядит вот так: **{account_number[-4::]}")
            return f"**{account_number[-4::]}"
