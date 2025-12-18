class Calculator():
 n_1 = float(input("Введите первое число: "))
 n_2 = float(input("Введите второе число: "))
 print("Выберите операцию: + , - , * , / .")
 q = input("Операция: ")

 add = n_1 + n_2
 subract = n_1 - n_2
 multiply = n_1 * n_2
 if n_2 !=0:
     divice = n_1 / n_2
 else:
     print("Ошибка: ")
     
 if q == "+":
     print("Результат сложения: ", add )
 elif q == "-":
     print("Результат вычитания: ", subract)
 elif q == "*":
     print("Результат умножения: ", multiply)
 elif q == "/":
     if n_2 !=0:
         print("Результат деления: ", divice)
     else:
         print("Деление на ноль!")