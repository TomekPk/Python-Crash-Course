'''
10-13. Verify User: The final listing for remember_me.py assumes either that the
user has already entered their username or that the program is running for the
first time. We should modify it in case the current user is not the person who
last used the program.
Before printing a welcome back message in greet_user(), ask the user if
this is the correct username. If it’s not, call get_new_username() to get the correct
username.
'''

import json


import json

def get_stored_username():
    file_name = "username.json"
    try:
        with open(file_name) as file:
            username = json.load(file)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input("What is your name? ")
    file_name = "username.json"
    with open(file_name, "w") as file:
        json.dump(username, file)
    return username



def greet_user():
    username = get_stored_username()
    if username:
        print("Welcome back, " + username)
        check_msg = input("Is it Your name " + username + "?\nWrite YES or NO: ")
        while True:
            if check_msg.lower() == "yes":
                print("We'll remember you when you come back, " + username +"!")
                break
            elif check_msg.lower() == "no":
                username = get_new_username()
                print("We'll remember you when you come back, " + username + "!")
                break
            else:
                check_msg = input("Please enter yes/no only: ")
                continue
    else:
        print("Hello new user. ")
        username = get_new_username()
        print("We'll remember you when you come back, " + username +"!")




greet_user()





