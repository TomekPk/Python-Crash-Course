'''
9-13. OrderedDict Rewrite: Start with Exercise 6-4 (page 108), where you
used a standard dictionary to represent a glossary. Rewrite the program using
the OrderedDict class and make sure the order of the output matches the order
in which key-value pairs were added to the dictionary.
'''
from collections import OrderedDict

glossary = OrderedDict() # create an instance of the OrderedDict class

# add glossaries
glossary["approach"] = "podchodzić"
glossary["appropriate"] = "odpowiedni,właściwy"
glossary["envolve"] = "obejmować"
glossary["comprehension"] = "zrozumienie"
glossary["particular"] = "konkretny"
glossary["immutable"] = "niezmienny"

# add few more words
glossary["nothing"] = "nic"
glossary["sun"]= "słońce"

#show glossary
for k,v in glossary.items():
    print(k.title() + " -EN to PL- " + v.title())
