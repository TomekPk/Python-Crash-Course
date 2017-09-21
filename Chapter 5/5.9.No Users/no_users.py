'''
5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is
not empty.
• If the list is empty, print the message We need to find some users!
• Remove all of the usernames from your list, and make sure the correct
message is printed.
'''

users_list = ["admin","user555","Danny","Bobby","girl007","Trezor"]

# Testing not empty list:
print("\nTesting user list is not empty list:")

if users_list:
    print("List is not empty")
else:
    print("list is empty")
print(users_list)

# Deleted usernames (exclusive admin) from the list and testing is it empty list now:

print("\nDeleted usernames (exclusive admin) from the list and testing is it empty list now:")

del users_list[2:]  # delete users from the list

if users_list:
    print("List is not empty: ", users_list)
    for user in users_list: #write greetings for admin
        if user == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print("Welcome " + user)
else:
    print("list is empty")


# Deleted everyting from the list and testing is it empty list now:
print("\nDeleted everything from the list and testing is it empty list now:")
del users_list[:]

if users_list:
    print("List is not empty", users_list)
    for user in users_list:     #write greetings for admin
        if user == "admin":
            print("Hello admin, would you like to see a status report?")
else:
    print("list is empty ", users_list)

