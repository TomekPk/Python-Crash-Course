'''
7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5
that do each of the following at least once:
1) • Use a conditional test in the while statement to stop the loop.
2) • Use an active variable to control how long the loop runs.
3) • Use a break statement to exit the loop when the user enters a 'quit' value.
'''

#7.4.
Question = "\nWhat topping do you want add to your pizza?"
Question += "\nPlease write topping or write 'quit' for close: "

#1) • Use a conditional test in the while statement to stop the loop.

while  input(Question) != "quit":

    if input(Question) == "quit":
        print("\nThank you for order. ")
    else:
        print("\t"+ input(Question).title() + " - we will add for you.")

#2) • Use an active variable to control how long the loop runs.
message = ""
while  message != "quit":
    message = input(Question)
    if message == "quit":
        print("\nThank you for order. ")
    else:
        print("\t"+ message.title() + " - we will add for you.")

#3) • Use a break statement to exit the loop when the user enters a 'quit' value.

while True:
    topping = input(Question)
    if topping == "quit":
        break
    else:
        print("\t"+ topping.title() + " - we will add for you.")