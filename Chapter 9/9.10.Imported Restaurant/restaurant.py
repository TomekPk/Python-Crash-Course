'''
Class that can be used to represent a Restaurant
'''

class Restaurant():
    def __init__(self, restaurant_name, couisine_type):
        self.restaurant_name = restaurant_name
        self.cousine_type = couisine_type

    def open_restaurant(self):
        print(self.restaurant_name.title() + " with couisine type: " + self.cousine_type + " is open now.")


