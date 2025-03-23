from unittest.mock import Mock, patch

from src.external_api import convert_usd_and_eur_in_rub


def test_convert_amount() -> None:
    mock_response = Mock()
    mock_response.json.return_value = {"result": 732120.340183}

    with patch("requests.get", return_value=mock_response):
        list_transaction = {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        }
        result = convert_usd_and_eur_in_rub(list_transaction)
        assert result["result"] == 690603.391805
