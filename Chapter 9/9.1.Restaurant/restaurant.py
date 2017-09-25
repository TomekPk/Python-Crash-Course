'''
9-1. Restaurant: Make a class called Restaurant. The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message indicating
that the restaurant is open.
Make an instance called restaurant from your class. Print the two attributes
individually, and then call both methods.
'''

class Restaurant():
    def __init__(self, restaurant_name, couisine_type):
        self.restaurant_name = restaurant_name
        self.cousine_type = couisine_type

    def open_restaurant(self):
        print(self.restaurant_name.title()+ " is open now.")

restaurant = Restaurant("My new restaurant","fast food")
print(restaurant.restaurant_name.title() + " with couisine type: " + restaurant.cousine_type)
restaurant.open_restaurant()
