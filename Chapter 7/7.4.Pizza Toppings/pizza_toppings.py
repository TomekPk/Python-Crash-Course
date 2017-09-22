'''
7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
pizza toppings until they enter a 'quit' value. As they enter each topping,
print a message saying you’ll add that topping to their pizza.
'''

Question = "\nWhat topping do you want add to your pizza?"
Question += "\nPlease write topping or write 'quit' for close: "

message = ""
while  message != "quit":
    message = input(Question)
    if message == "quit":
        print("\nThank you for order. ")
    else:
        print("\t"+ message.title() + " - we will add for you.")