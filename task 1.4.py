# <->   задание 1.4   <-> (Попытка коммита 2)
# Название: 
# - Проверка на палиндром
# Описание: 
# - На вход подается строка, все символы находятся в нижнем регистре и без пробелов. 
# - Напишите функцию, которая будет возвращать True, если строка является палиндромом и False, если строка палиндромом не является.

# Task
def isPalindrom(string : str) -> bool:
    if string.__eq__(''): return False 
    return string == string[::-1]

# Test
while True:           
    print(isPalindrom(input('Is Palindrom:')))