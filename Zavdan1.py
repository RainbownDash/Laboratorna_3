"""Дано два цілих числа a і b. Виведіть всі числа від a до b включно, в
порядку зростання, якщо a < b, або в порядку спадання у іншому
випадку."""
#Створення зміних для збереження двох цілочисельних значень
a = int(input("Введіть значення a: "))
b = int(input("Введіть значення b: "))
#Створення зміної для збреження кроку для циклу
step = 1
#Перевірка на відповідніст умови a < b
if a < b:
#Створення циклу для вивдення від а до b в порядку спадання
    for i in range(a, b+1, 1):
        #Виведення резулятату
        print(a)
        #Збільшення зміної а на 1
        a += 1
#Виконання умови, якщо попередня умова не була виконана
else:
#Створення циклу для вивдення від b до a в порядку спадання
    for i in range(a, b-1, -1):
        #Виведення резулятату
        print(a)
        #Зменження зміної а на 1
        a -= 1