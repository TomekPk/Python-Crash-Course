'''
9-4. Number Served: Start with your program from Exercise 9-1 (page 166).
Add an attribute called number_served with a default value of 0. Create an
instance called restaurant from this class. Print the number of customers the
restaurant has served, and then change this value and print it again.
Add a method called set_number_served() that lets you set the number
of customers that have been served. Call this method with a new number and
print the value again.
Add a method called increment_number_served() that lets you increment
the number of customers who’ve been served. Call this method with any number
you like that could represent how many customers were served in, say, a
day of business.
'''

class Restaurant():
    def __init__(self, restaurant_name, couisine_type):
        self.restaurant_name = restaurant_name
        self.cousine_type = couisine_type
        self.number_served = 15

    def set_number_served(self,new_served):
        if new_served >= self.number_served:
            self.number_served = new_served
            set_done = "New value of todays customers: " + str(self.number_served)
            return set_done
        else:
            message_too_low = "Please pass more than " + str(self.number_served)
            return message_too_low


    def open_restaurant(self):
        #print(self.restaurant_name.title()+ " is open now.")
        restaurant_description = "Welcome to: " + self.restaurant_name.title() + " with "\
                                 + self.cousine_type + ". We served "\
                                 + str(self.number_served) + " customers today."
        return restaurant_description

restaurant = Restaurant("My new restaurant","fast food")
print(restaurant.open_restaurant())
new_number_served = restaurant.set_number_served(14)
print(new_number_served)
