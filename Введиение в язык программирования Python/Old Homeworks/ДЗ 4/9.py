a = int(input("Введите возраст: "))
b = int(input("Введите день недели (1-7): "))

base_price = 500
percent = 0


if a < 12:
    percent -= 50
elif a >= 65:
    percent -= 30

if b == 6 or b == 7:
    percent += 20

final_price = base_price * (1 + percent / 100)
print("Итоговая цена билета:", final_price)