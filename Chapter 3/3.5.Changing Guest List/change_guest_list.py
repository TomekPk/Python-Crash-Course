'''
3-5. Changing Guest List: You just heard that one of your guests can’t make the
dinner, so you need to send out a new set of invitations. You’ll have to think of
someone else to invite.
• Start with your program from Exercise 3-4. Add a print statement at the
end of your program stating the name of the guest who can’t make it.
• Modify your list, replacing the name of the guest who can’t make it with
the name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still
in your list.
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
