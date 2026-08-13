def get_integer_input(message):
    while True:
        try:
            value = int(input(message))
            return value
        except ValueError:
            print("Invalid. Please enter a number.")