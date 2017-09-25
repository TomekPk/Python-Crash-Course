'''
8-11. Unchanged Magicians: Start with your work from Exercise 8-10. Call the
function make_great() with a copy of the list of magicians’ names. Because the
original list will be unchanged, return the new list and store it in a separate list.
Call show_magicians() with each list to show that you have one list of the original
names and one list with the Great added to each magician’s name.
'''

def show_magicians(name):
    for i in name:
        print(i)


def make_great(name,second_list):

    while name:
        remove_item = name.pop()
        print("Adding to new list: " + remove_item)
        remove_item = "Great " + remove_item
        second_list.append(remove_item)


magician_list = ["magic Adam","Magic John","memo Robertos"]
new_list = []


print("\nSTEP 1: show magicians list ")
show_magicians(magician_list)
print("\nSTEP 2: make great ")

'''
Below used magician_list[:] because with [:] it is no affecting to oryginal list.
Without copy ->  ...[:] it will do all functions affecting oryginal list.
'''

make_great(magician_list[:], new_list)  # !!! necessarily create empty new_list before run !!!
print("\nSTEP 3: check magicians updated list ")
show_magicians(new_list)
print("\nSTEP 3: check original magicians ")
show_magicians(magician_list)

# TASK:
# Try to add .title(). Make new order for items, like in oryginal magician)list.




