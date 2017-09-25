'''
9-7. Admin: An administrator is a special kind of user. Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 (page 166)
or Exercise 9-5 (page 171). Add an attribute, privileges, that stores a list
of strings like "can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrator’s set of
privileges. Create an instance of Admin, and call your method.
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

class Admin(User):
    def __init__(self, first_name, last_name, age, sex):
        super().__init__(first_name, last_name, age, sex)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        for i in self.privileges:
            print("\t- " + i)


# create admin user
admin_thomas = Admin("Thomas","Benert", 31, "male")
admin_thomas.describe_user()
admin_thomas.show_privileges()