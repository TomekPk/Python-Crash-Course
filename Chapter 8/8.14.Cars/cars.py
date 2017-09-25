'''
8-14. Cars: Write a function that stores information about a car in a dictionary.
The function should always receive a manufacturer and a model name. It
should then accept an arbitrary number of keyword arguments. Call the function
with the required information and two other name-value pairs, such as a
color or an optional feature. Your function should work for a call like this one:
________________________________________________________________________
car = make_car('subaru', 'outback', color='blue', tow_package=True)
________________________________________________________________________
Print the dictionary that’s returned to make sure all the information was
stored correctly.
'''

def make_car(manufacturer, model, **car_info):
    car_description = {}
    car_description["MANUFACTURER"] = manufacturer
    car_description["MODEL"] = model
    for k,v in car_info.items():
        car_description[k] = v
    return car_description

my_car = make_car("Skoda", "Fabia", year = 2001, color = "green",
                  mileage = 210000)
david_car = make_car("Subaru", "Impreza", color = "blue", year = "2010", mileage = 130000)

# function add cars to list_of_cars and print the list
def add_to_list_of_cars(car_profile):
    list_of_cars.append(car_profile)
    print(car_profile, " added to list_of_cars")
list_of_cars = []



# add my car to list_of cars
add_to_list_of_cars(my_car)
print("\nActual list of cars is below:\n" ,list_of_cars)
# add david_car to actual list_of cars
add_to_list_of_cars(david_car)
print("\nActual list of cars is below:\n" ,list_of_cars)