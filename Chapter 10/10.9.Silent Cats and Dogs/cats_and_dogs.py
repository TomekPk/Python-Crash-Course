'''
10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least three
names of cats in the first file and three names of dogs in the second file. Write
a program that tries to read these files and print the contents of the file to the
screen. Wrap your code in a try-except block to catch the FileNotFound error,
and print a friendly message if a file is missing. Move one of the files to a different
location on your system, and make sure the code in the except block
executes properly.
'''

# !!!!!!!!!!!IMPORTANT!!!!!!!!!!!!!
# DELETE ALL TXT FILES BEFORE RUN

cats_file = ""
dogs_file = ""

# create file cats_file
if cats_file != "":
    with open(cats_file+".txt", "w") as store:
        store.close()
else:
    cats_file = input("What filename do you prefer for cat. Please enter your name: \n")
cats_file = str(cats_file) + ".txt"


# create file dogs_file
if dogs_file != "":
    with open(dogs_file+".txt", "w")as store:
        store.close()
else:
    dogs_file = input("What filename do you prefer for dogs. Please enter your name: \n")
dogs_file = str(dogs_file) + ".txt"

class Cat():
    """ create a cat """
    def __init__(self, cat_name):
        self.cat_name = cat_name
        print("You create cat name: " + self.cat_name)

    def store_in_file(self):
        """ add cat name to cats.txt """
        with open(cats_file, "a") as store:
            store.writelines(self.cat_name + "\n")
            print("You store " + self.cat_name + " in " + cats_file)

class Dog():
    def __init__(self, dog_name):
        """ create a dog """
        self.dog_name = dog_name
        print("You create dog name: " + self.dog_name)

    def store_in_file(self):
        """ add dog name to dogs.txt """
        with open(dogs_file, "a") as store:
            store.writelines(self.dog_name + "\n")
            print("\tYou store " + self.dog_name + " in " + dogs_file)


# create cat:
animal1 = Cat("Maja")
animal2 = Cat("Johnson")
animal3 = Cat("Bety")

# store cat in a file
animal1.store_in_file()
animal2.store_in_file()
animal3.store_in_file()

# create dog
dog1 = Dog("HauHau")
dog2 = Dog("Bronix")
dog3 = Dog("Ron")

#store dog in a file
dog1.store_in_file()
dog2.store_in_file()
dog3.store_in_file()



