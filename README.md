# Виджет банковских операций

# Описание:

Мой проект это это серверная часть виджета банковских операций. Виджет имеет возможность отображать операции клиента, маскировать номер карты или счета, сортировать операции по времени.

## Установка:

Клонируйте репозиторий:
```
git clone https://github.com/AJLbN0H/homework_10_1.git
```

## Примеры работы функций:

* ```get_mask_account``` - маскировки номера карты (XXXX XX** **** XXXX);


* ```get_mask_card_number``` - маскировка номера счета (**XXXX);


* ```mask_account_card``` - совмещает в себе эти две фнукции (Тип карты XXXX XX** **** XXXX или Счет **XXXX);


* ```get_date``` - возврощает строку с датой операции;


* ```filter_by_state``` - возвращает новый список словарей, содержащий только те словари, у которых ключ state соответствует указанному значению;


* ```sort_by_date``` - возвращает список отсортированный по дате;


* ```filter_by_currency``` - возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной;


* ```transaction_descriptions``` - возвращает описание каждой операции по очереди;


* ```card_number_generator``` - генерирует номер карты в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999;


* ```log``` - функция-декоратор, автоматически регистрирует детали выполнения функций, такие как время вызова, имя функции, передаваемые аргументы, результат выполнения и информация об ошибках;

## Использование:

1. Откройте репозиторий


2. Перейдите в пакет ```src``` ознакомтесь с примерами работы функций и выберете подходящую для вас.


3. Откройте файл с нужной вам функцией


4. Вставте свои данные


5. Введите свои данные и получите результат

## Были проведены тесты функций:

### Модуль masks
* ```get_mask_card_number```:
  * Тестирование правильности маскирования номера карты.
  * Проверка работы функции на различных входных форматах номеров карт, включая граничные случаи и нестандартные длины номеров.
  * Проверка, что функция корректно обрабатывает входные строки, где отсутствует номер карты.
* ```get_mask_account```:
  * Тестирование правильности маскирования номера счета.
  * Проверка работы функции с различными форматами и длинами номеров счетов.
  * Проверка, что функция корректно обрабатывает входные данные, где номер счета меньше ожидаемой длины.

### Модуль widget
* ```mask_account_card```:
  * Тесты для проверки, что функция корректно распознает и применяет нужный тип маскировки в зависимости от типа входных данных (карта или счет).
  * Параметризованные тесты с разными типами карт и счетов для проверки универсальности функции.
  * Тестирование функции на обработку некорректных входных данных и проверка ее устойчивости к ошибкам.
* ```get_date```:
  * Тестирование правильности преобразования даты.
  * Проверка работы функции на различных входных форматах даты, включая граничные случаи и нестандартные строки с датами.
  * Проверка, что функция корректно обрабатывает входные строки, где отсутствует дата.

### Модуль processing
* ```filter_by_state```:
  * Тестирование фильтрации списка словарей по заданному статусу ```state```.
  * Проверка работы функции при отсутствии словарей с указанным статусом ```state``` в списке.
  * Параметризация тестов для различных возможных значений статуса ```state```.
* ```sort_by_date```:
  * Тестирование сортировки списка словарей по датам в порядке убывания и возрастания.
  * Проверка корректности сортировки при одинаковых датах.
  * Тесты на работу функции с некорректными или нестандартными форматами дат.

### Модуль generators
* ```transaction_descriptions```:
  * Напишите тесты, проверяющие, что функция корректно фильтрует транзакции по заданной валюте.
  * Проверьте, что функция правильно обрабатывает случаи, когда транзакции в заданной валюте отсутствуют.
  * Убедитесь, что генератор не завершается ошибкой при обработке пустого списка или списка без соответствующих валютных операций.
* ```transaction_descriptions```:
  * Проверьте, что функция возвращает корректные описания для каждой транзакции.
  * Тестируйте работу функции с различным количеством входных транзакций, включая пустой список.
* ```card_number_generator```:
  * Напишите тесты, которые проверяют, что генератор выдает правильные номера карт в заданном диапазоне.
  * Проверьте корректность форматирования номеров карт.
  * Убедитесь, что генератор корректно обрабатывает крайние значения диапазона и правильно завершает генерацию.
  
### С тестами можно ознакомиться в пакете ```tests```, а с покрытием тестами в директории ```htmlcov``` -> ```index.html```
