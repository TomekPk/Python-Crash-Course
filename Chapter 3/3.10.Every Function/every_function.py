'''
3-9. Dinner Guests: Working with one of the programs from Exercises 3-4
through 3-7 (page 46), use len() to print a message indicating the number
of people you are inviting to dinner.

len(guest_list)

3-10. Every Function: Think of something you could store in a list. For example,
you could make a list of mountains, rivers, countries, cities, languages, or anything
else you’d like. Write a program that creates a list containing these items
and then uses each function introduced in this chapter at least once.
'''


bicycle_list= ["Cube",
               "Specialized",
               "haibike",
               "Accent",
               "Giant"
               ]
print("\n1)Print list bicycle_list")
print(bicycle_list)

print("\n2)Print haibike capitalized:")
print(bicycle_list[2].title())

print("\n3)Remove haibike item from list and put at the end of list but capitalized this time")

popped_bicycle = bicycle_list.pop(2) #remove 3 item from list
print(bicycle_list)
print("I removed: ",popped_bicycle)


print("\n4)Add Haibike capitalized at the end of the list")
bicycle_list.append("Haibike")
print(bicycle_list)

print("\n5)Remove Accent from the list and send information it was removed")
removed_bike = "Accent"
bicycle_list.remove(removed_bike)
print("I removed: ", removed_bike)
print(bicycle_list)

print("\n6)Insert new bike Merida after Specialized")
new_bike = "Merida"
bicycle_list.insert(2,new_bike)
print(bicycle_list)

print("\n7)Sort list alphabetical")
bicycle_list.sort()
print(bicycle_list)

print("\n8)Sort list reverse")
bicycle_list.sort(reverse=True)
print(bicycle_list)

print("\n9)Delete Giant from the list")
del bicycle_list[3]
print(bicycle_list)

print("\n10)Remove Merida from the list")
bicycle_list.remove("Merida")
print(bicycle_list)


