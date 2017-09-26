'''
9-11. Imported Admin: Start with your work from Exercise 9-8 (page 178).
Store the classes User, Privileges, and Admin in one module. Create a separate
file, make an Admin instance, and call show_privileges() to show that
everything is working correctly.
'''

from users import *
from admin import *


# make an Admin instance:
new_admin = Admin("John","Kowalsky",24,"male")

#call describe_user:
new_admin.describe_user()

# call show_privilages
new_admin.privileges.show_privileges()
