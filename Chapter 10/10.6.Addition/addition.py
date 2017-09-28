'''
10-6. Addition: One common problem when prompting for numerical input
occurs when people provide text instead of numbers. When you try to convert
the input to an int, you’ll get a TypeError. Write a program that prompts for
two numbers. Add them together and print the result. Catch the TypeError if
either input value is not a number, and print a friendly error message. Test your
program by entering two numbers and then by entering some text instead of a
number.
'''

message_1 = input("Number 1. Enter number: \n")
try:
    answer1 = int(message_1)
except ValueError:
    print("Please enter number only!")
    message_1 = input("Number 1. Enter number: \n")


message_2 = input("Number 2. Enter second number: \n")
try:
    answer2 = int(message_2)
except ValueError:
    print("Please enter number only!")
    message_2 = input("Number 2. Enter number: \n")


message = int(message_1) + int(message_2)
print("Number 1 is: " + str(message_1))
print("Number 2 is: " + str(message_2))
print("Sum of Number 1 and Number 2 is: " + str(message))
