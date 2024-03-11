import re
from pathlib import Path

def total_salary(path):
    
    file_path = Path(path)
    if file_path.exists():
        with open(path, 'r') as file_data:
            total_workers = 0
            total_salary = 0
            splited_lines = file_data.readlines()
            
            for line in splited_lines:
                number_apart = re.findall(r'\d+', line) 
                number_combined = ''.join(number_apart)

                total_salary += int(number_combined)
                total_workers += 1
            average_salary = total_salary / total_workers

            print(f"Загальна сума заробітної плати: {total_salary}, Середня заробітна плата: {average_salary}")
            return(total_salary, average_salary)
