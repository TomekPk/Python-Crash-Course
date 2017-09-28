'''
10-12. Favorite Number Remembered: Combine the two programs from
Exercise 10-11 into one file. If the number is already stored, report the favorite
number to the user. If not, prompt for the user’s favorite number and store it in a
file. Run the program twice to see that it works.
'''

import json


file_name = "favorite_number.json"

try:
    with open(file_name) as file:
        fav_number= json.load(file)
except ValueError:
    print(file_name + " is empty")
    fav_number = input("Hello. What is Your favorite number? ")
    with open(file_name, "w") as file:
        save_fav = json.dump(fav_number,file)
    print("You add your favorite number: " + fav_number + " to " + file_name)

else:
    print("Your favorite number is: " + fav_number)








