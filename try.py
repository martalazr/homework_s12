import requests
import string

def save_book(url):
    r = requests.get(url)
    return r.text

platero = "https://www.gutenberg.org/cache/epub/39209/pg39209.txt"
buscon = "https://www.gutenberg.org/cache/epub/32315/pg32315.txt"
#------------------------------ejemplo y funciones----------------------------
#Book uno es Platero y yo
book_uno = save_book(platero)

#Book dos es El buscón de Quevedo
book_dos = save_book(buscon)

chars = ".¡!()[],;:¿?"

#Primero eliminamos la puntuación y otros símbolos que puedan molestar
#Luego lo ponemos todo en minúsculas con lower()
#Luego creamos una lista que contiene todas las palabras separadas con split()
words_uno = book_uno.translate(str.maketrans('', '', chars)).lower().split()
words_dos = book_dos.translate(str.maketrans('', '', chars)).lower().split()


#con esto podemos empezar a crear la función que cuenta las palabras únicaas
#y la función que calcula el ratio

def unic(lista):
    cnt = 0
    for word in lista:
        tmp = lista
        tmp.remove(word)
        if not(word in tmp):
            cnt += 1
    return cnt

def ratio(lista):
    return (unic(lista)/(len(lista)))
#---------------------------------------------------------------------------
#Ya podemos hacer la función que compara los dos

def compare(url_uno, url_dos):
    b_uno = save_book(url_uno)
    b_dos = save_book(url_dos)
    w_uno = b_uno.translate(str.maketrans('', '', chars)).lower().split()
    w_dos = b_dos.translate(str.maketrans('', '', chars)).lower().split()
    #unique words
    if (unic(w_uno) < unic(w_dos)):
        print("The second book has more unique words than the first one")
    elif (unic(w_uno) > unic(w_dos)):
        print("The first book has more unique words than the second one")
    else:
        print ("The two books have the same amount of unique words")

    #ratio
    if (ratio(w_uno) < ratio(w_dos)):
        print("The second book has a higher ratio of unique to total words than the first one")
    elif (ratio(w_uno) > ratio(w_dos)):
        print("The first book has a higher ratio of unique to total words than the second one")
        #muy poco probable
    else:
        print ("The two books have the same ratio of unique to total words")
