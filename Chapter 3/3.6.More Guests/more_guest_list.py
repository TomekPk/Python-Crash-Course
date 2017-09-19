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
message_after = ". I want to invite You for a dinner. Be at 5 p.m. See You"

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

# add 3 more guests ...

print("\n")
guest_list.insert(0, "Monika")
print(message_before + guest_list[0] + message_after)
print("My currently guest list: ", guest_list)


print("\n")
guest_list.insert(2, "Adam")
print(message_before + guest_list[2] + message_after)
print("My currently guest list: ", guest_list)


print("\n")
guest_list.append("Krzysiek")
print(message_before + guest_list[-1] + message_after)
print("My currently guest list: ", guest_list)


# Print guest list using for loop
print("\nAll Guests invited:")
for index in range(len(guest_list)):
    print(guest_list[index])

print("\nInvitations:")
for index in range(len(guest_list)):
    print(message_before+ guest_list[index] + message_after)


