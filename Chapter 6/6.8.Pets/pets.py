'''
6-8. Pets: Make several dictionaries, where the name of each dictionary is the
name of a pet. In each dictionary, include the kind of animal and the owner’s
name. Store these dictionaries in a list called pets. Next, loop through your list
and as you do print everything you know about each pet.
'''

Benny = {
    "kind": "dog",
    "owner_name": "maria",
}

Miau = {
    "kind": "cat",
    "owner_name": "david",
}

Kert = {
    "kind": "hamster",
    "owner_name": "ben",
}

pets = [Benny,Miau,Kert]

for pet in pets:
    print("\nPet: ")
    for key,value in pet.items():
        print(key.title() + ": " + value.upper())
