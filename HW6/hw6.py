from collections import UserDict

class Field: #Батьківський класс для перетворення значення в формат строки
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field): #Класс для зберігання імені
    def __init__(self, value):
        super().__init__(value)
        self.name = value


class Phone(Field): #Класс для зберігання і валідації номеру телефону
    def __init__(self, value):

        if len(value) == 10:
            super().__init__(value)
        else:
            super().__init__(False)


class Record: #Основний класс для роботи з окремим записом 
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone): #Додавання телефону до списку вже існуючих при умові що телефон валідний
        if Phone(phone).value:
            self.phones.append(Phone(phone).value)
        else:
            print("You enter not correct phone")
    
    def find_phone(self, phone): #Пошук телефону за номером
        if phone in self.phones:
            return phone
        else:
            print('Phone not find')
        
    def edit_phone(self, old_num, new_num): #Зміна одного номеру на інший
        record = self
        try:
            record.remove_phone(old_num)
            record.add_phone(new_num)
            book.add_record(record)
        except:
            print('Phone dont found')

    def remove_phone(self, number_remove): #Видалення номеру якщо він присутній

        try:
            self.phones.remove(number_remove)
        except:
            print('Phone dont found')

    def __str__(self):
        return f"Contact name: {self.name}, phones: {'; '.join(p for p in self.phones)}"

class AddressBook(UserDict): #Словник що містить всі записи. Ключ - Ім`я, значення - об`єкт классу Record

    def add_record(self, record): #Додавання запису до довідника
        self.data[str(record.name)] = record

    
    def find(self, name): #Знаходження записа в довіднику

        if name in self.data:
            return self.data[name]
        else:
            return None
    
    def delete(self, name): #Видалення запису з довідника
        try:
            del self.data[name]
        except:
            print('Contact dont found')
            

book = AddressBook()

john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
book.add_record(john_record)
print(john_record)

john = book.find("John")
john.edit_phone("1234567890", "1112223333")
print(john)

phone = john.find_phone("1112223333")
print(phone, john.name)

book.delete("John")




