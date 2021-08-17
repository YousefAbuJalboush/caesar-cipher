import nltk
import re
from nltk.corpus import words, names
import random

########################################################################

nltk.download('names', quiet=True)
nltk.download('words', quiet=True)
word_list = words.words()
name_list = names.words()

########################################################################

def encrypt( plain_text, key ):

    encrypted = ""

    for letter in plain_text:

        if letter.isupper():  

            letter_num = ord( letter ) - ord( 'A' )
            letter_shift = ( letter_num + key ) % 26 + ord( 'A' )
            new_letter = chr( letter_shift )
            encrypted = encrypted + new_letter

        elif letter.islower(): 

            letter_num = ord( letter ) - ord( 'a' )
            letter_shift = ( letter_num + key ) % 26 + ord( 'a' )
            new_letter = chr( letter_shift )
            encrypted = encrypted + new_letter

        elif letter.isdigit():

            new_numb = ( int( letter ) + key ) % 10
            encrypted = encrypted + str( new_numb )

        else:

            encrypted = encrypted + letter

    return encrypted

########################################################################

def decrypt( encrypted, key ):
    return encrypt( encrypted, -key )

########################################################################
########################################################################

if __name__ == "__main__":

    plain_text = "My Name is Yousef Abu-Jalboush. $ - % _ @ * # ^ Test"
    key = random.randint(1, 26)
    # key = 13
    encrypted_text = encrypt( plain_text, key )
    decrypted_text = decrypt( encrypted_text, key )

    print( encrypted_text )
    print( decrypted_text )

########################################################################
########################################################################
