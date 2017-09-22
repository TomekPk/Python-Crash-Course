'''
6-11. Cities: Make a dictionary called cities. Use the names of three cities as
keys in your dictionary. Create a dictionary of information about each city and
include the country that the city is in, its approximate population, and one fact
about that city. The keys for each city’s dictionary should be something like
country, population, and fact. Print the name of each city and all of the information
you have stored about it.
'''

cities = {
    "Warsaw": {"country": "Poland",
               "population in billions": 8.175,
               "fact:": "I was born there",},
    "New York": {"country": "USA",
               "population in billions": 1.573,
               "fact:": "Wall Street ",},
    "Vilnius": {"country": "Lithuania",
               "population in billions": 0.542,
               "fact:": "I was born there",},

}

for name,value in cities.items():
    print("\n" + name.upper())    #print value along with name
    for a,b in value.items():
        show = a + ": " + str(value[a])
        print(show)
        #print("\t" + a + ": " + str(b))
