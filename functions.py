def add(a, b):
    return a + b
def subtract(a, b):
    return a - b 
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b 
running = True 
while running:
    try: 
        num1 = int(input("Первое число: "))
        operation = input("Выбери операцию(+, -, *, /): ")
        num2 = int(input("Второе число: "))
        if operation == "+":
            print("Ответ:", add(num1, num2))
        elif operation == "-":
            print("Ответ:", subtract(num1, num2))
        elif operation == "*":
            print("Ответ:", multiply(num1, num2)) 
        elif operation == "/":
            print("Ответ:", divide(num1, num2))
        else:
            print("Неизвестная операция")
    except:
        print("Ошибка! Введи число прасильно")        
    stop = input("Остановить калькулятор? yes/no: ")
    if stop == "yes":
        running = False            