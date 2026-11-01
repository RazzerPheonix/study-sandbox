a = int(input())
b = int(input())
c = int(input())

if a + b > c and b + c > a and a + c > b:
    if a == b == c:
        print("Треугольник равносторонний")
    elif a == b or a == c or b == c:
        print("Треугольник равнобедренный")
    elif a != b and a != c and b != c:
        print("Треугольник разносторонний")
else:
    print("Это не треугольник")