from unittest.mock import Mock, patch

from src.external_api import convert_usd_and_eur_in_rub


def test_convert_amount() -> None:
    """testing convert currency with external API."""

    mock_response = Mock()
    mock_response.json.return_value = {"result": 8905.0893}

    with patch("requests.get", return_value=mock_response):
        result = convert_usd_and_eur_in_rub(100, "USD")
        assert result["result"] == 8905.0893
