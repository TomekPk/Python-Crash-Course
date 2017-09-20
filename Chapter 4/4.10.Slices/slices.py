'''
4-10. Slices: Using one of the programs you wrote in this chapter, add several
lines to the end of the program that do the following:
1)• Print the message, The first three items in the list are:. Then use a slice to
print the first three items from that program’s list.
2)• Print the message, Three items from the middle of the list are:. Use a slice
to print three items from the middle of the list.
3)• Print the message, The last three items in the list are:. Use a slice to print
the last three items in the list.
'''

cube_list = [value**3 for value in range(1,11)]
print(cube_list)

print("\nMy list: ")
my_list = [value*15 for value in range(1,15)]
print(my_list)

# 1)
print("\n1)")
print("The first three items in the cube_list are:", cube_list[:3])

# 2)
print("\n1)")
print("Three items from the middle in the cube_list are:", cube_list[3:6])

# 3)
print("\n1)")
print("Last three items in the cube_list are:", cube_list[-3:])