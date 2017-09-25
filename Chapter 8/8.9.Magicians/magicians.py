'''
8-9. Magicians: Make a list of magician’s names. Pass the list to a function
called show_magicians(), which prints the name of each magician in the list.
'''



def show_magicians(name):
    for i in name:
        print(i)

magician_list = ["magicAdam","MagicJohn","memoRobertos"]
show_magicians(magician_list)