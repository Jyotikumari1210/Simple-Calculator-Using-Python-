print("~~~~~~Simple Calculator~~~~~~")
while True:
    print(" 1 For Addition")
    print(" 2 For Subtraction")
    print(" 3 For Multiplication")
    print(" 4 For Division")
    print(" 5 To Exit")

    choice = input("Enter your choice:")

    if choice == "5":
        print("Exiting the program.")
        break

    num1 = float(input("Enter Number 1:"))
    num2 = float(input("Enter Number 2:"))

    if choice == "1":
        print(num1, "+", num2, "=", (num1 + num2))
    elif choice == "2":
        print(num1, "-", num2, "=", (num1 - num2))
    elif choice == "3":
        print(num1, "*", num2, "=", (num1 * num2))
    elif choice == "4":
        if num2 == 0.0:
            print("Divide by 0 Error")
        else:
            print(num1, "/", num2, "=", (num1 / num2))
    else:
        print("Invalid choice")
