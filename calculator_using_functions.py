print("=== Simple Python Calculator ===")

def calculator():
    num1 = float(input("Enter num1: "))
    num2 = float(input("Enter num2: "))
    opt = input("Choose operator (+, -, *, /): ")

    if opt == "+":
        print(num1, "+", num2, "=", num1 + num2)
    elif opt == "-":
        print(num1, "-", num2, "=", num1 - num2)
    elif opt == "*":
        print(num1, "*", num2, "=", num1 * num2)
    elif opt == "/":
        if num2 == 0:
            print("Cannot divide by zero!")
        else:
            print(num1, "/", num2, "=", num1 / num2)
    else:
        print("Choose symbol from the list only...")


while True:
    calculator()
    a = input("Do you want to Continue calculating (YES/NO): ")

    if a.lower() == "yes":
        continue
    elif a.lower() == "no":
        print("Thank You!")
        break
    else:
        print("Invalid input, continuing...")