print("В соответствии с 4 вариантом, уравнение 3*a + 3 - b + 4*c")
def get_number(yp_name):
    while True:
        try:
            num = float(input(f"Введите значение для {yp_name} (от -1000000 до 1000000): "))
            if -1000000 <= num <= 1000000:
                return num
            else:
                print("Ошибка: число должно быть в диапазоне от -1000000 до 1000000!")
        except ValueError:
            print("Ошибка: введите корректное число!")

def solve_equation(a, b, c):
    return 3*a + 3 - b + 4*c

a = get_number('a')
b = get_number('b')
c = get_number('c')

x = solve_equation(a, b, c)

print(f"Решение уравнения: x = 3*{a} + 3 - {b} + 4*{c} = {x}")
