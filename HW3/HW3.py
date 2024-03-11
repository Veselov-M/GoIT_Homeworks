#Блок імпорту бібліотек/моудлів
 
from datetime import datetime, timedelta
import random
import re

#Завдання 1 (різниця між вказаною і сьогоднішньою датами)

def get_days_from_today(date):
    try:
        date_format = datetime.strptime(date, '%Y-%m-%d').date() #Перевірка введених данних на правильність формату

    except:
        print('Your date not in correct format, please enter date in format: YYYY-MM-DD')
        return None
    
    else:
        current_date = datetime.today().date()
        days_diff = current_date.toordinal() - date_format.toordinal()
        print(f'Days diff is: {days_diff}')
        return (days_diff)
    
#Завдання 2 (Виграшні числа)

def get_numbers_ticket(min, max, quantity):
    try:
        is_condition_correct = min >= 1 and max <= 1000 and (quantity >= min and quantity <= max) and min < max  #Перевірка вхідних данних
    
    except:
        is_condition_correct = False

    if is_condition_correct:
        random_numbers = set()

        while len(random_numbers) < quantity:  #Цикл генерації унікальних виграшних номерів
            random_numbers.add(random.randint(min, max))

        print(f'Your numbers: {sorted(random_numbers)}')
        return(sorted(random_numbers))

    else:
        print('Please enter correct conditions')
        return None
    
#Завдання 3 (Телефонні номери)
    
def normalize_phone(phone_number):
    correct_numbers = []

    for phones in phone_number: #Перебір усіх наданих номерів

        number_apart = re.findall(r'\d+', phones) #Видалення зайвих знаків в номерах 
        number_combined = ''.join(number_apart) #Об`єднання цифр в номер

        if len(number_combined) == 12: #Перевірка на те чи номер є дійсним

            if number_combined.startswith('38'): #Перевірка чи номер належить громадянам України
                number_combined = '+' + number_combined
                correct_numbers.append(number_combined) #В разі проходження усіх перевірок додання номеру до загального списку

        elif len(number_combined) == 10: #Перевірка на те чи номер є дійсним

            if number_combined.startswith('0'):
                number_combined = '+38' + number_combined
                correct_numbers.append(number_combined) #В разі проходження усіх перевірок додання номеру до загального списку


    print(f'All correct numbers: {correct_numbers}')
    return (correct_numbers)    

#Завдання 4 (Привітання з днем народження)

def get_upcoming_birthdays(users):

    current_date = datetime.today().date()

    actual_birthday_user = {}
    actual_birthday_full = []

    this_week_birthday_user = {}
    this_week_birthday_full = []

    for user in users: #Перебір усіх користувачів
        user_birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date() 
        user_birthday_celebrate = datetime(current_date.year, user_birthday.month, user_birthday.day).date()

        if user_birthday_celebrate < current_date: #Перевірка, чи вже пройшов день народження
            user_birthday_celebrate = datetime(user_birthday_celebrate.year + 1, user_birthday_celebrate.month, user_birthday_celebrate.day).date()

        if user_birthday_celebrate.isoweekday() >= 6:  #Переніс святкування в разі вихідного дня, на найближчий понеділок
            days_to_monday = 8 - user_birthday_celebrate.isoweekday()
            user_birthday_celebrate += timedelta(days=days_to_monday)

        days_diff = user_birthday_celebrate.toordinal() - current_date.toordinal() #Різниця між датою святкування та сьогоднішнью датою, для знаходження найближчих 7 свят

        if days_diff <= 7:
            this_week_birthday_user = {"Name": user.get("name"), "Congratulation date": user_birthday_celebrate.strftime("%Y.%m.%d")}
            this_week_birthday_full.append(this_week_birthday_user)
        
        actual_birthday_user = {"Name": user.get("name"), "Congratulation date": user_birthday_celebrate.strftime("%Y.%m.%d")}
        actual_birthday_full.append(actual_birthday_user)
    
    print(actual_birthday_full) #Повний список святкування днів народження всіх користувачів
    print(this_week_birthday_full) #Список святкування днів народження на наступні 7 днів
    return (actual_birthday_full, this_week_birthday_full)


        



