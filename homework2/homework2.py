def get_number():
    while True:
        try:
            num = int(input("Введите целое число: "))  
            return num
        except ValueError:
            print("Ошибка: введите корректное целое число!")  

def convert_to_binary(number):
    if number < 0:
        return '-' + bin(abs(number))[2:]
    else:
        return bin(number)[2:]

def convert_to_octal(number):
    if number < 0:
        return '-' + oct(abs(number))[2:]
    else:
        return oct(number)[2:]

number = get_number()

binary_representation = convert_to_binary(number)
octal_representation = convert_to_octal(number)

print(f"Число {number} в двоичной системе: {binary_representation}")
print(f"Число {number} в восьмеричной системе: {octal_representation}")
