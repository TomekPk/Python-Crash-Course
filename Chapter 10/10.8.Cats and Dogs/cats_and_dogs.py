'''
10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least three
names of cats in the first file and three names of dogs in the second file. Write
a program that tries to read these files and print the contents of the file to the
screen. Wrap your code in a try-except block to catch the FileNotFound error,
and print a friendly message if a file is missing. Move one of the files to a different
location on your system, and make sure the code in the except block
executes properly.
'''


cats_file = "cats.txt"
dogs_file = "dogs.txt"


# create file cats_file
if cats_file == "":
    with open(cats_file, "w") as store_1:
        store_1.close()

# create file dogs_file
if dogs_file != "":
    with open(dogs_file, "w")as store_2:
        store_2.close()

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
        print("\nYou create cat name: " + self.dog_name)

    def store_in_file(self):
        """ add dog name to dogs.txt """
        with open(dogs_file, "a") as store:
            store.writelines(self.dog_name + "\n")
            print("\tYou store " + self.dog_name + " in " + dogs_file)


# create cat:
animal1 = Cat("Maja")
# store cat in a file
animal1.store_in_file()

animal2 = Cat("Johnson")
animal2.store_in_file()

animal3 = Cat("Bety")
animal3.store_in_file()

# create dog
dog1 = Dog("HauHau")
#store dog in a file
dog1.store_in_file()

dog2 = Dog("Bronix")
dog2.store_in_file()

dog3 = Dog("Ron")
dog3.store_in_file()



