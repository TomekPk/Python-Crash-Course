'''
10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop
so the user can continue entering numbers even if they make a mistake and
enter text instead of a number.
'''

print("Enter two numbers and I will add them together.")
print("Enter 'q' to quit.")

message_1 = input("Number 1. Enter number: \n")
x = True
while x:
    if message_1 == "q":
        break
    else:
        try:
            answer1 = int(message_1)
        except ValueError:
            print("Please enter number only!")
            message_1 = input("Number 1. Enter number: \n")
        else:
            x = False

message_2 = input("Number 2. Enter second number: \n")

start = True
while start:
    if message_2 == "q":
        break
    else:
        try:
            answer2 = int(message_2)
        except ValueError:
            print("Please enter number only!")
            message_2 = input("Number 2. Enter number: \n")
        else:
            start = False


try:
    message = int(message_1) + int(message_2)
except ValueError:
    print("You do not pass two numbers!")
else:
    print("Number 1 is: " + str(message_1))
    print("Number 2 is: " + str(message_2))
    print("Sum of Number 1 and Number 2 is: " + str(message))
