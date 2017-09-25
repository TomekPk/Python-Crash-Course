'''
9-8. Privileges: Write a separate Privileges class. The class should have one
attribute, privileges, that stores a list of strings as described in Exercise 9-7.
Move the show_privileges() method to this class. Make a Privileges instance
as an attribute in the Admin class. Create a new instance of Admin and use your
method to show its privileges.
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
        self.privileges = Privileges()


class Privileges():
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        for i in self.privileges:
            print("\t- " + i)



# create admin user
admin_thomas = Admin("Thomas","Benert", 31, "male")
admin_thomas.describe_user()
admin_thomas.privileges.show_privileges()