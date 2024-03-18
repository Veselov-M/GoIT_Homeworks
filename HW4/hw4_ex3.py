import sys
from colorama import Fore, Style, init
from pathlib import Path, PurePath


def directory_or_file(path, deep):
    if path.is_dir(): #Перевірки чи папка чи файл
        print(Fore.YELLOW + Style.BRIGHT + str(path.name))
        for dir in path.iterdir(): #Відкриття папки і перебір всіх файлів що до неї входять
            print(Fore.YELLOW + Style.BRIGHT + '--' * deep, end='') #Вивід назви папки
            directory_or_file(dir, deep + 1) #Рекурсія для розкриття всіх папок до найнижчого рівня

    else:
        print(Fore.BLUE + Style.BRIGHT + ' ' + str(path.name)) #Вивід назви файлу

if __name__ == "__main__": #Запуск файлу з консолі

    if len(sys.argv) > 1: #Обробка виключень коли не передано жодного шляху
        if Path(sys.argv[1]).exists(): #Обробка виключень коли шлях не є доступним
            directory = Path(sys.argv[1]) #Приведення типу str в тип Path 
            for path in directory.iterdir(): #Цикл перебору всіх файлів за наявним шляхом
                deep = 1
                directory_or_file(path, deep)

        else:
            print(Fore.RED + Style.BRIGHT + 'Path dont exist' + Style.RESET_ALL) 

    else:
        print(Fore.RED + Style.BRIGHT + 'You dont enter the' + Style.RESET_ALL)

