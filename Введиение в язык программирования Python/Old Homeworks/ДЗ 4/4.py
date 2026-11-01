a = int(input())
b = int(input())
c = int(input())

if a == b and b == c:
    print("Все числа равны")
elif b >= a and b >= c:
    print("Наибольшее число: b")
elif a >= b and a >= c:
    print("Наибольшее число: a")
else:
    print("Наибольшее число: c")