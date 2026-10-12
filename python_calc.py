def main():
    print("----Welcome to Python Calculator----\n")
    # Loop to handle multiple calculations before exiting
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
                # To handle division by zero
                if b == 0:
                    print("Division by zero is undefined!")
                else:
                    print(f"{a} / {b} = {division(a, b)}")

            case 5:
                a = int(input("Enter a number: "))
                print(even_odd(a))

            case 6:
                a, b = take_two_inputs()
                # To handle division by zero
                if b == 0:
                    print("Division by zero is undefined!")
                else:
                    print(f"Percentage of {a} from {b} = {calculate_percentage(a, b)}%")

            case 7:
                print("Exiting Calculator...")
                # Loop exits only for this case
                break;

            # Print error message for invalid selection
            case _:
                print("Invalid Choice! Select a valid option.")
        print("")
            

# Function to take two inputs
def take_two_inputs():
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))
    return a, b


# Function to do addition
def addition(a, b):
    return a + b


# Function to do subtraction
def subtraction(a, b):
    return a - b


# Function to do multiplication
def multiplication(a, b):
    return a * b


# Function to do division
def division(a, b):
    return a / b


# Function to check if number is even or odd
def even_odd(a):
    if a % 2 == 0:
        return f"{a} is even"
    else:
        return f"{a} is odd"


# Function to find percentage
def calculate_percentage(a, b):
    return 100 * (a / b)


if __name__ == "__main__":
    main()
