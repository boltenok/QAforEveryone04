"""
6.1 Write a program/function that prints list entities one by one. As an input use a list.
    e.g. print_entities(["a", "b", "c"]) should return:
        "a"
        "b"
        "c"
"""


def print_entities(list1):
    for item in list1:
        print(item)


print_entities(["a", "b", "c"])

"""
6.2 Write a program/function that converts strings into tuples.
    e.g. convert("abide") should return tuple like:
        ("a", "b", "i", "d", "e") 
"""


def convert(var):
    new_list = []
    for each in var:
        new_list.append(each)
    return tuple(new_list)


print(convert("abide"))

"""
6.3 Write a program/function that removes duplicates and returns only unique values as a list.
    e.g. remove_dups("abcdadab") should return ["a", "d", "c", "b"].
    Note, order of elements in the list is not important!
"""


def remove_dubs(text):
    return list(set(text))


print(remove_dubs("abcdadab"))

"""
6.4 Write a program/function that collects certain data as parameters and returns a dictionary object.
    e.g. client("John", "Doe", "01/23/1934", "Male", "San Antonio", "TX", "78261")
    should return a dictionary object like:
        {
            "Name": "John",
            "Lastname": "Doe",
            "DOB": "01/23/1934",
            "Sex": "Male",
            "City": "San Antonio",
            "State": "TX",
            "ZipCode": "78261"
        }
"""


def client(name, last_name, dob, sex, city, state, zip_code):
    # list_of_objects = []
    list_item = {
        "Name": name,
        "Lastname": last_name,
        "DOB": dob,
        "Sex": sex,
        "City": city,
        "State": state,
        "ZipCode": zip_code
    }
    # if name not in list_of_objects:
    #     list_of_objects.append(list_item)
    return list_item
