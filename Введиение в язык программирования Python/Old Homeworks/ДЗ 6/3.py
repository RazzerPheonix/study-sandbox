x = int(input("Введите ширину: "))

i = 0

while i < x:
    if i == 0 or i == x - 1: 
        print("*" * x)
    else:
        print("*" + " " * (x-2) + "*")
    i += 1