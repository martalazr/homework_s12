# Compare 2 books from project gutenberg.
# Which one has more unique words? Which one has the ratio of unique to total words higher?

import requests
import string

def save_book(url):
    r = requests.get(url)
    return r.text

# The two books are Platero y yo and El buscón de Quevedo
platero = "https://www.gutenberg.org/cache/epub/39209/pg39209.txt"
buscon = "https://www.gutenberg.org/cache/epub/32315/pg32315.txt"

book_one = save_book(platero)
book_two = save_book(buscon)

chars = ".¡!()[],;:¿?"
# We firstly eliminate punctuation and other symbols that can bother us
# We put every character in lower case thanks to lower()
# Then we create a list containing all the words splitted with split()
words_one = book_one.translate(str.maketrans('', '', chars)).lower().split()
words_two = book_two.translate(str.maketrans('', '', chars)).lower().split()

# We can create the function that counts unique words
def unique(list):
    cnt = 0
    for word in list:
        tmp = list
        tmp.remove(word)
        if not(word in tmp):
            cnt += 1
        return cnt

# We can create the function that calculates the ratio
def ratio(list):
    return (unique(list)/(len(list)))

# We can create the function that compares the two books
def compare(url_one, url_two):
    b_one = save_book(url_one)
    b_two = save_book(url_two)
    w_one = b_one.translate(str.maketrans('', '', chars)).lower().split()
    w_two = b_two.translate(str.maketrans('', '', chars)).lower().split()

    # Unique words
    if (unique(w_one) < unique(w_two)):
        print("The second book has more unique words than the first one")
    elif (unique(w_one) > unique(w_two)):
        print("The first book has more unique words than the second one")
    else:
        print("The two books have the same amount of unique words")

    # Ratio
    if (ratio(w_one) < ratio(w_two)):
        print("The second book has a higher ratio of unique to total words that the first one")
    elif (ratio(w_one) > ratio(w_two)):
        print("The first book has a higher ratio of unique to total words than the second one")
    else:
        print("The two books have the same ratio of unique to total words")
