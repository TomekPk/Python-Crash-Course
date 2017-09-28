'''
10-1. Learning Python: Open a blank file in your text editor and write a few
lines summarizing what you’ve learned about Python so far. Start each line
with the phrase In Python you can.... Save the file as learning_python.txt in the
same directory as your exercises from this chapter. Write a program that reads
the file and prints what you wrote three times. Print the contents once by reading
in the entire file, once by looping over the file object, and once by storing
the lines in a list and then working with them outside the with block.
'''

my_text = "learning_python.txt"

############################################
# print by reading entire file
'''
with open(my_text) as text_object:
    content = text_object.read()
    print(content)
    print(content)
    print(content)
'''
############################################
# print by looping over the file object
'''
with open(my_text) as text_object:
    for i in text_object:
        print(i.strip())
'''
############################################
# print by by storing the lines in a list and then working with them outside the with block.
with open(my_text) as text_object:
    lines = text_object.readlines()

list_lines = []
for line in lines:
    list_lines.append(line.strip())

# print new list made from lines
print(list_lines)

# print items from list
for item in list_lines:
    print(item)
############################################

