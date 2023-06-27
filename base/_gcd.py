def gcd(num1: int, num2: int) -> int:
    num1, num2 = max(num1, num2), min(num1, num2)
    if num2 > 0:
        print(f'перед рекурсивным вызовом:\t{num1 = },\t{num2 = }')
        result = gcd(num2, num1 % num2)
        print(f'после рекурсивного вызова:\t{result = }')
        return result
    else:
        print(f'последний рекурсивный вызов:\t{num1 = },\t{num2 = }')
        return num1

