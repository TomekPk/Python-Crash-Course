'''
9-14. Dice: The module random contains functions that generate random numbers
in a variety of ways. The function randint() returns an integer in the
range you provide. The following code returns a number between 1 and 6:
from random import randint
x = randint(1, 6)
Make a class Die with one attribute called sides, which has a default
value of 6. Write a method called roll_die() that prints a random number
between 1 and the number of sides the die has. Make a 6-sided die and roll
it 10 times.
Make a 10-sided die and a 20-sided die. Roll each die 10 times.
'''

from random import randint


class Die():
    def __init__(self,sides):
        self.sides = sides


    def roll_die(self, x_times):
        n = 1
        while n <= x_times:
            x = randint(1, self.sides)
            print(str(n) + ". roll: " + "\t" +str(x))
            n += 1

print("\nFirst Dice:")
# create a Die(how many sides it have)
my_dice = Die(10)

# roll Die(how many times)
my_dice.roll_die(10)

print("\nSecond Dice:")
# create 20 sides Die
my_dice2 = Die(20)

# roll 20 sides Die 20 times
my_dice2.roll_die(20)

