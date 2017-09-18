'''
3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just
printing each person’s name, print a message to them. The text of each message
should be the same, but each message should be personalized with the
person’s name.
'''

names = ["Adam","Arek","Darek"]

message_before = "Hi "
message_after = ". How are You today?"
print(message_before + names[0] + message_after)
print(message_before + names[1] + message_after)
print(message_before + names[2] + message_after)
