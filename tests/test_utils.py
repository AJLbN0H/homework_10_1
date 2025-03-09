from src.utils import json_file, transaction_amount
from unittest.mock import Mock, patch
import pytest
from typing import Iterable


@patch("builtins.open")
def test_json_file(path_to_json: Mock) -> None:
    json_data = '[{"id": 441945886, "amount": "31957.58"}]'
    data = [{"id": 441945886, "amount": "31957.58"}]
    mock_json = path_to_json.return_value.__enter__.return_value
    mock_json.read.return_value = json_data
    assert json_file("data/operations.json") == data
    path_to_json.assert_called_once_with("data/operations.json", "r", encoding="utf-8")


@patch("builtins.open")
def test_empty_json_file(path_to_json: Mock) -> None:
    json_data = ""
    mock_json = path_to_json.return_value.__enter__.return_value
    mock_json.read.return_value = json_data
    assert json_file("data/operations.json") == []


@patch("builtins.open")
def test_not_a_list_json_file(path_to_json: Mock) -> None:
    json_data = '[{"id": 441945886, "amount": "31957.58"]'
    mock_json = path_to_json.return_value.__enter__.return_value
    mock_json.read.return_value = json_data
    assert json_file("data/operations.json") == []


def test_load_not_exist_operations_json() -> None:
    assert json_file("data/operations_not_found.json") == []


@pytest.mark.parametrize("transaction, amount", [
    (
            [{
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
                "operationAmount": {
                    "amount": "8221.37",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод организации",
                "from": "MasterCard 7158300734726758",
                "to": "Счет 35383033474447895560"
            }],
            732120.340183
    ),
    (
            [{
                "id": 441945887,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {
                    "amount": "31957.58",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                },
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589"
            }],
            31957.58
    )
])
def test_transaction_amount(transaction: Iterable[list], amount: float) -> None:
    with patch("requests.get") as mock_convert:
        mock_convert.return_value.json.return_value = {"result": 732120.340183}
        assert transaction_amount(transaction) == amount
