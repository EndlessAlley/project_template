def input_text_from_console():
    """
    Функція для введення тексту з консолі.

    Returns:
        str: Введений текст.
    """
    text = input("Введіть текст: ")
    return text


def read_text_from_file(file_path):
    """
    Функція для зчитування тексту з файлу за допомогою вбудованих можливостей Python.

    Args:
        file_path (str): Шлях до файлу.

    Returns:
        str: Зміст файлу.
    """
    with open(file_path, 'r') as file:
        text = file.read()
    return text


def read_text_from_file_with_pandas(file_path):
    """
    Функція для зчитування тексту з файлу за допомогою бібліотеки pandas.

    Args:
        file_path (str): Шлях до файлу.

    Returns:
        str: Зміст файлу.
    """
    import pandas as pd
    data = pd.read_csv(file_path)
    text = data.to_string(index=False, header=False)
    return text
