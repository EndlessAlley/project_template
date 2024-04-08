def print_text_to_console(text):
    """
    Функція для виводу тексту у консоль.

    Args:
        text (str): Текст для виведення.
    """
    print(text)


def write_text_to_file(text, file_path):
    """
    Функція для запису тексту до файлу за допомогою вбудованих можливостей Python.

    Args:
        text (str): Текст для запису.
        file_path (str): Шлях до файлу.
    """
    with open(file_path, 'w') as file:
        file.write(text)
