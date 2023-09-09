import datetime
import pickle

class Note:
    def __init__(self, name: str, text: str="", tags: list=[]):
        self.name = name
        self.text = text
        self.tags = tags
        self.created_date = datetime.datetime.now().replace(microsecond=0)

    def edit(self):
        print("Введіть текст нотатки. Для завершення введення натисніть Ctrl-Z - Enter.")
        new_text = []
        while True:
            try:
                line = input()
                new_text.append(line)
            except EOFError:
                break
        self.text = "\n".join(new_text)
      
    def remove_tag(self, tag: str):
        self.tags.remove(tag)

class Notebook:
    def __init__(self):
        self.notes = {}

    def add_note(self, note: Note):
        # Перевіряємо, чи ім'я вже існує
        original_name = note.name
        i = 1
        while note.name in self.notes:
            note.name = f"{original_name}_{i}"  # Додаємо суфікс, якщо ім'я вже існує
            i += 1
        self.notes[note.name] = note

    def search_notes(self, query: str):
        matching_notes = []
        for note in self.notes.values():
            # Перевіряємо, чи збігається рядок пошуку з ім'ям, текстом або тегами нотатки
            if query.lower() in note.name.lower() or query.lower() in note.text.lower() \
                or any(tag.lower() == query.lower() for tag in note.tags):
                matching_notes.append(note)
        if not matching_notes:
            print("Нічого не знайдено...")
        return matching_notes

    def sort_notes(self, by_name=False, by_tags=False, by_created_date=False):
        if by_name:
            sorted_notes = sorted(self.notes.values(), key=lambda note: note.name)
        elif by_tags:
            sorted_notes = sorted(self.notes.values(), key=lambda note: note.tags)
        elif by_created_date:
            sorted_notes = sorted(self.notes.values(), key=lambda note: note.created_date)
        else:
            return None
        return sorted_notes
    
    def available_notes(self):
        for idx, note in enumerate(notebook.notes.values()):
                print(f"{idx + 1}. {note.name}")
    
    def save_to_file(self, filename):      # Запис у файл за протоколом pickle
        with open(filename, 'wb') as file:
            pickle.dump(self.notes, file)

    def load_from_file(self, filename):    # Завантаження з файлу за протоколом pickle
        try:
            with open(filename, 'rb') as file:
                self.notes = pickle.load(file)
        except FileNotFoundError:
            self.notes = {}
        except Exception as error:
            print(f"Виникла помилка: {error}")

def format_note(note: Note):
    return f"\nІм'я: {note.name}\nДата створення: {note.created_date}\nТекст:\n{note.text}\nТеги: {', '.join(note.tags)}"

# Головний код
if __name__ == "__main__":
    
    notebook = Notebook()
    notebook.load_from_file('notebook.pkl')
    start = True
    
    while True:
        if not start:
            input("\nНатисніть Enter для повернення в головне меню...")
        start = False
        print("\nНотатки")
        print("1. Додати нотатку")
        print("2. Редагувати нотатку")
        print("3. Видалити нотатку")
        print("4. Пошук нотаток")
        print("5. Сортування нотаток")
        print("6. Вихід")

        choice = input("\nВиберіть опцію: ")
        print("\n")

        if choice == "1":
            name = input("Введіть ім'я нотатки (або натисніть Enter, щоб згенерувати): ")
            if not name:
                name = f"Note_{datetime.datetime.now().replace(microsecond=0).timestamp()}"
            name = name.lower()  # Приводимо ім'я до нижнього регістру
            note = Note(name)
            note.edit()  # Виклик методу edit для створення тексту нотатки                       
            tags = input("Введіть теги (розділені пробілами): ").split()
            note.tags = [tag.strip() for tag in tags]
            notebook.add_note(note)
            print("Нотатка успішно додана.")
        elif choice == "2":
            # Редагування нотатки
            print("Список доступних нотаток:")
            notebook.available_notes()
            edit_choice = input("Виберіть номер нотатки для редагування: ")
            try:
                edit_choice = int(edit_choice)
                if 1 <= edit_choice <= len(notebook.notes):
                    selected_note = list(notebook.notes.values())[edit_choice - 1]
                    selected_note.edit()  # Виклик методу edit для редагування тексту нотатки                    
                    tags = input("Змініть теги (розділені пробілами) (Enter - без змін): ").split() # редагування тегів
                    if tags:
                        selected_note.tags = [tag.strip() for tag in tags]         
                    print("Нотатка успішно відредагована.")
                else:
                    print("Неправильний номер нотатки.")
            except ValueError:
                print("Неправильний номер нотатки.")
            
        elif choice == "3":
            # Видалення нотатки
            print("Список доступних нотаток:")
            notebook.available_notes()
            delete_choice = input("Виберіть номер нотатки для видалення: ")
            try:
                delete_choice = int(delete_choice)
                notes_list = list(notebook.notes.values())  # Створюємо список нотаток зі словника
                if 1 <= delete_choice <= len(notebook.notes):
                    deleted_note = notes_list.pop(delete_choice - 1)  # Видаляємо нотатку зі списку
                    del notebook.notes[deleted_note.name]  # Видаляємо нотатку зі словника за її іменем                                     
                    print("Нотатка успішно видалена.")
                else:
                    print("Неправильний номер нотатки.")
            except ValueError:
                print("Неправильний номер нотатки.")

        elif choice == "4":
            query = input("Введіть рядок для пошуку: ")
            matching_notes = notebook.search_notes(query)
            for note in matching_notes:
                print(format_note(note))
        elif choice == "5":
            # Вкладене меню для сортування
            print("Меню сортування:")
            print("1. За іменем")
            print("2. За тегами")
            print("3. За часом створення")
            sort_choice = input("Виберіть метод сортування: ")
            
            if sort_choice == "1":
                sorted_notes = notebook.sort_notes(by_name=True)
            elif sort_choice == "2":
                sorted_notes = notebook.sort_notes(by_tags=True)
            elif sort_choice == "3":
                sorted_notes = notebook.sort_notes(by_created_date=True)
            else:
                print("Невірний вибір сортування")
                continue

            if sorted_notes:
                for note in sorted_notes:
                    print(format_note(note))
            else:
                print("Невідомий метод сортування")
        
        elif choice == "6":
            notebook.save_to_file('notebook.pkl')
            break
