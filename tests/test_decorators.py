import os
import tempfile

from src.decorators import log
from src.masks import get_mask_card_number


def test_logging_to_console_get_mask_card_number(capsys):
    @log()
    def logged_get_mask_card_number(card_number: str) -> str:
        return get_mask_card_number(card_number)

    user_input = "7000792289606361"
    logged_get_mask_card_number(user_input)
    captured = capsys.readouterr()
    assert (
        "Функция 'get_mask_card_number' выполнена за 0.0003 секунд. " "Результат: 7000 79** **** 6361" in captured.out
    )

    @log()
    def logged_get_mask_card_number(card_number: str) -> str:
        return get_mask_card_number(card_number)

    user_input = "700079228960636"
    logged_get_mask_card_number(user_input)
    captured = capsys.readouterr()
    assert (
        "В функции 'get_mask_card_number' возникла ошибка 'Номер карты должен содержать 16 цифр', "
        "входные данные: '700079228960636'" in captured.out
    )

    @log()
    def logged_get_mask_card_number(card_number: str) -> str:
        return get_mask_card_number(card_number)

    user_input = "7000___-234**79228960636"
    logged_get_mask_card_number(user_input)
    captured = capsys.readouterr()
    assert (
        "В функции 'get_mask_card_number' возникла ошибка 'Номер карты должен содержать 16 цифр', "
        "входные данные: '7000___-234**79228960636'" in captured.out
    )

    @log()
    def logged_get_mask_card_number(card_number: str) -> str:
        return get_mask_card_number(card_number)

    user_input = ""
    logged_get_mask_card_number(user_input)
    captured = capsys.readouterr()
    assert (
        "В функции 'get_mask_card_number' возникла ошибка 'Вы не ввели номер карты', входные данные: ''"
        in captured.out
    )

    @log()
    def logged_get_mask_card_number(card_number: str) -> str:
        return get_mask_card_number(card_number)

    user_input = None
    logged_get_mask_card_number(user_input)
    captured = capsys.readouterr()
    assert (
        "В функции 'get_mask_card_number' возникла ошибка 'Вы не ввели номер карты', входные данные: 'None'"
        in captured.out
    )


def test_logging_to_file_get_mask_card_number():
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_filename = temp_file.name

    try:

        @log(filename=temp_filename)
        def logged_get_mask_card_number(card_number: str) -> str:
            return get_mask_card_number(card_number)

        logged_get_mask_card_number("7000792289606361")
        with open(temp_filename, "r", encoding="utf-8") as f:
            log_content = f.read()
        assert (
            "Функция 'get_mask_card_number' выполнена за 0.0003 секунд. Результат: 7000 79** **** 6361" in log_content
        )
    finally:
        os.remove(temp_filename)

    try:

        @log(filename=temp_filename)
        def logged_get_mask_card_number(card_number: str) -> str:
            return get_mask_card_number(card_number)

        logged_get_mask_card_number("700079228960636")
        with open(temp_filename, "r", encoding="utf-8") as f:
            log_content = f.read()
        assert (
            "В функции 'get_mask_card_number' возникла ошибка 'Номер карты должен содержать 16 цифр', "
            "входные данные: '700079228960636'" in log_content
        )
    finally:
        os.remove(temp_filename)

    try:

        @log(filename=temp_filename)
        def logged_get_mask_card_number(card_number: str) -> str:
            return get_mask_card_number(card_number)

        logged_get_mask_card_number("7000___-234**79228960636")
        with open(temp_filename, "r", encoding="utf-8") as f:
            log_content = f.read()
        assert (
            "В функции 'get_mask_card_number' возникла ошибка 'Номер карты должен содержать 16 цифр', "
            "входные данные: '7000___-234**79228960636'" in log_content
        )
    finally:
        os.remove(temp_filename)

    try:

        @log(filename=temp_filename)
        def logged_get_mask_card_number(card_number: str) -> str:
            return get_mask_card_number(card_number)

        logged_get_mask_card_number("")
        with open(temp_filename, "r", encoding="utf-8") as f:
            log_content = f.read()
        assert (
            "В функции 'get_mask_card_number' возникла ошибка 'Вы не ввели номер карты', входные данные: ''"
            in log_content
        )
    finally:
        os.remove(temp_filename)

    try:

        @log(filename=temp_filename)
        def logged_get_mask_card_number(card_number: str) -> str:
            return get_mask_card_number(card_number)

        logged_get_mask_card_number(None)
        with open(temp_filename, "r", encoding="utf-8") as f:
            log_content = f.read()
        assert (
            "В функции 'get_mask_card_number' возникла ошибка 'Вы не ввели номер карты', входные данные: 'None'"
            in log_content
        )
    finally:
        os.remove(temp_filename)
