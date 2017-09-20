'''
4-8. Cubes: A number raised to the third power is called a cube. For example,
the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
is, the cube of each integer from 1 through 10), and use a for loop to print out
the value of each cube.
'''


numbers_list=list(range(1,11))
print(numbers_list)

for cube in numbers_list:
    print(cube**3)

# with append():
print("\nSolution with append (): ")
cube_numbers= []
numbers=list(range(1,11))

for cube in numbers:
    cube_numbers.append(cube**3)

for i in cube_numbers:
    print(i)