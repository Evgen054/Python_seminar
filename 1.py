# 1. Сумма трех Посчитайте сумму трех введенных целых чисел

a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
c = int(input("Введите число c: ")) 
print(f"Сумма: {a+b+c}")


# Задача 1
# За день машина проезжает n километров. Сколько 
# дней нужно, чтобы проехать маршрут длиной m 
# километров? При решении этой задачи нельзя 
# пользоваться условной инструкцией if и циклами.


n = int(input("Км за день: "))
m = int(input("Км всего: "))

print( ((-m)//(n))* (-1))
