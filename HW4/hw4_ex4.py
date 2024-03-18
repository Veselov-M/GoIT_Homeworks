from pathlib import Path, PurePath

def parse_input(user_input): #Обробка команди, а також аргументів переданих користувачем
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts): #Функція додавання нового контакту
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts): #Функція зміни вже існуючого контакту
    name, phone = args
    if name in contacts: 
        contacts[name] = phone
        return "Contact updated."
    else:
        return "This contact is not created yet."

def show_phone(args, contacts): #Функція виводу вже існуючого контакту у консоль
    if args in contacts:
        return contacts[args]
    else: 
        return "This contact is not created yet."

def show_all(contacts): #Функція виводу всіх існуючих контактів
    return contacts

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True: #Нескінченний цикл бота
        user_input = input("Enter a command: ") #Аргументи передані користувачем
        command, *args = parse_input(user_input) #Розбивка переданих дланних користувача

        if command in ["close", "exit"]: #Блок виклику наявних команд бота
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args[0], contacts))
            
        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.")

if __name__ == "__main__": #Запуск файлу з консолі
    main()
