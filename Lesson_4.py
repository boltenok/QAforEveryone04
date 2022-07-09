"""
4.1 Write a program to print result like (use loop):
    H
    e
    l
    l
    o

    P
    y
    t
    h
    o
    n
    !
"""

for letter in "Hello Python!":
    print(letter)

"""
4.2 Write a program that uses loop and prints numbers from 1 to 100 
    but the program should stop if a number is equal to 45.
"""
print("_" * 100)
i = 1
while i <= 100:
    print(i)
    if i == 45:
        break
    i += 1
for x in range(1, 100):
    print(x)
    if x == 45:
        break
"""
4.3 Write a program that prints even numbers from 1 to 20.
"""
print("_" * 100)
a = 1
while a <= 20:
    if (a % 2) == 0:
        print(a)
    a += 1

"""
4.4 Write a program that prints odd numbers from 1 to 30.
"""
print("_" * 100)
b = 1
while b <= 30:
    if (b % 2) != 0:
        print(b)
    b += 1
"""
4.4 Write a program that prints first 10 letters from ABC, the results should be like:
    1 a
    2 b
    3 c
    4 d
    5 e
    6 f
    7 g
    8 h
    9 i
    10 j
"""
abc = "abcdefghij"

for i in range(1, 11):
    print(i, abc[i-1])


"""
4.6 Write a program that prints numbers from 30 to 0 in decreasing order.
"""
print("_" * 100)
for i in range(30, -1, -1):
    print(i)
