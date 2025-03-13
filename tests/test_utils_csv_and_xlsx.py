from unittest.mock import Mock, patch
from src.utils_csv_and_xlsx import csv_file


@patch("csv.DictReader")
def test_utils_csv_file(mock_csv: Mock) -> None:
    csv_data = [
            {'id': '650703', 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': '16210', 'currency_name': 'Sol',
            'currency_code': 'PEN', 'from': 'Счет 58803664561298323391', 'to': 'Счет 39745660563456619397',
            'description': 'Перевод организации'}]
    data = [
        {'id': '650703', 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': '16210', 'currency_name': 'Sol',
         'currency_code': 'PEN', 'from': 'Счет 58803664561298323391', 'to': 'Счет 39745660563456619397',
         'description': 'Перевод организации'}]
    mock_csv.return_value = csv_data
    assert csv_file("data/transaction.csv") == data

#def test_utils_csv_file(patch_to_csv: Mock) -> None:
    #csv_data = {'id;state;date;amount;currency_name;currency_code;from;to;description': '650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;Счет 58803664561298323391;Счет 39745660563456619397;Перевод организации'}
    #data = [{'id': '650703', 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': '16210', 'currency_name': 'Sol', 'currency_code': 'PEN', 'from': 'Счет 58803664561298323391', 'to': 'Счет 39745660563456619397', 'description': 'Перевод организации'}]
    #mock_csv = patch_to_csv.return_value.__enter__.return_value
    #mock_csv.read.return_value = csv_data
    #assert csv_file('data/transaction.csv') == data
    #patch_to_csv.assert_called_once_with("data/transaction.csv", "r", encoding="utf-8")

#{'id;state;date;amount;currency_name;currency_code;from;to;description': '650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;Счет 58803664561298323391;Счет 39745660563456619397;Перевод организации'}