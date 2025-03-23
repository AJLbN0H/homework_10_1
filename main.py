import pandas as pd

from src.processing import filter_by_state, sort_by_date
from src.search_by_transactions import search_by_list_description
from src.utils import json_file
from src.utils_csv_and_xlsx import csv_file, xlsx_file
from src.widget import get_date, mask_account_card

user_json_file = json_file("data\\operations.json")
user_csv_file = csv_file("data\\transactions.csv")
user_xlsx_file = xlsx_file("data\\transactions_excel.xlsx")


def main():

    print(
        """\nПрограмма: Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла"""
    )
    user_patch_to_file = input("\nПользователь: ")
    user_list_transactions = "Список транзакций пользователя"

    while True:
        if user_patch_to_file == "1":
            print("\nПрограмма: Для обработки выбран JSON-файл.")
            user_list_transactions = user_json_file
            break

        elif user_patch_to_file == "2":
            print("\nПрограмма: Для обработки выбран CSV-файл.")
            user_list_transactions = user_csv_file
            break

        elif user_patch_to_file == "3":
            print("\nПрограмма: Для обработки выбран XLSX-файл.")
            user_list_transactions = user_xlsx_file
            break

        else:
            print("\nОшибка! Некорректные данные!\n" "Введите цифру необходимого пункта меню (1, 2 или 3)")
            user_patch_to_file = input("\nПользователь: ")

    list_transactions_filtered_by_state = []

    if user_patch_to_file == "1":
        print(
            """\nПрограмма: Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED"""
        )

        user_state = input("\nПользователь: ")

        while True:
            if user_state.upper() == "EXECUTED":
                [
                    list_transactions_filtered_by_state.append(transact)
                    for transact in user_list_transactions
                    if filter_by_state([transact], "EXECUTED") != "Транзакции отсутствуют"
                ]
                print('\nПрограмма: Операции отфильтрованы по статусу "EXECUTED"')
                break

            elif user_state.upper() == "CANCELED":
                [
                    list_transactions_filtered_by_state.append(transact)
                    for transact in user_list_transactions
                    if filter_by_state([transact], "CANCELED") != "Транзакции отсутствуют"
                ]
                print('\nПрограмма: Операции отфильтрованы по статусу "CANCELED"')
                break

            else:
                print(
                    f'\nОшибка! Статус операции "{user_state}" недоступен!\n'
                    "Введите один из статусов по которому необходимо выполнить фильтрацию (EXECUTED или CANCELED)"
                )
                user_state = input("\nПользователь: ")

    else:
        print(
            """\nПрограмма: Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"""
        )

        user_state = input("\nПользователь: ")

        while True:
            if user_state.upper() == "EXECUTED":
                [
                    list_transactions_filtered_by_state.append(transact)
                    for transact in user_list_transactions
                    if filter_by_state([transact], "EXECUTED") != "Транзакции отсутствуют"
                ]
                print('\nПрограмма: Операции отфильтрованы по статусу "EXECUTED"')
                break

            elif user_state.upper() == "CANCELED":
                [
                    list_transactions_filtered_by_state.append(transact)
                    for transact in user_list_transactions
                    if filter_by_state([transact], "CANCELED") != "Транзакции отсутствуют"
                ]
                print('\nПрограмма: Операции отфильтрованы по статусу "CANCELED"')
                break

            elif user_state.upper() == "PENDING":
                [
                    list_transactions_filtered_by_state.append(transact)
                    for transact in user_list_transactions
                    if filter_by_state([transact], "PENDING") != "Транзакции отсутствуют"
                ]
                print('\nПрограмма: Операции отфильтрованы по статусу "PENDING"')
                break

            else:
                print(
                    f'\nОшибка! Статус операции "{user_state}" недоступен!\n'
                    "Введите один из статусов по которому необходимо выполнить фильтрацию (EXECUTED или CANCELED)"
                )
                user_state = input("\nПользователь: ")

    print("\nПрограмма: Отсортировать операции по дате? Да/Нет")

    user_sort_by_date = input("\nПользователь: ")
    list_transactions_filtered_by_date = []

    while True:
        if user_sort_by_date.lower() == "да":
            print("\nПрограмма: Отсортировать по возрастанию или по убыванию?")

            user_reverse = input("\nПользователь: ")

            while True:
                if user_reverse.lower() == "по возрастанию":
                    list_transactions_filtered_by_date = sort_by_date(
                        list_transactions_filtered_by_state, reverse=False
                    )
                    break

                elif user_reverse.lower() == "по убыванию":
                    list_transactions_filtered_by_date = sort_by_date(list_transactions_filtered_by_state)
                    break

                else:
                    print("\nОшибка! Некорректные данные!\n" 'Введите "по возрастанию" или "по убыванию"')
                    user_reverse = input("\nПользователь: ")
            break

        elif user_sort_by_date.lower() == "нет":
            list_transactions_filtered_by_date = list_transactions_filtered_by_state
            break

        else:
            print("\nОшибка! Некорректные данные!\n" 'Введите "Да" или "Нет"')
            user_sort_by_date = input("\nПользователь: ")

    print("\nПрограмма: Выводить только рублевые тразакции? Да/Нет")

    user_filtered_transactions_in_rub = input("\nПользователь: ")
    list_transactions_in_rub = []

    while True:
        if user_filtered_transactions_in_rub.lower() == "да":
            [
                list_transactions_in_rub.append(i)
                for i in list_transactions_filtered_by_date
                if i["operationAmount"]["currency"]["code"] == "RUB"
            ]
            break

        elif user_filtered_transactions_in_rub.lower() == "нет":
            list_transactions_in_rub = list_transactions_filtered_by_date
            break

        else:
            print("\nОшибка! Некорректные данные!\n" 'Введите "Да" или "Нет"')
            user_filtered_transactions_in_rub = input("\nПользователь: ")

    print("\nПрограмма: Отфильтровать список транзакций по определенному слову в описании? Да/Нет")

    user_answer_filter_by_word = input("\nПользователь: ")
    list_transactions_filtered_by_word = []

    while True:
        if user_answer_filter_by_word.lower() == "да":
            print("\nПрограмма: Введите слово")
            user_filter_word = input("Пользователь: ")
            list_transactions_filtered_by_word = search_by_list_description(list_transactions_in_rub, user_filter_word)
            break

        elif user_answer_filter_by_word.lower() == "нет":
            list_transactions_filtered_by_word = list_transactions_in_rub
            break

        else:
            print("\nОшибка! Некорректные данные!\n" 'Введите "Да" или "Нет"')
            user_answer_filter_by_word = input("\nПользователь: ")

    print("\nПрограмма: Распечатываю итоговый список транзакций...")

    if not list_transactions_filtered_by_word:
        print("\nПрограмма: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")

    else:
        print(
            f"""\nПрограмма:
Всего банковских операций в выборке: {len(list_transactions_filtered_by_word)}"""
        )
        for transact in list_transactions_filtered_by_word:
            if not pd.isna(transact.get("from")):
                print(
                    f"""\n{get_date(transact['date'])} {transact['description']}
{mask_account_card(transact['from'])} -> {mask_account_card(transact['to'])}
Сумма: {transact['operationAmount']['amount']} {transact['operationAmount']['currency']['name']}"""
                )
            else:
                print(
                    f"""\n{get_date(transact['date'])} {transact['description']}
Неизвестно -> {mask_account_card(transact['to'])}
Сумма: {transact['operationAmount']['amount']} {transact['operationAmount']['currency']['name']}"""
                )


if __name__ == "__main__":
    main()
