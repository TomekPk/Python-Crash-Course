'''
10-11. Favorite Number: Write a program that prompts for the user’s favorite
number. Use json.dump() to store this number in a file. Write a separate program
that reads in this value and prints the message, “I know your favorite
number! It’s _____.”
'''
import json

favorite_number = input("Hello. What is Your favorite number? ")
file_name = "favorite_number.json"

def save_fav_number():
    with open(file_name, "w") as file:
        json.dump(favorite_number,file)

def retrieve_fav_number():
    with open(file_name) as file:
        json.load(file)
    print("I know your favourite number! It's: " + favorite_number)

save_fav_number()
retrieve_fav_number()