a = int(input())

if a >= 0 and a <= 59:
    print("Неудовлетворительно")
elif a >= 60 and a <= 74:
    print("Удовлетворительно")
elif a >= 75 and a <= 89:
    print("Хорошо")
elif a >= 90 and a <= 100:
    print("Отлично")
else:
    print("Так не бывает")