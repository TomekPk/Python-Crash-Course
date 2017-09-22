'''
6-12. Extensions: We’re now working with examples that are complex enough
that they can be extended in any number of ways. Use one of the example programs
from this chapter, and extend it by adding new keys and values, changing
the context of the program or improving the formatting of the output.
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
               "fact:": ["1.I was born there","2.Something more"],},

}
cities["London"] = {"country": "UK",
                    "population in billions:": 8.787,
                    "fact": "Great Fire of London in 1666",
                    }

for name,value in cities.items():
    print("\n" + name.upper())    #print value along with name
    for a,b in value.items():
        #print(type(b))
        show = a + ": " + str(value[a])
        print(show)




        #print("\t" + a + ": " + str(b))
'''
listaaa = ["a","b"]

if type(listaaa) is list:
    for i in listaaa:
        print(i)
'''
