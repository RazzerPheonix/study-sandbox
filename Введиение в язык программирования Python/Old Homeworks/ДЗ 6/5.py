x = input("Введите число: ")


while True:
    i = 0
    print("-"*4,"Menu","-"*4)
    print("1. Определить количество чисел")
    print("2. Вычеслить сумму чисел в цифре")
    print("3. Вычеслить среднее арифметическое")
    print("4. Определить кол-во нулей")
    print("5. Выход")

    q = int(input("Выберите действие: "))
    
    if q == 1:
        num = 0
        while i < len(x):
            num += 1
            i += 1
        print("Кол-во чисел в цифре = ", num)
    elif q == 2:
        num = 0
        while i < len(x):
            num += int(x[i])
            i += 1
        print("Сумма чисел в цифре = ",num)
    elif q == 3:
        num = 0
        while i < len(x):
            num += int(x[i])
            i += 1
        count = num / i
        print("Сред. арифм = ",count)
    elif q == 4:
            num = 0
            while i < len(x):
                if x[i] == '0':
                    num += 1
                i += 1
            print("Кол-во нулей = ",num)
    elif q == 5:
        break
    else:
        print("Неверный пункт меню")
        continue