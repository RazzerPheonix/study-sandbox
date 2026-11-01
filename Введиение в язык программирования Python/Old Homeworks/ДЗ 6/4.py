x = int(input("Введите ширину: "))
y = int(input("Введите высоту: "))

i,j = 0, 0

while i < y:
    if i == 0 or i == y - 1: 
        print("*" * x)
    else:
        print("*" + " " * (x-2) + "*")
    i += 1