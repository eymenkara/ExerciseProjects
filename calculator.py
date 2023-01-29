logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


def add(n1, n2):
    return n1 + n2


def substract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


end = False
while not end:
    result = 0
    reset = False
    while not reset:
        if result == 0:
            n1 = input("What's the first number? ")
            number1 = float(n1)
        else:
            number1 = result

        print("+\n-\n*\n/")

        operation = input("Pick an operation from above: ")

        n2 = input("What's the second number? ")
        number2 = float(n2)

        if operation == "+":
            result = add(number1, number2)
        elif operation == "-":
            result = substract(number1, number2)
        elif operation == "*":
            result = multiply(number1, number2)
        elif operation == "/":
            result = divide(number1, number2)
        print(f"{number1} {operation} {number2} = {result}")

        q_reset = input(f"Would you like to keep calculating with {result}? Type 'yes' or 'no'. ")
        if q_reset == "no":
            reset = True

    q_end = input("Would you like to quit? Type 'yes' or 'no'. ")
    if q_end == "yes":
        end = True


