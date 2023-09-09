import time
def print_logo():
    # Відкрийте файл для читання
    file_path = "LOGO.txt"
    try:
        with open(file_path, "r") as file:
            # Читаємо ітеративно кожен символ з файлу
            while True:
                char = file.read(1)  # Читаємо один символ
                if not char:  # Якщо кінець файлу, виходимо з циклу
                    break
                time.sleep(0.0003)
                print(char, end="")  # Виводимо символ без переносу на новий рядок
    except FileNotFoundError:
        print(f"Файл '{file_path}' не знайдено.")
    except Exception as e:
        print(f"Сталася помилка: {str(e)}")
