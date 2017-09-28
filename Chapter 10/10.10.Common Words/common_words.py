'''
10-10. Common Words: Visit Project Gutenberg (http://gutenberg.org/ )
and find a few texts you’d like to analyze. Download the text files for these
works, or copy the raw text from your browser into a text file on your
computer.
You can use the count() method to find out how many times a word or
phrase appears in a string. For example, the following code counts the number
of times 'row' appears in a string:
line = "Row, row, row your boat"
line.count('row')
2
>line.lower().count('row')
3
Notice that converting the string to lowercase using lower() catches
all appearances of the word you’re looking for, regardless of how it’s
formatted.
Write a program that reads the files you found at Project Gutenberg and
determines how many times the word 'the' appears in each text.
'''

book1 = "Hackers, Heroes of the Computer Revolution.txt"
book2 = "Memory.txt"

def count_words(book,word):
    """ count word in book
    :param book: choose book to open
    :param word: choose word for search in file
    :return: how many argument word occur in book
    """
    with open(book, "r") as content:
        book_content = content.read().lower().count(word.lower())
        print(book + " contain " + str(book_content) + " '" + word +"' word")

# counting word "the"
count_words(book1,"the")
count_words(book2,"the")

# counting word "often"
count_words(book1,"often")
count_words(book2,"often")