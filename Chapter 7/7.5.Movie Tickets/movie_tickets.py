'''
7-5. Movie Tickets: A movie theater charges different ticket prices depending on
a person’s age. If a person is under the age of 3, the ticket is free; if they are
between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
$15. Write a loop in which you ask users their age, and then tell them the cost
of their movie ticket.
'''

Question = "\nWelcome in our movie theater. How old are you?"
Question +="\nPlease enter Your age: "

answer = int(input(Question))
if answer < 3:
    print("\nYour admission is for free. Have fun!")
elif answer >= 3 and answer <= 12:
    print("\nTicket for you cost 10$")
else:
    print("\nTicSket for you cost 15$")