'''
9-5. Login Attempts: Add an attribute called login_attempts to your User
class from Exercise 9-3 (page 166). Write a method called increment_
login_attempts() that increments the value of login_attempts by 1. Write
another method called reset_login_attempts() that resets the value of login_
attempts to 0.
Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts(). Print login_attempts again to
make sure it was reset to 0.
'''


class User():
    def __init__(self, first_name, last_name, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

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
user_three.greet_users


print("\nAdding and resetting login attempts for user: \n" + user_one.first_name + " " + user_one.last_name)
# adding and resetting login attempts for user
print(str(user_one.login_attempts)) # show login_attempts for user_one
user_one.increment_login_attempts() # incrementing login_attempts for user_one
print(str(user_one.login_attempts)) # show login_attempts for user_one
print(str(user_one.login_attempts)) # show login_attempts for user_one
user_one.increment_login_attempts() # incrementing login_attempts for user_one
print(str(user_one.login_attempts)) # show login_attempts for user_one
user_one.reset_login_attempts()     # resetting login_attempts for user_one
print(str(user_one.login_attempts)) # show login_attempts for user_one

