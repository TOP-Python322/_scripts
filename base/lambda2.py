def calculator(num1: float, num2: float, operation: 'function') -> float:
    return operation(num1, num2)


operations = [
    lambda x, y: x + y,
    lambda x, y: x - y,
    lambda x, y: x * y,
    lambda x, y: x / y,
    lambda x, y: x // y,
    lambda x, y: x % y,
    lambda x, y: x ** y,
]
results = []
prompt = 'введите число: '
n1, n2 = float(input(prompt)), float(input(prompt))
for oper in operations:
    results += [calculator(n1, n2, oper)]
print(*results)
