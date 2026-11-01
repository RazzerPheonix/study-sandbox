a = input("число 1: ")
b = input("число 2: ")

op = input("операция: ")

a = int(a)
b = int(b)

if op == "+":
    print(a+b)
elif op == "-":
    print(a-b)
elif op == "*":
    print(a*b)
elif op == "/":
    if b == 0:
        print("делить на ноль нельзя")
    else:
        print(a/b)
else:
    print("Операция неизвестна")