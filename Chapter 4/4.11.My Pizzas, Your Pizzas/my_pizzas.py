'''
4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
(page 60). Make a copy of the list of pizzas, and call it friend_pizzas.
Then, do the following:
1) • Add a new pizza to the original list.
2) • Add a different pizza to the list friend_pizzas.
3) • Prove that you have two separate lists. Print the message, My favorite
pizzas are:, and then use a for loop to print the first list. Print the message,
My friend’s favorite pizzas are:, and then use a for loop to print the second
list. Make sure each new pizza is stored in the appropriate list.
'''
pizza_list = ["salami","village","chicken","chilly"]
friend_pizzas = pizza_list[:]
print(friend_pizzas)

# 1)
pizza_list.append("beacon")

# 2)
friend_pizzas.append("tomatoes")

# 3)
print("\nMy friend's favorite pizzas are: ")
for pizza in pizza_list:
    print(pizza)

print("\nMy friend's favorite pizzas are: ")
for pizza in friend_pizzas:
    print(pizza)
