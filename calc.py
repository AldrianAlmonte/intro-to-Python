# imports


# global variables


# functions
def print_menu():
    print("*** PyCalc ***")
    print("_________________")
    print("[1] Sum")
    print("[2] Substract")
    print("[3] Multiply")
    print("[4] Division")

    print("[ex] Exit")


def sum(num1, num2):
    result = num1 + num2
    print("the result is " + str(result))


def substract(num1, num2):
    result = num1 - num2
    print("the result is " + str(result))


def multiply(num1, num2):
    result = num1 * num2
    print("the result is " + str(result))


def divide(num1, num2):
    if num2 == 0:
        print("error")
    else:
        result = num1 / num2
        print("the result is " + str(result))


# plain instructions
opt = ""
while opt != "ex":
    print_menu()

    opt = input("Please select an option: ")
    if opt == "ex":
        break  # kill the loop

    num1 = float(input("Please provide num1: "))
    num2 = float(input("Please provide num2: "))

    if opt == "1":
        sum(num1, num2)

    elif opt == "2":
        substract(num1, num2)

    elif opt == "3":
        multiply(num1, num2)

    elif opt == "4":
        divide(num1, num2)

    print("")
    input("Press Enter to continue...")
    print("\n\n\n")

print("\n\n\n")
print("Thank you for using PyCalc today!")
