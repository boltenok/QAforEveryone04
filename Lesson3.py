# Write a program to return a boolean value as a print statement if one number is greater than another.
# E.g. If X is greater than Y return True otherwise return False

a = int(input("Enter the first number:\n"))
b = int(input("Enter the second number to compare:\n"))

# print("The second number is grater: " + str(a < b))
# if (a > 0) and (b > 0):
#     if a > b:
#         message = f'{a} is greater than {b}'
#     elif b == a:
#         message = "They are equal"
#     else:
#         message = f'{b} is greater than {a}'
#     print(message)
# else:
#     print("Invalid number")

# print(f'The second number is grater: {message}')
# print("The second number is grater: " + str(message))


def compare_two_numbers(a, b):
    if a > b:
        return f'{a} is greater than {b}'
    elif b == a:
        return "They are equal"
    else:
        return f'{b} is greater than {a}'


def validate_two_numbers(a, b):
    if (a > 0) and (b > 0):
        return compare_two_numbers(a, b)
    else:
        return "Invalid number"

