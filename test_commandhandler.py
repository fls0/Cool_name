from collections import UserDict
from datetime import datetime
import pickle
import re
from dateparser import parse


class Field:
    def __init__(self, some_value):
        self._value = None
        self.value = some_value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def __str__(self):
        return f'{self.value}'


class Name(Field):
    pass


class Phone(Field):
    @Field.value.setter
    def phone_number(self, value):  # для перевірки в візьмемо український номер
        flag = True
        for i in value:
            if i.isdigit() or i in '+':
                continue
            else:
                flag = False
                return f'Wrong number'
        if flag:
            if value.startswith('+38') and len(value) == 13:
                self._value = value
            elif len(value) == 10:
                self._value = value
        else:
            return f'Wrong number'


class Birthday(Field):
    def valid_date(self, value: str):
        try:
            obj_datetime = parse(value)
            return obj_datetime.date()
        except Exception:
            raise 'Wrong data type. Try "dd-mm-yy"'

    @Field.value.setter
    def value(self, value):
        self._value = self.valid_date(value)


class Email(Field):
    @Field.value.setter
    def validate_email(self, value: str):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if re.fullmatch(regex, value):
            self._value = value
        else:
            return f'Wrong email'
        
class Adress(Field):
    pass


class Record:
    def __init__(self, name: Name, phone: Phone, birthday: Birthday, email: Email, adress=None):
        self.name = name
        self.phones = []
        if phone:
            self.phones.append(phone)
            self.phone = phone
        self.birthday = birthday
        self.email = email
        if adress:
            self.adress = adress

    def add_phone(self, phone):
        phone_number = Phone(phone)
        if phone_number not in self.phones:
            self.phones.append(phone_number)

    def remove_phone(self, phone):
        phone_obj = Phone(phone)
        if phone_obj in self.phones:
            self.phones.remove(phone_obj)

    def edit_phone(self, old_phone, new_phone):
        self.remove_phone(old_phone)
        self.add_phone(new_phone)

    def days_to_birthday(self):
        pass


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find_record(self, value):
        return self.data.get(value)

    def __init__(self):
        super().__init__()

    def dump(self):
        with open('AdressBook.bin', 'wb') as file:
            pickle.dump(self.data, file)

    def load(self):
        with open('AdressBook.bin', 'rb') as file:
            self.store = pickle.load(file)





def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "ValueError. Please enter the name and phone number."
        except IndexError:
            return "IndexError. Give me name and phone please."
        except NameError:
            return "Invalid input. Name should contain only letters."
        except TypeError:
            return "Invalid input. Phone number should contain only digits."
    return wrapper


class CommandHandler:
    def __init__(self, command: str):
        self.command = command

    def command_handler(self, input_str):
        if input_str == "hello":
            print("How can I help you?")
        elif input_str.startswith("add "):
            print(CommandHandler.command_add(input_str))
        elif input_str.startswith("change "):
            print(CommandHandler.command_change(input_str))
        elif input_str.startswith("phone "):
            print(CommandHandler.command_phone(input_str))
        elif input_str == "show all":
                (CommandHandler.command_show_all(contact_list))
        elif input_str in ["good bye", "close", "exit"]:
            print("Good bye!")
        else:
            print("Невірно введена команда. Доступні команди:'hello','add','change','phone','show all','good bye','close','exit'")
            

    @input_error
    def command_add(input_str):
        _, name, phone, birthday, email, adress = input_str.split()
        name = Name(name)
        phone = Phone(phone)
        birthday = Birthday(birthday)
        email = Email(email)
        adress = Adress(adress)
        contacts = Record(name, phone, birthday, email, adress)
        contact_list.add_record(contacts)
        return f"Contact {name} has been added."

    @input_error
    def command_delete(input_str):
        pass


    @input_error
    def command_change(input_str):
        _, name, phone, birthday, email, adress = input_str.split()
        name = name.title()
        contact_list[name] = Phone(phone), Birthday(birthday), Email(email), Adress(adress)
        return f"Contact {name} has been updated."


    @input_error
    def command_phone(input_str):
        list_comand = input_str.split()
        name = list_comand[1].title()
        if not name.isalpha():
            raise NameError
        return contact_list[name]


    def command_show_all(contact_list):
        if not contact_list:
            return "Список контактів пустий."
        result = "Contacts:\n"
        for name, value in contact_list.items():
            result += f"{name}: {value.phone.value, str(value.birthday.value), value.email.value, value.adress.value}\n"
        return result.strip()


def main():
    print("Доступні команди:'hello','add','change','phone','show all','good bye','close','exit'" '\n' 'Для додвання контакту: Імя номер др емейл')
    while True:
        input_str = input("Enter command: ").lower().strip()
        if input_str:
            CommandHandler.command_handler(input_str)


if __name__ == "__main__":
    contact_list = AddressBook()
    name_1 = Name('Bill')
    phone_1 = Phone('1234567890')
    b_day_1 = Birthday('1992-04-04')
    email_1 = Email('asda@gmail.com')
    adress_1 = Adress('Pushkina 28')

    name_2 = Name('serg')
    phone_2 = Phone('1234567890')
    b_day_2 = Birthday('1995.3.2')
    email_2 = Email('asd.a@gmail.com')
    adress_2 = Adress('Pushkina 28')

    name_3 = Name('Oleg')
    phone_3 = Phone('1234567890')
    b_day_3 = Birthday('2 02 1967')
    email_3 = Email('asd123a@gmail.com')
    adress_3 = Adress('Pushkina 28')

    name_4 = Name('Max')
    phone_4 = Phone('1234567890')
    b_day_4 = Birthday('19*02*1999')
    email_4 = Email('asda.123@gmail.com')
    adress_4 = Adress('Pushkina 28')

    rec_1 = Record(name_1, phone_1, b_day_1, email_1, adress_1)
    rec_2 = Record(name_2, phone_2, b_day_2, email_2, adress_2)
    rec_3 = Record(name_3, phone_3, b_day_3, email_3, adress_3)
    rec_4 = Record(name_4, phone_4, b_day_4, email_4, adress_4)
    ab = AddressBook()

    ab.add_record(rec_1)
    ab.add_record(rec_2)
    ab.add_record(rec_3)
    ab.add_record(rec_4)

    print(rec_1.adress)
    print(rec_2.adress)

    print('All Ok')

    print(rec_1.birthday)
    print(rec_2.birthday)
    print(rec_3.birthday)
    print(rec_4.birthday)
    main()
