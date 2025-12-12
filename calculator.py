def calculate():
    operators = {"+": lambda x, y: x + y,
                    "-": lambda x, y: x - y,
                    "*": lambda x, y: x * y,
                    "/": lambda x, y: x / y,
                }
    while True:
    
        first_number = input("Enter first number (enter q to quit): ")
        if first_number.lower() == 'q':
            break
        try:
            first_number = float(first_number)
        except ValueError:
            print("Enter a valid number!")
            continue
        operator = input("Enter an operator: (enter q to quit): ")
        if operator.lower() == 'q':
            break
        elif operator not in operators:
            print("Print a valid operator!")
            continue
        second_number = input("Enter second number (enter q to quit): ")
        if second_number.lower() == 'q':
            break
        try:
            second_number = float(second_number)
        except ValueError:
            print("Enter a valid number!")
            continue
        result = operators[operator](first_number, second_number)
        print("result:", result)
        keep_going = input("Do you wish to continue? (yes/no): ")
        if keep_going.lower() == 'yes':
            continue
        elif keep_going.lower() == 'no':
            break
calculate()
        
    