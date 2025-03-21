from unittest.mock import Mock, patch

import pandas as pd

from src.utils_csv_and_xlsx import csv_file, xlsx_file


@patch("csv.DictReader")
def test_csv_file(mock_csv: Mock) -> None:
    csv_data = [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": "16210",
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        }
    ]
    data = [
        {
            "id": 650703,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "operationAmount": {"amount": "16210", "currency": {"name": "Sol", "code": "PEN"}},
            "description": "Перевод организации",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
        }
    ]
    mock_csv.return_value = csv_data
    assert csv_file("..\\data\\transactions.csv") == data


def test_not_exist_csv() -> None:
    assert csv_file("..\\data\\transactions_not_found.csv") == []


@patch("csv.DictReader")
def test_invalid_csv(mock_csv: Mock) -> None:
    mock_csv.return_value = [{"ids": 111}]
    assert csv_file("..\\data\\transactions_not_found.csv") == []


@patch("pandas.read_excel")
def test_read_excel(mock_excel: Mock) -> None:
    excel_data = pd.DataFrame(
        {
            "id": [111],
            "state": ["EXECUTED"],
            "date": ["2024-12-15"],
            "amount": [111.0],
            "currency_name": ["Ruble"],
            "currency_code": ["RUB"],
            "description": ["test"],
            "from": ["Master Card"],
            "to": ["Visa"],
        }
    )
    data = [
        {
            "id": 111,
            "state": "EXECUTED",
            "date": "2024-12-15",
            "operationAmount": {"amount": "111.0", "currency": {"name": "Ruble", "code": "RUB"}},
            "description": "test",
            "from": "Master Card",
            "to": "Visa",
        }
    ]
    mock_excel.return_value = excel_data
    assert xlsx_file("data/transactions_excel.xlsx") == data


def test_not_exist_excel() -> None:
    assert xlsx_file("data/notexist.xlsx") == []


@patch("pandas.read_excel")
def test_invalid_excel(mock_csv: Mock) -> None:
    mock_csv.return_value = pd.DataFrame({"ids": [111.0]})
    assert xlsx_file("data/transactions_excel.xlsx") == []
