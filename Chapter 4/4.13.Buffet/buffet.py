'''
4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five
simple foods, and store them in a tuple.
1) • Use a for loop to print each food the restaurant offers.
2) • Try to modify one of the items, and make sure that Python rejects the
change.
3) • The restaurant changes its menu, replacing two of the items with different
foods. Add a block of code that rewrites the tuple, and then use a for
loop to print each of the items on the revised menu.
'''


restaurant_food = ("schabowy","zupa ogórkowa","czerwona kapusta","naleśniki z serem","ciastko czekoladowe")

print(restaurant_food)

# 1)
print("\nRestaurant offer:")
for i in restaurant_food:
    print("- " +i)

# 2)
#restaurant_food.remove(1) # Reject

# 3)
print(str(len(restaurant_food))+" foods:", restaurant_food)

restaurant_food = ("a food","b food","c food","d food","e food","f food")
print(len(restaurant_food)," foods after change:", restaurant_food)

print("\nNEW MENU:")
for i in restaurant_food:
    print("- " +i)

