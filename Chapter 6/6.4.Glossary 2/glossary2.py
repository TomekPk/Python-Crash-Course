'''
6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
up the code from Exercise 6-3 (page 102) by replacing your series of print
statements with a loop that runs through the dictionary’s keys and values.
When you’re sure that your loop works, add five more Python terms to your
glossary. When you run your program again, these new words and meanings
should automatically be included in the output.
'''

glossary = {
    "approach": "podchodzić",
    "appropriate": "odpowiedni,właściwy",
    "envolve": "obejmować",
    "comprehension": "zrozumienie",
    "particular": "konkretny",
    "immutable": "niezmienny",
}
# add new words
glossary["nothing"] = "nic"
glossary["sun"]= "słońce"

# Sorted glossary by keys
for key in sorted(glossary.keys()):
    print(key +": "+ glossary[key])
