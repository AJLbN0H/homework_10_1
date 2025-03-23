import csv
import logging
import os
from typing import Union

import pandas as pd

current_dir = os.path.dirname(os.path.abspath(__file__))
rel_file_path = os.path.join(current_dir, "..\\logs\\utils_csv_and_xlsx.log")
abs_file_path = os.path.abspath(rel_file_path)

logger = logging.getLogger()
file_handler = logging.FileHandler(abs_file_path, "w", encoding="utf-8")
file_formater = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def csv_file(patch_to_csv: Union[str]) -> list:
    """Принимает на вход путь до csv-файла и возвращает список словарей с данными о финансовых транзакциях"""

    csv_transactions_list = []

    try:
        with open(patch_to_csv, "r", encoding="utf-8") as file:
            transactions_list = csv.DictReader(file, delimiter=";")
            for transaction in transactions_list:
                if type(csv_transactions_list) is not list:
                    logger.error("В csv-файле находиться неверный тип данных")
                    return []

                id = int(transaction["id"])
                state = transaction["state"]
                date = transaction["date"]
                amount = str(transaction["amount"])
                currency_name = transaction["currency_name"]
                currency_code = transaction["currency_code"]
                from_val = transaction["from"]
                to_val = transaction["to"]
                description = transaction["description"]

                transactions = {
                    "id": id,
                    "state": state,
                    "date": date,
                    "operationAmount": {
                        "amount": amount,
                        "currency": {
                            "name": currency_name,
                            "code": currency_code,
                        },
                    },
                    "description": description,
                    "from": from_val,
                    "to": to_val,
                }

                csv_transactions_list.append(transactions)
    except FileNotFoundError:
        logger.error("csv-файла с таким именем не существует")
        return csv_transactions_list
    except ValueError:
        logger.error("В csv-файле находиться неверный тип данных")
        return csv_transactions_list

    logger.info(f"Список транзакций готов: {csv_transactions_list}")
    return csv_transactions_list


def xlsx_file(patch_to_xlsx: Union[str]) -> list:
    """Принимает на вход путь до xlsx-файла и возвращает список словарей с данными о финансовых транзакциях"""

    xlsx_transactions_list = []

    try:
        xlsx_data = pd.read_excel(patch_to_xlsx)
        transactions_list = xlsx_data.to_dict(orient="records")

        for transactions in transactions_list:

            id = int(transactions["id"])
            state = transactions["state"]
            date = transactions["date"]
            amount = str(transactions["amount"])
            currency_name = transactions["currency_name"]
            currency_code = transactions["currency_code"]
            from_val = transactions["from"]
            to_val = transactions["to"]
            description = transactions["description"]
            transaction = {
                "id": id,
                "state": state,
                "date": date,
                "operationAmount": {
                    "amount": amount,
                    "currency": {
                        "name": currency_name,
                        "code": currency_code,
                    },
                },
                "description": description,
                "from": from_val,
                "to": to_val,
            }

            xlsx_transactions_list.append(transaction)

        if type(xlsx_transactions_list) is not list:
            return []
    except KeyError:
        logger.error("В xlsx-файле находиться неверный тип данных")
        return []
    except FileNotFoundError:
        logger.error("xlsx-файла с таким именем не существует")
        return xlsx_transactions_list
    except ValueError:
        logger.error("В xlsx-файле находиться неверный тип данных")
        return xlsx_transactions_list

    logger.info(f"Список транзакций готов: {xlsx_transactions_list}")
    return xlsx_transactions_list
