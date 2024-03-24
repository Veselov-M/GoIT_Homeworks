
def input_error(func):  #Обробка винятків
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "User with this name has not been created yet."
        except IndexError:
            return "Please, enter the name of user."

    return inner

@input_error
def parse_input(user_input): #Обробка команди, а також аргументів переданих користувачем
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts): #Функція додавання нового контакту
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts): #Функція зміни вже існуючого контакту
    name, phone = args
    if name in contacts: 
        contacts[name] = phone
        return "Contact updated."
    else:
        return "User with this name has not been created yet."

@input_error
def show_phone(args, contacts): #Функція виводу вже існуючого контакту у консоль
    return contacts[args[0]]

@input_error   
def show_all(contacts): #Функція виводу всіх існуючих контактів
    return contacts

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
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
            print(show_phone(args, contacts))
            
        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.")

if __name__ == "__main__": #Запуск файлу з консолі
    main()