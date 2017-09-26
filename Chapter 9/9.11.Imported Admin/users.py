'''
Classes that can be used to represent Users
'''

# PARENT class
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

# CHILD class inherit from User class
class Admin(User):
    def __init__(self, first_name, last_name, age, sex):
        super().__init__(first_name, last_name, age, sex)
        '''Make a Privileges instance
            as an attribute in the Admin class:'''
        print("You create Admin account")
        self.privileges = Privileges()


class Privileges():
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        for i in self.privileges:
            print("\t- " + i)


