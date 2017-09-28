'''
10-3. Guest: Write a program that prompts the user for their name. When they
respond, write their name to a file called guest.txt.
'''
my_text = "guest.txt"

name_message = input("Hello. Please enter Your name below: \n")


class User():
    def __init__(self,name_message):
        self.name_message = name_message

    def add_user_to_txt(self):
        with open(my_text, "a") as guest_list:
            guest_list.write(self.name_message + "\n")

    def clear_guest_list(self):
        with open(my_text, "w"):
            pass

user1 = User(name_message)
user1.add_user_to_txt()
user1.clear_guest_list()

