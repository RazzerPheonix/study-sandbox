a = int(input("Введите начало диапозона: "))
b = int(input("Введите конец диапозона: "))

for i in range(a, b + 1):
    if i % 7 == 0:
        print(i)