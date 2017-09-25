'''
8-10. Great Magicians: Start with a copy of your program from Exercise 8-9.
Write a function called make_great() that modifies the list of magicians by adding
the phrase the Great to each magician’s name. Call show_magicians() to
see that the list has actually been modified.
'''



def show_magicians(name):
    for i in name:
        print(i)


def make_great(name):
    i = 0
    while i < (len(name)):
        name[i] = "Great " + name[i].title()
        #print(name[i])
        i = i + 1

magician_list = ["magic Adam","Magic John","memo Robertos"]


print("\nSTEP 1: show magicians ")
show_magicians(magician_list)
print("\nSTEP 2: make great ")
make_great(magician_list)
print("\nSTEP 3: check magicians updated list ")
show_magicians(magician_list)


