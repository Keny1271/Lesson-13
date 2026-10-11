def add(P , Q):
    return P + Q
def subtract(P , Q):
    return P - Q
def multiply(P , Q):
    return P * Q
def divide(P , Q):
    return P / Q
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
choice = input("Enter choice(1/2/3/4):")
num_1 = float(input("Enter first number: "))
num_2 = float(input("Enter second number: "))
if choice == '1':
    print(num_1, "+", num_2, "=", add(num_1, num_2))
elif choice == '2':
    print(num_1, "-", num_2, "=", subtract(num_1, num_2))
elif choice == '3':
    print(num_1, "*", num_2, "=", multiply(num_1, num_2))
elif choice == '4':
    print(num_1, "÷", num_2, "=", divide(num_1, num_2))
    if num_2 == 0:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid input")