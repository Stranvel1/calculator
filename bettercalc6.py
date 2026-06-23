while True:
    x = float(input("введите первое число: "))
    if x % 2 == 0:
        print("первое число четное")
    else:
        print("первое число нечетное")
    y = float(input("введите второе число: "))
    if y % 2 == 0:
        print("второе число четное")
    else:
        print("второе число нечетное")
    action = input("какое действие? (+, -, *, /, **)")
    if action == "+":
        print(x + y)
    elif action == "-":
        print(x + y)
    elif action == "*":
        print(x * y)
    elif action == "/":
        if y == 0:
            print("на ноль делить нельзя!")
        else:
            print(x / y)
    elif action == "**":
        print(x ** y)
    else:
        print("я не знаю такого действия")
    
    again = input("хотите продолжить? (да/нет)(yes/no)")
    if again == "нет" or again == "no":
        print("до свидания!")
        break