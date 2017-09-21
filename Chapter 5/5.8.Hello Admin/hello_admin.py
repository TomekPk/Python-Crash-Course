'''
5-8. Hello Admin: Make a list of five or more usernames, including the name
'admin'. Imagine you are writing code that will print a greeting to each user
after they log in to a website. Loop through the list, and print a greeting to
each user:
• If the username is 'admin', print a special greeting, such as Hello admin,
would you like to see a status report?
• Otherwise, print a generic greeting, such as Hello Eric, thank you for logging
in again.
'''

# print special greeting for admin and gereric for other users
users_list = ["admin","user555","Danny","Bobby","girl007","Trezor"]


for user in users_list:
    if user == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + user + ". You log in now." )


# admin or generic greetings or no user in list
print("\n")
user_in = "Bobby"   # change user_in

if user_in in users_list:
    if user_in == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + user_in + ". You log in now.")
else:
    print("Sorry. No user " + user_in + " in database.")

