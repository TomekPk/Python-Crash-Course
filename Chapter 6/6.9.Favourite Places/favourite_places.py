'''
6-9. Favorite Places: Make a dictionary called favorite_places. Think of three
names to use as keys in the dictionary, and store one to three favorite places
for each person. To make this exercise a bit more interesting, ask some friends
to name a few of their favorite places. Loop through the dictionary, and print
each person’s name and their favorite places.
'''


favourite_places = {
    "Thomas" : ["USA","Netherland"],
    "David" : ["Bahamas","Germany"],
    "Adam" : ["Krakow","Warsaw"],
}

#add new friends favourite places:
favourite_places["Monica"] = ["home","village"]

for name,place in favourite_places.items():
    print(name + ": ")
    for item in place:
        print("\t"+item)

list = ["a","b"]
for i in list:
    print()