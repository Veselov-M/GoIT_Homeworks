import sys
from pathlib import Path
from collections import defaultdict

def parse_log_line(line: str) -> dict: #Парсинг окремого логу на компоненти
    parsed_line = line.split(' ')
    log_info = {parsed_line[2]: str(parsed_line[0]) + " " + str(parsed_line[1]) + " - " + str(' '.join(parsed_line[3::]).removesuffix('\n'))} #Лог має вигляд Ім`я: Детальна інформація
    return (log_info)

def load_logs(file_path: str) -> list: #Відкриття файлу і збереження логів
    parsed_logs = []
    try:
        with open(Path(file_path), 'r') as file:
            all_lines = file.readlines()

            for line in all_lines: #Збереження логів в загальному списку з потрібним виглядом
                parsed_logs.append(parse_log_line(line)) 
    except:
        print('Path is not correct!')
    return parsed_logs 
    
def filter_logs_by_level(logs: list, level: str) -> list: #Додаткова фунція що повертає всі логи з вказаним при запуску рівнем
    logs_level = []
    for log in logs:
        if level.upper() in log:
            logs_level.append(log[level.upper()])
    return logs_level

def count_logs_by_level(logs: list) -> dict: #Функція підрахунку логів по їх рівням
    leveled_logs = defaultdict(int)
    for log in logs:
        for key in log.keys():
            leveled_logs[key] += 1
    return leveled_logs

def display_log_counts(counts: dict): #Вивід фінальної таблиці в консоль
    print(f'Рівень логування | Кількість')
    print(f'---------------- | ---------')
    for key, count in counts.items():
        print(f'{key:<15}', " | ", f'{count:<4}')


if __name__ == "__main__": #Запуск файлу з консолі
    try: #Перевірка на присутність більше 1 переданого при запуску программи параметру
        path = sys.argv[1]
        display =  display_log_counts(count_logs_by_level(load_logs(path)))
        display

        if len(sys.argv) > 2:  #Перевірка на необхідність детальної інформації по певному рівню логів
            level = sys.argv[2]
            filtered_logs = filter_logs_by_level(load_logs(path), level)
            print(f'\nДеталі логів для рівня {level.upper()}:')
            for log in filtered_logs:
                print(log)

    except:
        print('You dont enter any path!')


