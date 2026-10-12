def main():
    print("----Welcome to Python Calculator----\n")
    while (True):
        print("Select one of the following options:")
        print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Check Even/Odd\n6.Calculate Percentage\n7.Exit")
        option = int(input("Option: "))

        print("")
        match option:
            case 1:
                a, b = take_two_inputs()
                print(f"{a} + {b} = {addition(a, b)}")

            case 2:
                a, b = take_two_inputs()
                print(f"{a} - {b} = {subtraction(a, b)}")

            case 3:
                a, b = take_two_inputs()
                print(f"{a} x {b} = {multiplication(a, b)}")

            case 4:
                a, b = take_two_inputs()
                if b == 0:
                    print("Division by zero is undefined!")
                else:
                    print(f"{a} / {b} = {division(a, b)}")

            case 5:
                a = int(input("Enter a number: "))
                print(even_odd(a))

            case 6:
                a, b = take_two_inputs()
                if b == 0:
                    print("Division by zero is undefined!")
                else:
                    print(f"Percentage of {a} from {b} = {calculate_percentage(a, b)}%")

            case 7:
                print("Exiting Calculator...")
                break;

            case _:
                print("Invalid Choice! Select a valid option.")
        print("")
            

def take_two_inputs():
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))
    return a, b


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


def even_odd(a):
    if a % 2 == 0:
        return f"{a} is even"
    else:
        return f"{a} is odd"


def calculate_percentage(a, b):
    if b == 0:
        return "Division by zero undefined!"
    else:
        return 100 * (a / b)


if __name__ == "__main__":
    main()
