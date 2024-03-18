import re
from pathlib import Path

def total_salary(path): 
    
    file_path = Path(path)  #Парсинг данних типу str в тип Path
    if file_path.exists():  #Перевірка, чи доступний такий шлях
        with open(path, 'r') as file_data: #Відкриття файлу для читання
            total_workers = 0
            total_salary = 0
            splited_lines = file_data.readlines() #Запис усіх строк файлу в змінну
            
            for line in splited_lines:
                splited_data = line.split(',') #Розділ строки на ім`я та заробітню плату

                total_salary += int(splited_data[1]) #Підрахунок заробітньої плати
                total_workers += 1 #Підрахунок робітників
            average_salary = total_salary / total_workers #Середня зп

            print(f"Загальна сума заробітної плати: {total_salary}, Середня заробітна плата: {average_salary}")
            return(total_salary, average_salary)
        
total_salary('ex1_additional_data.txt') #Виклик функції з данним з прикладу