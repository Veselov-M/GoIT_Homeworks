from pathlib import Path

def get_cats_info(path):

    file_path = Path(path)#Парсинг данних типу str в тип Path
    if file_path.exists(): #Перевірка, чи доступний такий шлях
        with open(path, 'r') as file_data: #Відкриття файлу для читання
            all_cats = []
            splited_lines = file_data.readlines() #Запис усіх строк файлу, списком в змінну
            
            for line in splited_lines:
                cat_info = line.split(',') #Розділ строки на id, ім`я та вік кота
                cat_dict = {"id":cat_info[0] , "name":cat_info[1] , "age":cat_info[2].replace('\n', '')} #Рознесення до словника відповідної частинки інформації
                all_cats.append(cat_dict) #Додавання словника до загального спсику котів
            
            print(all_cats)
            return(all_cats)
        
get_cats_info('ex2_additional_data.txt') #Виклик функції з данним з прикладу
