from collections import UserDict
from datetime import datetime
import pickle
from abc import abstractmethod, ABCMeta

class MyBaseClass(metaclass=ABCMeta):
    @abstractmethod
    def exit(book):
        pass

    @abstractmethod
    def greeting():
        pass

    @abstractmethod
    def add(book, *args): 
        pass
    
    @abstractmethod
    def change(book, *args): 
        pass

    @abstractmethod
    def phone(book, *args):
        pass

    @abstractmethod
    def all(book):
        pass

    @abstractmethod
    def remove(book, *args):
        pass

    @abstractmethod
    def add_birthday(book, *args):
        pass

    @abstractmethod
    def show_birthday(book, *args):
        pass

    @abstractmethod
    def birthdays(book):
        pass


class Main(MyBaseClass):
        def exit(book):
            print("Good bye!")
            save_data(book)

        def greeting():
            print("How can I help you?")

        def add(book, *args): 
            book.add_record(*args)

        def change(book, *args): 
            book.change_record(*args)

        def phone(book, *args):
            if book.find(*args):
                print(book.find(*args))
            else:
                print("Contact not found")

        def all(book):
            book.all_contacts()

        def remove(book, *args):
            book.delete(*args)

        def add_birthday(book, *args):
            book.add_bday(*args)

        def show_birthday(book, *args):
            book.show_birthday(*args)

        def birthdays(book):
            book.birthdays()


def save_data(book, filename="addressbook.pkl"): #Збереження данних у файл
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"): #Читання данних з файлу/створення нового пустого довідника
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            print("Give me name and phone please.")
        except KeyError:
            print("User with this name has not been created yet.")
        except IndexError:
            print("Please, enter the name of user.")
        except TypeError:
            print("Please, enter correct data.")
        except AttributeError:
            print("Dont found such contact")

    return inner

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        super().__init__(value)
        self.name = value


class Phone(Field):
    def __init__(self, value):

        if len(value) == 10:
            super().__init__(value)
        else:
            super().__init__(False)

class Birthday(Field):
    def __init__(self, value):
        try:
            super().__init__(datetime.strptime(value, '%d.%m.%Y').date())
            print("Birthday added")
        except:
            print('Data not in correct format')


class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        if Phone(phone).value:
            self.phones.append(Phone(phone).value)
            print("Contact added")
        else:
            print("You enter not correct phone")

    def add_birthday(self, day):
        rec = self
        rec.birthday = Birthday(day)
        return(rec)
    
    def show_near_bdays(all_bdays: dict): 
        congrat_list = {}
        for name, day in all_bdays.items():
            if Record.is_congrat_week(day.value):
                congrat_list[name] = day

        if len(congrat_list) > 0:
            print("Next week b-days:")
            for name, day in congrat_list.items():
                print("Contact name: ", name.value, " b-day date: ", day.value)
        else:
            print('There is no b-days in nearest week!')

    def is_congrat_week(data):
        current_date = datetime.today().date()
        current_year = int(current_date.year)
        data = data.replace(year=current_year) 
        days_diff = data.toordinal() - current_date.toordinal()
        week_day = data.isoweekday()

        week_end = 14 - week_day
        if days_diff >= 0 and days_diff <= week_end:
            return True
        else:
            return False
        
    def __str__(self):
        return f"Contact name: {self.name}, phones: {'; '.join(p for p in self.phones)}"

class AddressBook(UserDict):
    @input_error
    def add_record(self, name, phone, *_ ):
        if self.find(name):
            record = self.find(name)
        else:
            record = Record(name)

        record.add_phone(phone)

        self.data[name] = record

    @input_error
    def find(self, name, *_):

        if name in self.data:
            return self.data[name]
        else:
            return None
        
    @input_error
    def delete(self, name, *_):
        try:
            del self.data[name]
        except:
            print('Contact not found')

    @input_error
    def change_record(self, name, new_num, *_):
        if self.find(name) and new_num:
            self.delete(name)
            self.add_record(name, new_num)
        else:
            print("Contact not found")
        
    def all_contacts(self):
        if  self.data.values():
            for record in self.data.values():
                print(record)
        else:
            print("You dont add any contact yet")

    @input_error
    def add_bday(self, name, date, *_):
        record = self.find(name)
        record.add_birthday(date)
        self.data[name] = record

    #@input_error
    def show_birthday(self, name, *_):
        ppl = self.find(name)
        print(ppl.birthday)
    
    def birthdays(self):
        b_days = {}
        for rec in self.data.values():
            if rec.birthday:
                b_days[rec.name] = rec.birthday
        Record.show_near_bdays(b_days)
        

@input_error
def parse_input(user_input): #Обробка команди, а також аргументів переданих користувачем
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args
            

def logic():
    book = load_data()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        match command:
            case "close" | "exit": 
                Main.exit(book)
                break

            case "hello":
                Main.greeting()

            case "add": 
                Main.add(book, *args)

            case "change": 
                Main.change(book, *args)

            case "phone":
                Main.phone(book, *args)

            case "all":
                Main.all(book)

            case "remove":
                Main.remove(book, *args)

            case "add-birthday":
                Main.add_birthday(book, *args)

            case "show-birthday":
                Main.show_birthday(book, *args)

            case "birthdays":
                Main.birthdays(book)

            case _:
                print("Invalid command.")

if __name__ == "__Main__": #Запуск файлу з консолі
    logic()




