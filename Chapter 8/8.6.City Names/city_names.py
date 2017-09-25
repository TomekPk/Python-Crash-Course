'''
8-6. City Names: Write a function called city_country() that takes in the name
of a city and its country. The function should return a string formatted like this:
"Santiago, Chile"
Call your function with at least three city-country pairs, and print the value
that’s returned.
'''


def city_country(name,country):
    message_city = name + ", " + country
    return message_city.title()

formated_message = city_country("warsaw","poland")
print(formated_message)

adam_city_country = city_country("London","England")
print(adam_city_country)

company = city_country("Brasilia","Brasil")
print(company)

home = city_country("buenos Aires","argentina")
print(home)

