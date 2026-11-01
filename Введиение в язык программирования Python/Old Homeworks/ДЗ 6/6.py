x = int(input("Введите размер клетки: "))
y = 8

i = 0

while i < y:
        if i % 2 == 0:
                print(("*" * x +"-" * x) * 4)
                i += 1
        else:        
                print(("-" * x +"*" * x) * 4)
                i += 1