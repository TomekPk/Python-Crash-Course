'''
8-16. Imports: Using a program you wrote that has one function in it, store that
function in a separate file. Import the function into your main program file, and
call the function using each of these approaches:
import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *
'''

import printing_functions
printing_functions.make_my_new_name("Thomas")

from printing_functions import make_my_new_name
make_my_new_name("David")

from printing_functions import make_my_new_name as mnn
mnn("Robert")

import printing_functions as pf
pf.make_my_new_name("Diana")

from printing_functions import *
make_my_new_name("Jack")

make_my_new_name("asd")
