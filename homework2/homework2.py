print("Сделал Ягафаров Марк из ПИ-332Б")
def get_number():
    while True:
        try:
            num = int(input("Введите целое десятичное число: "))
            return num
        except ValueError:
            print("Ошибка: введите корректное целое число!")

def choose_conversion():
    while True:
        choice = input("Выберите систему счисления для перевода (2 - двоичная, 8 - восьмеричная): ")
        if choice in ('2', '8'):
            return choice
        else:
            print("Ошибка: введите 2 или 8!")

number = get_number()
choice = choose_conversion()

if choice == '2':
    print(f"Число {number} в двоичной системе: {bin(number)[2:]}")
elif choice == '8':
    print(f"Число {number} в восьмеричной системе: {oct(number)[2:]}")
