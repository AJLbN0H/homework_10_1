import time


def log(filename: str = None):
    """Декоратор, который автоматически логирует начало и конец выполнения функции, а также ее результаты или возникшие
    ошибки. Декоратор должен принимать необязательный аргумент filename, который определяет, куда будут записываться
    логи (в файл или в консоль):
    Если filename задан, логи записываются в указанный файл.
    Если filename не задан, логи выводятся в консоль."""

    def decorator(func):
        def wrappers(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            error_dict = [
                "Вы не ввели номер карты",
                "Номер карты должен содержать 16 цифр",
                "Вы не ввели номер счета",
                "Номер счета должен содержать 20 цифр",
                "Введите тип и номер карты или номер счета",
                "Номер счета должен содержать 20 цифр",
                "Номер карты должен содержать 16 цифр",
                "Вы не ввели данные по транзакциям",
                "Транзакции отсутствуют",
                "Вы не ввели данные по транзакциям",
                "Вы не ввели дату",
            ]
            end_time = time.time()
            if result in error_dict:
                error_message = (
                    f"В функции '{func.__name__[7::]}' возникла ошибка '{result}', " f"входные данные: '{args[0]}'"
                )
                if filename is not None:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(error_message + "\n")
                else:
                    print(error_message)
            else:
                log_message = (
                    f"Функция '{func.__name__[7::]}' выполнена за {end_time - start_time:.4f} секунд. "
                    f"Результат: {result}\n"
                )
                if filename is not None:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(log_message)
                else:
                    print(log_message)

            return result

        return wrappers

    return decorator
