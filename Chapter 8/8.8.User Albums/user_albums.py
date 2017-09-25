'''
8-8. User Albums: Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album’s artist and title. Once you have that
information, call make_album() with the user’s input and print the dictionary
that’s created. Be sure to include a quit value in the while loop.
'''


def make_album(artist_name , album_title , number=""):
    dic_of_album = {"artist_name": artist_name ,
                    "album_title": album_title,
                    }
    if number:
        dic_of_album["number"] = number
    return dic_of_album


while True:
    artist_n = input("What is your artist name? "
                    "\nWrite 'q' for quit: ")

    if artist_n == "q":
        break

    album_t = input("\nWhat is album title?"
                    "\nWrite 'q' for quit: ")
    if album_t =="q":
        break
    my_album = make_album(artist_n.title(),album_t.title())
    print(my_album)

