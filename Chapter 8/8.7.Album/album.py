'''
8-7. Album: Write a function called make_album() that builds a dictionary
describing a music album. The function should take in an artist name and an
album title, and it should return a dictionary containing these two pieces of
information. Use the function to make three dictionaries representing different
albums. Print each return value to show that the dictionaries are storing the
album information correctly.
Add an optional parameter to make_album() that allows you to store the
number of tracks on an album. If the calling line includes a value for the number
of tracks, add that value to the album’s dictionary. Make at least one new
function call that includes the number of tracks on an album.
'''


def make_album(artist_name , album_title , number=""):
    dic_of_album = {"artist_name": artist_name.title() ,
                    "album_title": album_title.title(),
                    }
    if number:
        dic_of_album["number"] = number
    return dic_of_album
my_album = make_album("Artist1","Album1")
print(my_album)

#make three dictionaries
adam_album = make_album("someone1","nice song")
david_album = make_album("Peter Song","my song")
olivia_album = make_album("Moron Wandy","great opportunity")

#make dictionary include the number of tracks:
john_album = make_album("John Rondon","oh Johny",15)

print("\n" , adam_album , "\n" , david_album , "\n" , olivia_album)
print("\n", john_album)