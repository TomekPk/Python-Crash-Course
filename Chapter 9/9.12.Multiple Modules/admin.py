from users import User
from user_privileges import Privileges


# CHILD class inherit from User class
class Admin(User):
    def __init__(self, first_name, last_name, age, sex):
        super().__init__(first_name, last_name, age, sex)
        '''Make a Privileges instance
            as an attribute in the Admin class:'''
        print("You create Admin account")
        self.privileges = Privileges()
