import csv
import pandas as pd
from typing import Union


#user_patch_to_csv = '..\\data\\transactions.csv'
user_patch_to_csv = ''


def csv_file(patch_to_csv: Union[str]) -> list:
    """Принимает на вход путь до csv-файла и возвращает список словарей с данными о финансовых транзакциях"""

    csv_transactions_list = []

    with open(patch_to_csv, 'r', encoding='utf-8') as file:
        transactions_list = csv.DictReader(file)
        for transaction in transactions_list:
            csv_transactions_list.append(transaction)

    return csv_transactions_list

csv_file(user_patch_to_csv)
#print(csv_file(user_patch_to_csv))

user_patch_to_xlsx = ''
#user_patch_to_xlsx = '..\\data\\transactions_excel.xlsx'

def xlsx_file(patch_to_xlsx: Union[str]) -> list:
    """Принимает на вход путь до xlsx-файла и возвращает список словарей с данными о финансовых транзакциях"""

    transactions_list = pd.read_excel(patch_to_xlsx)
    xlsx_transactions_list = transactions_list.to_dict(orient='records')

    return xlsx_transactions_list

#xlsx_file(user_patch_to_xlsx)
#print(xlsx_file(user_patch_to_xlsx))