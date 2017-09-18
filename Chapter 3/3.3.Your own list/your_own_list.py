'''
3-3. Your Own List: Think of your favorite mode of transportation, such as a
motorcycle or a car, and make a list that stores several examples. Use your list
to print a series of statements about these items, such as “I would like to own a
Honda motorcycle.”
'''

names = ["Adam","Arek","Darek"]
fav_transportation = ["bike","car","motorcycle"]

message_before = "My friend "
message_after = " love to ride a "
print(message_before + names[0] + message_after + fav_transportation[1])
print(message_before + names[1] + message_after + fav_transportation[2])
print(message_before + names[2] + message_after + fav_transportation[0])
