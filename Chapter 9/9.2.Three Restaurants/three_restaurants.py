'''
9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
different instances from the class, and call describe_restaurant() for each
instance.
'''

class Restaurant():
    def __init__(self, restaurant_name, couisine_type):
        self.restaurant_name = restaurant_name
        self.cousine_type = couisine_type

    def open_restaurant(self):
        print(self.restaurant_name.title()+ " is open now.")

    def describe_restaurant(self):
        print("\n" + self.restaurant_name.title() + " with couisine type: " + self.cousine_type + ".")

# Create new objects (instances) of Restaurant class
restaurant_one = Restaurant("My new restaurant", "fast food")
restaurant_two = Restaurant("David restaurant", "chinesse food")
restaurant_three = Restaurant("Robert restaurant", "chicken and fry")

# call 2 methods describe_restaurant and open_restaurant for each of instances
restaurant_one.describe_restaurant()
restaurant_one.open_restaurant()

restaurant_two.describe_restaurant()
restaurant_two.open_restaurant()

restaurant_three.describe_restaurant()
restaurant_three.open_restaurant()


