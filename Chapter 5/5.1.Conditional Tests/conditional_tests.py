'''
5-1. Conditional Tests: Write a series of conditional tests. Print a statement
describing each test and your prediction for the results of each test. Your code
should look something like this:
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
• Look closely at your results, and make sure you understand why each line
evaluates to True or False.
• Create at least 10 tests. Have at least 5 tests evaluate to True and another
5 tests evaluate to False.
'''
bike = "Accent"
print("bike == 'accent' False")
print(bike == "accent")


color = "yellow"
print("\ncolor == Yellow False")
print(color == "Yellow")

color = "yellow"
print("\ncolor == yellow True")
print(color == "yellow")


# True results
print("\nTrue tests: ")
# 1
number = 1
print(number == 1)
# 2
my_name = "user555"
print(my_name == "user555")
# 3
car = "Ferrari"
print(car.lower() == "ferrari")
# 4
age_1 = 20
age_2 = 31
print(age_1 != age_2)
# 5
print(age_1 >=18 and age_2 >=18)


#False results
print("\nFalse tests: ")
# 1
car = "Ferrari"
print(car.upper() == "ferrari")
# 2
price = 20.00
quantity = 2
print(price == 20 and quantity > 5)
# 3
something = True
print(not something)
# 4
dog = True
cat = True
print(dog is not cat)
# 5
love_programming = True
skill_level = 1
if love_programming == True and skill_level >1:
    print(skill_level >2)

