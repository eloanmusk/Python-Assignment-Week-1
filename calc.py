num1 = int(float(input("Enter first number: ")))
num2 = int(float(input("Enter second number: ")))

def results(x, y):
    print(f"Sum: {x + y}")
    print(f"Difference: {x - y}")
    print(f"Multiplication: {x * y}")
    print(f"Division: {x / y}")
    print(f"Modulus: {x % y}")
    print(f"Int division: {x // y}")
    print(f"Power: {x ** y}")

results(num1, num2)