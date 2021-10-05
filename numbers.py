# a program that inputs 5 numbers from the user and finds the sum
# and average

print("Input numbers to calculate their sum and average: Input 0 to exit.")

count = 0
sum = 0.0
number = 1

while number !=0:
    number = int(input(""))
    sum = sum + number
    count +=1

if count == 0:
    print("Input some numbers")
else:
    print("sum of the above numbers is: ", sum, "and avearage is", sum / (count-1))
