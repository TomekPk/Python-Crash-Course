'''
8-12. Sandwiches: Write a function that accepts a list of items a person wants
on a sandwich. The function should have one parameter that collects as many
items as the function call provides, and it should print a summary of the sandwich
that is being ordered. Call the function three times, using a different number
of arguments each time.
'''



def make_sandwich(*items):
    print("\nSummary items on your sandwich: ")
    for i in items:
        print("\t- " + i)

make_sandwich("bread","tomatoe","beef","onion")

make_sandwich("bread","buter","ketchup","garlic","cucumber")

make_sandwich("bread","butter","tomato")


