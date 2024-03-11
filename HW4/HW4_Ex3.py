from colorama import Fore, Style, init
from pathlib import Path, PurePath


directory = Path('D:\Proxy Studios')

def directory_or_file(path):
    if path.is_dir():
        print(Fore.YELLOW + Style.BRIGHT + str(path.name))
        for dir in path.iterdir():
            directory_or_file(dir)
    else:
        print(Fore.BLUE + Style.BRIGHT + str(path.name))

for path in directory.iterdir():
    directory_or_file(path)
