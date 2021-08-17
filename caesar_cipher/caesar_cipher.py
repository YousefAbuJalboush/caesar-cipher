import nltk
import re
from nltk.corpus import words, names
import random

from nltk.util import pr

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
# Dario Code for Count Words
def count_words(text):
    candidate_words = text.split()
    word_count = 0
    for candidate in candidate_words:
        word = re.sub(r'[^A-Za-z]+','', candidate)
        if word.lower() in word_list or word in name_list:
            word_count += 1
        else:
            pass
    return word_count

##############################

def crack( encrypted ):
    decrypt_word = ''

    for key in range(26):

        expected = decrypt(encrypted, key)
        # print(expected)
        word_count = count_words(expected)
        percentage = int(word_count / len(expected.split()) * 100)

        if percentage > 50:
            decrypt_word = expected

    if not decrypt_word :
        decrypt_word = "Not 50 percent English text."

    return decrypt_word

########################################################################
########################################################################

if __name__ == "__main__":

    # plain_text = "My Name is Yousef Abu-Jalboush. $ - % _ @ * # ^ Test"
    plain_text = "It was the best of times, it was the worst of times."
    key = random.randint(1, 26)
    # key = 13
    encrypted_text = encrypt( plain_text, key )
    decrypted_text = decrypt( encrypted_text, key )
    
    print( f'Plain Text : {plain_text}' )
    print( f'Encrypt    : {encrypted_text}' )
    print( f'Decrypt    : {decrypted_text}' )

    crack_text = crack(encrypted_text)
    print( f'Crack      : {crack_text}' )

########################################################################
########################################################################
