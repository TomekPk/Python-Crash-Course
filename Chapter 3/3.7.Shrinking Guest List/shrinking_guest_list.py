'''
3-7. Shrinking Guest List: You just found out that your new dinner table won’t
arrive in time for the dinner, and you have space for only two guests.

• Start with your program from Exercise 3-6. Add a new line that prints a
message saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two
names remain in your list. Each time you pop a name from your list, print
a message to that person letting them know you’re sorry you can’t invite
them to dinner.
• Print a message to each of the two people still on your list, letting them
know they’re still invited.
• Use del to remove the last two names from your list, so you have an empty
list. Print your list to make sure you actually have an empty list at the end
of your program.
'''

last_guest_list= ['Monika', 'Ewelina', 'Adam', 'Tomek', 'Damian', 'Krzysiek']

print("Dear Guests we have a little problem with table, and I can invite only two od You for dinner.")
remove_one= last_guest_list.pop(0)
remove_two= last_guest_list.pop(-1)
remove_three= last_guest_list.pop(-1)
remove_four= last_guest_list.pop(-1)

print("Sorry " + remove_one + ". I invite too much people for dinner. We will met another time. See You soon.")
print("Sorry " + remove_two + ". I invite too much people for dinner. We will met another time. See You soon.")
print("Sorry " + remove_three + ". I invite too much people for dinner. We will met another time. See You soon.")
print("Sorry " + remove_four + ". I invite too much people for dinner. We will met another time. See You soon.")

print("\nMy current list of guests:")
print(last_guest_list ,"\n")

message_before = "Hello "
message_after = ". I want to invite You for a dinner. Be at 5 p.m. See You"

for i in range(len(last_guest_list)):
    print(message_before + last_guest_list[i] + message_after)


# delete items from list
del last_guest_list[0]
del last_guest_list[-1]
#print(last_guest_list)

if last_guest_list:
    print("\nMy guest list is not empty:", last_guest_list)
else:
    print("\nMy guest list is empty now:", last_guest_list)


# From previous exercise:
##############################################################################
'''
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
'''


