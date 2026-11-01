import random


while True:
    i = 0
    print("-"*4,"Menu","-"*4)
    print("1. Лёгкий")
    print("2. Средний")
    print("3. Сложно")
    print("4. Гуру")
    print("5. Выход")

    q = int(input("Выберите сложность"))
    
    if q == 1:
        cnt = 3
        mx = 3
    elif q == 2:
        cnt = 6
        mx = 6
    elif q == 3:
        cnt = 9
        mx = 9
    elif q == 4:
        cnt = 12
        mx = 10
    elif q == 5:
        print("Выход из программы.")
        break
    else:
        print("Неверный пункт меню!")
        continue
    f = 0
    for _ in range(cnt):
                x = random.randint(1, mx)
                y = random.randint(1, 10)
                print(x, "*", y, "=")
                c = int(input("Введите ответ"))
                if c == x * y:
                    f += 1
                else:
                    print("Неправильный ответ")
    print("Тестирование завершено! Правильных ответов:", f, "из", cnt)
    
    if f == cnt:
        print("Оценка: 5 (Отлично!)")
    elif f >= cnt / 2:
        print("Оценка: 4 (Хорошо)")
    else:
        print("Оценка: 3 (Стоит потренироваться)")
    print()