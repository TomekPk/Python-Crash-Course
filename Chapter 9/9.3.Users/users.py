'''
9-3. Users: Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.
Create several instances representing different users, and call both methods
for each user.
'''


class User():
    def __init__(self, first_name, last_name, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
    def describe_user(self):
        print("\nUser info: " + self.first_name + ", " + self.last_name + ", " + str(self.age) + ", " + self.sex)

    def greet_users(self):
        print("Hello " + self.first_name + " " + self.last_name + ". Your age is " +
              str(self.age) + " and you are " + self.sex + ".")

user_one = User("David","Berks",26,"male")
user_one.describe_user()
user_one.greet_users()

user_two = User("Robert", "Fairy", 33, "male")
user_two.describe_user()
user_two.greet_users()

user_three = User("Eva", "Benksy", 18, "female")
user_three.describe_user()
user_three.greet_users()