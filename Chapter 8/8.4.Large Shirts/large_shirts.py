'''
8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python. Make a large shirt and a
medium shirt with the default message, and a shirt of any size with a different
message.
'''

def make_shirt(shirt_message="I love Python", shirt_size="large"):
    print("You order shirt size: " + str(shirt_size) +" and message on the shirt"
          " will be: " + "'"+ shirt_message + "'.")

# call using positional arguments:
make_shirt("I love programming", "XXL")

#call using keyword arguments:
make_shirt(shirt_size="large")
make_shirt(shirt_size="medium")