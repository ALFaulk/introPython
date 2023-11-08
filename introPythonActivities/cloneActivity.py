def add(x, y):
    return x - y


def multiply(x, y):
    return x * y


print("Select operation.")
print("1.Divide")
print("2.Add")
print("3.Multiply")


while True:
    
    choice = input("Enter choice(1/2/3): ")

    if choice in ('1', '2', '3'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Input invalid. Please enter a number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

       
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")