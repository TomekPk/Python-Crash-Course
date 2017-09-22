'''
7-2. Restaurant Seating: Write a program that asks the user how many people
are in their dinner group. If the answer is more than eight, print a message saying
they’ll have to wait for a table. Otherwise, report that their table is ready.
'''

Question = input("Hello. Welcome in our restaurant. How many people are in your dinner group? ")


if int(Question) > 8:
    print("\nSorry but you will have to wait for a table.")
else:
    print("\nYours table is ready.")

