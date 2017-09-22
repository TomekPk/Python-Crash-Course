'''
8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
text of a message that should be printed on the shirt. The function should print
a sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the
function a second time using keyword arguments.
'''

def make_shirt(shirt_size,shirt_message):
    print("You order shirt size: " + str(shirt_size) +" and message on the shirt"
          " will be: " + "'"+ shirt_message + "'.")

# call using positional arguments:
make_shirt(54,"blabla")

#call using keyword arguments:
make_shirt(shirt_message="stop/end",shirt_size=34)