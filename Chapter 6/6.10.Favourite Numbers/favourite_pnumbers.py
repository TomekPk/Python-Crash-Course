'''
6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so
each person can have more than one favorite number. Then print each person’s
name along with their favorite numbers.
'''


fav_numbers = {
    "Adam": [22,32,33],
    "Ewa": [12,99,7],
    "Thomas": [4,7,6,10],
    "David": [23,3],
    "Agata": [33,43],
}


for name,value in fav_numbers.items():
    print(name + ": ", *value, sep="|")     #print value along with name

