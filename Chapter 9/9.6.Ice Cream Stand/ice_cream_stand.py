'''
9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand that inherits from the Restaurant class you wrote
in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either version of
the class will work; just pick the one you like better. Add an attribute called
flavors that stores a list of ice cream flavors. Write a method that displays
these flavors. Create an instance of IceCreamStand, and call this method.
'''

class Restaurant():
    def __init__(self, restaurant_name, couisine_type):
        self.restaurant_name = restaurant_name
        self.couisine_type = couisine_type

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is open now.")

class IceCreamStand(Restaurant):
    def __init__(self, ice_name, couisine_type):
        super().__init__(ice_name, couisine_type) #super() make connection child and parent class
        self.flavors = ["apple", "banana", "chocolate"]

    def display_flavors(self):
        flavors = self.flavors
        print(flavors)

#create an instance of IceCreamStand, and call display_flavours() method
ice_cream_stand_1 = IceCreamStand("Ice Cream from Thomas", "ice cream")
ice_cream_stand_1.open_restaurant()
ice_cream_stand_1.display_flavors()
