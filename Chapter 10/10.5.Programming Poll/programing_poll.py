'''
10-5. Programming Poll: Write a while loop that asks people why they like
programming. Each time someone enters a reason, add their reason to a file
that stores all the responses.
'''

my_text = "poll.txt"

q = True
while q:
    name_message = "Hello. Why do You like programming? \n"
    name_message += "For end press q: \n"
    user_name = input(name_message)
    if user_name.lower() == "q":
        q = False
    else:
        with open(my_text, "a") as guest_object:
            guest_object.write("Answer: " + user_name.title() + "\n")




