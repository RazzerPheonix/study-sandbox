a = int(input("Введите начало диапозона: "))
b = int(input("Введите конец диапозона: "))
c = 0
c = int(c)

for i in range(a, b + 1):
    print("основной диапозон: " ,i)
    if i % 7 == 0:
        print("кратно 7: ",i)
        
for i in range(b, a - 1, - 1):
    print("перевёрнутый диапозон: " ,i)
    if i % 5 == 0:
        c += 1
print(c)