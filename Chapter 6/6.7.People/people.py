'''
6-7. People: Start with the program you wrote for Exercise 6-1 (page 102).
Make two new dictionaries representing different people, and store all three
dictionaries in a list called people. Loop through your list of people. As you
loop through the list, print everything you know about each person.
'''

person1 = {
    "first_name":   "Ewa",
    "last_name":    "Bunny",
    "age:":         "32",
    "city":         "Krakow"
}

person2 = {
    "first_name":   "Adam",
    "last_name":    "Autorski",
    "age:":         "30",
    "city":         "Warsaw"
    }

person3 = {
    "first_name":   "John",
    "last_name":    "Kowalski",
    "age:":         "33",
    "city":         "Bialystok"
    }

people= [person1,person2,person3]

# LOOPING
for person in people:
    print("\n")
    for key,value in person.items():
        print(key.title()+ ": "+ value.upper())
    if person["first_name"] == "John":
        print("John moved last time to Warsaw.")    # John moved last time.
