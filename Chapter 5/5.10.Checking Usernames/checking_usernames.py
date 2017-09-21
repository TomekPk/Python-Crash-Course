'''
5-10. Checking Usernames: Do the following to create a program that simulates
how websites ensure that everyone has a unique username.
• Make a list of five or more usernames called current_users.
• Make another list of five usernames called new_users. Make sure one or
two of the new usernames are also in the current_users list.
• Loop through the new_users list to see if each new username has already
been used. If it has, print a message that the person will need to enter a
new username. If a username has not been used, print a message saying
that the username is available.
• Make sure your comparison is case insensitive. If 'John' has been used,
'JOHN' should not be accepted.
'''


# create lists:
current_users = ["admin","uSer555","Danny","Bobby","girl007","Trezor"]
new_users = ["tom772", "Bambam","Danny","Trezor","USER555"]



# LIST COMPREHENSION for current_users to make list with lowercase (short way):
current_users_low = [item.lower() for item in current_users]

# make list with lowercase (long way):
current_users_low2 = []
for i in current_users:
    current_users_low2.append(i.lower())



for i in new_users:
    if i.lower() in current_users_low:  # or current_users_low2 for use
        print(i, " is already exist. Please enter a new username")
    else:
        print(i, " that username is available")

