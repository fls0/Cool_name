from AdressBook.AB import main as ab_main
from NoteBook.NB import main as nb_main
from Map.Map import main as map_main
from sort.sort import main as sort_main
import os


if __name__ == '__main__':
    print('MENU')
    while True:
        choice = input(
            'Вітаю, я ваш персональний помічник.\nОберіть функцію:\n1.Записна книжка\n2.Нотатник\n3.Карта\n4.Сортування папки\n5.Гра\n0.Вихід\n')
        if choice == '1':
            ab_main()
        elif choice == '2':
            nb_main()
        elif choice == '3':
            map_main()
        elif choice == '4':
            sort_main()
        elif choice == '5':
            os.system('Personal_assistant/Game/game.py')
        elif choice == '0':
            break
