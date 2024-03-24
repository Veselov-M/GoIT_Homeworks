from collections import defaultdict

cache = defaultdict(int) #Вирішив створення довіднику винести за функцію caching_fibonacci, так як в іншому випадку при послідовному виклику функції декілька разів 
                         #кеш стирається і функція починає рахуватися з самого початку
   
def caching_fibonacci():

    #cache = defaultdict(int) - як запропоновану у завданні 

    def fibonachi (n: int): #функція підрахунку числа фібоначі
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        else:
            cache[n] = fibonachi(n - 1) + fibonachi(n - 2)  
            return cache[n]
        
    return fibonachi

f = caching_fibonacci() #Присвоєння змінній - функцію 

print(f(5))
print(f(10))
print(f(10))
print(f(10))
