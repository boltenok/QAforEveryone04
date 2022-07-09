"""
5.1 Write a function to compare 2 numbers.
    E.g. compare(2, 3) should return False otherwise should return True.
"""


def compare_numbers(a, b):
    return a > b


# print(compare_numbers(2, 3))
# print(compare_numbers(3, 2))

"""
5.2 Modify the previous function to compare only positive numbers.
    In case of negative numbers it will return a print statement like: "Can compare only positive numbers!".
"""


def compare_numbers_2(a, b):
    if a > 0 and b > 0:
        return a > b
    else:
        return f'{a} and {b} are out of range. Can compare only positive numbers!'
# print(compare_numbers_2(-1, 2))
# print(compare_numbers_2(1, 2))
# print(compare_numbers_2(2, 3))


"""
5.3 Write a function to sum 2 numbers.
    E.g. add(4, 5) should return 9 as a result.
"""
def sum_up_numbers(a, b):
    return a + b

# print(sum_up_numbers(4, 5))

"""
5.4 Write a function to subtract 2 numbers.
    E.g. sub(4, 2) should return 2 as a result.
"""
def sub_numbers(a, b):
    return a - b

# print(sub_numbers(4, 2))
"""
5.5 Write a function that returns a type of input.
    E.g. give_a_type("test") should return a print statement like: "string".
"""
def give_a_type(inp):
    if isinstance(inp, str):
        return "String"
    elif isinstance(inp, int):
        return "Integer"
    elif isinstance(inp, float):
        return "Float"
    elif isinstance(inp, complex):
        return "Complex number"
    elif isinstance(inp, list):
        return "List"
    elif isinstance(inp, tuple):
        return "Tuple"
    elif isinstance(inp,range):
        return "Range of data"
    elif isinstance(inp, dict):
        return "Dictionary"
    elif isinstance(inp, bool):
        return "Boolean"
    elif isinstance(inp, bytes):
        return "Binary"
    else:
        return "None"


"""
5.6 Write a function that prints input vertically.
    E.g. print_vertical("test me please") should return:
        t
        e
        s
        t

        m
        e

        p
        l
        e
        a
        s
        e
"""

def print_vertical(string):
    for letter in string:
        print(letter)

# print_vertical("test me please, lol")

"""
5.7 Write a function that concatenates 2 strings.
    E.g. concat("abc" , "123") should return a print statement like: "adc123".
"""

def concat(inp1, inp2):
    return str(inp1) + str(inp2)

print(concat("abc" , 123))
