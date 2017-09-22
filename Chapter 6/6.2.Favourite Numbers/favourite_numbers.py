'''
6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
Think of five names, and use them as keys in your dictionary. Think of a favorite
number for each person, and store each as a value in your dictionary. Print
each person’s name and their favorite number. For even more fun, poll a few
friends and get some actual data for your program.
'''

fav_numbers = {
    "Adam":22,
    "Ewa":26,
    "Thomas":30,
    "David":23,
    "Agata":43,
}

for key,value in fav_numbers.items():
    print(key,": ",value)

fav_numbers["Marcin"] = 30  #add new person
fav_numbers["John"]= 40     #add new person

print("\nList with additional people")
for key,value in fav_numbers.items():   #shows actual glossary data
    print(key,": ",value)