'''
7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
the sandwich 'pastrami' appears in the list at least three times. Add code
near the beginning of your program to print a message saying the deli has
run out of pastrami, and then use a while loop to remove all occurrences of
'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
in finished_sandwiches.
'''

sandwich_orders = ["pastrami","hamburger","vegetarian","pastrami","with tomatoes and salami","pastrami"]

print("\nInformation! Today Deli has run out of pastrami.")
x=1
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
    print(str(x) + ".pastrami is removed")
    x = x + 1


print("\nActual sandwich orders: ")
for i in sandwich_orders:
    print("\t-" , i)






