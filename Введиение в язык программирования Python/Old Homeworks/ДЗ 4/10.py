password = input("Введите пароль: ")
errors = 0

if len(password) < 8:
    print("Ошибка: пароль должен быть не менее 8 символов.")
    errors += 1

if not any(char.isdigit() for char in password):
    print("Ошибка: пароль должен содержать хотя бы одну цифру.")
    errors += 1

if not any(char.isupper() for char in password):
    print("Ошибка: пароль должен содержать хотя бы одну заглавную букву.")
    errors += 1

if errors == 0:
    print("Поздравляем! Пароль надёжный.")