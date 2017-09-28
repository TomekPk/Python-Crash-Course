'''
10-2. Learning C: You can use the replace() method to replace any word in a
string with a different word. Here’s a quick example showing how to replace
'dog' with 'cat' in a sentence:
message = "I really like dogs."
message.replace('dog', 'cat')
'I really like cats.'
Read in each line from the file you just created, learning_python.txt, and
replace the word Python with the name of another language, such as C. Print
each modified line to the screen.
'''
my_text = "learning_python.txt"

# print by reading entire file and replace Python string to C string
with open(my_text) as text_object:
    lines = text_object.readlines()

for line in lines:
    print(line.replace("Python","C").strip())



