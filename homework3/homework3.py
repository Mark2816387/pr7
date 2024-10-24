print("В соответствии с 4 вариантом, переводим в шестяричную систему счистления")
def get_number():
    while True:
        try:
            num = int(input("Введите целое число: "))  
            return num
        except ValueError:
            print("Ошибка: введите корректное целое число!")  

def convert_to_base_6(number):
    if number == 0:
        return '0'
    
    is_negative = number < 0
    number = abs(number)
    
    base_6_digits = []
    
    while number > 0:
        base_6_digits.append(str(number % 6))
        number //= 6
    
    base_6_digits.reverse()
    
    result = ''.join(base_6_digits)
    
    return '-' + result if is_negative else result

number = get_number()

base_6_representation = convert_to_base_6(number)

print(f"Число {number} в шестиричной системе: {base_6_representation}")
