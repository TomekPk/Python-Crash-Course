'''
10-4. Guest Book: Write a while loop that prompts users for their name. When
they enter their name, print a greeting to the screen and add a line recording
their visit in a file called guest_book.txt. Make sure each entry appears on a
new line in the file.
'''

my_text = "guest_book.txt"

q = True
while q:
    name_message = "Hello. Please enter Your name below. \n"
    name_message += "For ending press q: \n"
    user_name = input(name_message)
    if user_name.lower() == "q":
        q = False
    else:
        with open(my_text, "a") as guest_object:
            guest_object.write(user_name.title() + "\n")




