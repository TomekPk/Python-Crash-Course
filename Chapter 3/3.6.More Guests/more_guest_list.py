'''
3-6. More Guests: You just found a bigger dinner table, so now more space is
available. Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or Exercise 3-5. Add a print
statement to the end of your program informing people that you found a
bigger dinner table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list.
'''

guest_list = ["Ewelina","Tomek","Gosia"]


message_before = "Hello "
message_after = ". I want to invite You for a dinner. Will You come at 5 p.m?"

# First invitation
print(message_before + guest_list[0] + message_after)
print(message_before + guest_list[1] + message_after)
print(message_before + guest_list[2] + message_after)

cant_guest_list= guest_list.pop(2)
print("\nUnfortunately "+ cant_guest_list + " will not eat with us.\n" )
print(guest_list)

# New person add to my guest_list
guest_list.append("Damian")
print("My new guest list:")
print(guest_list)

# Confirmation of invitation without Gosia
print("\nMy new invitations: ")
message2_after = " You are still invited for a dinner. If something changed, please call me.n"
print(guest_list[0] + message2_after)
print(guest_list[1] + message2_after)
print(message_before + guest_list[2] + message_after)

# add new guests ...
