'''
6-5. Rivers: Make a dictionary containing three major rivers and the country
each river runs through. One key-value pair might be 'nile': 'egypt'.
• Use a loop to print a sentence about each river, such as The Nile runs
through Egypt.
• Use a loop to print the name of each river included in the dictionary.
• Use a loop to print the name of each country included in the dictionary.
'''

river = {
    "Yukon": "USA",
    "Yangtze": "China",
    "Volga": "Russia",
    "Nile": "Egypt"
}
sentence= " runs trough "

for k,v in river.items():
    print(k + sentence + v)

print("\nRiver names:")
for i in river.keys():
    print(i)

print("\nRiver countries:")
for i in river.values():
    print(i)
