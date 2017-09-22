'''
7-3. Multiples of Ten: Ask the user for a number, and then report whether the
number is a multiple of 10 or not.
'''

Question = input("Please give me a number multiple of 10: ")


if int(Question)%10 == 0:
    print(Question + " is multiple of 10.")
else:
    print("\nThis number is not multiple of 10.")

