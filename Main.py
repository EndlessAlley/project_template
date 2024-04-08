import app
from app.io import output
from app.io import input


def main():
    text_from_console = input.input_text_from_console()
    file_text = input.read_text_from_file('file.txt')
    pandas_file_text = input.read_text_from_file_with_pandas('file.csv')

    print("Текст, введений з консолі:")
    output.print_text_to_console(text_from_console)
    print("\nТекст, зчитаний з файлу (за допомогою вбудованих можливостей Python):")
    output.print_text_to_console(file_text)
    print("\nТекст, зчитаний з файлу (за допомогою бібліотеки pandas):")
    output.print_text_to_console(pandas_file_text)

    output.write_text_to_file(text_from_console, 'output.txt')
    output.write_text_to_file(file_text, 'output.txt')
    output.write_text_to_file(pandas_file_text, 'output.txt')


if __name__ == "__main__":
    main()
