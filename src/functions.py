import json


def load_operations():
    """
    Функция выгружает последние пять транзакций.
    """

    with open('operations.json', 'r', encoding='utf-8') as operation_file:
        return json.load(operation_file)[:5]


print(load_operations())