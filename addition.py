# A program that finds the sum of numbers between 1 and 1000
#using for loop

def addition():
    sum = 0
    for i in range(1, 1000 + 1):
        sum = sum + i
    print("The sum of numbers is: ", sum)

addition()