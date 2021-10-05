#a program that computes the square of a number

def main():
    num = int(input("Enter a number: "))
    result = num ** 2
    print("The square of", num, "is", result)


main()


#a program that computes square root of a number using the math module

import math

def sqareroot():
    number = int(input("Enter a number: "))
    ans = math.sqrt(number)
    print("The square root of", number, "is", ans)

sqareroot()
