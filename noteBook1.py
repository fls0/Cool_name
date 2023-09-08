import json                     #буде потрібно для запису/читання з файлу на диску
import os                       #для выдкриття файлу
from datetime import datetime   #для визначення коли буде створена нотатка

class Note:
    """Клас Note. 
        Основна сутність нашого NoteBook 
        Вирішив що буде мати такі поля (подивився як в телефоні):
     - title - заголовок
     - content - текст замітки
     - tags - теги замітки відповідно до тз
     - created_at - дата створення
     """
    def __init__(self, title, content, tags=None, created_at=None):
        self.title = title
        self.content = content
        self.tags = tags or []
        self.created_at = datetime.now().strftime('%Y-%m-%d %H:%M')

class Manager:
    """Клас Manager.
    Тут написані методи що використовуються для виконня завдання:    
    - def upload_notes - завантажує нотатки з диску. (Виконується при запуску)
    - def save_notes - зберігає нотатки на диск. (виконується 1- коли створюємо, 2- коли редактуємо, 3- коли видаляємо)
    - def add_notes - додає нотатки.
    - def edit_note - редактує нотатки
    - def delete_note - видаляє нотатки
    - def search_notes_by_tag - шукає нотатки по тегу(ам)
    - def search_notes_by_content - шукає нотатки по тексту нотатки.
    """
    def __init__(self, storage_path):

        self.storage_path = storage_path    # шлях куди зберігати і звідки зчитувати
        self.notes = []                     # тут будуть лежати всі нотатки з якими ми будем працювати