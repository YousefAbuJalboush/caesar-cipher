from caesar_cipher import __version__

from caesar_cipher.caesar_cipher import *
import random

#######################################################

def test_version():
    assert __version__ == '0.1.0'

#######################################################

def test_encrypt():
    plain_text = "My Name is Yousef Abu-Jalboush. $ - % _ @ * # ^ Test"
    key = 13
    actual = encrypt( plain_text, key )
    expected = "Zl Anzr vf Lbhfrs Noh-Wnyobhfu. $ - % _ @ * # ^ Grfg"
    assert actual == expected

#######################################################

def test_decrypt():
    encrypted_text = "Zl Anzr vf Lbhfrs Noh-Wnyobhfu. $ - % _ @ * # ^ Grfg"
    key = 13
    actual = decrypt( encrypted_text, key )
    expected = "My Name is Yousef Abu-Jalboush. $ - % _ @ * # ^ Test"
    assert actual == expected

#######################################################

def test_both_encrypt_and_decrypt():
    plain_text = "It was the best of times, it was the worst of times."
    key = random.randint(1, 26)
    encrypt_text = encrypt( plain_text, key )
    actual = decrypt( encrypt_text, key )
    expected = plain_text
    assert actual == expected

#######################################################

def test_crack():
    plain_text = "It was the best of times, it was the worst of times."
    key = random.randint(1, 26)
    encrypt_text = encrypt( plain_text, key )

    actual = crack( encrypt_text )

    expected = plain_text

    assert actual == expected

#######################################################

def test_crack_not_50per_english_text():
    plain_text = "My Name is Yousef Abu-Jalboush. $ - % _ @ * # ^ Test"
    key = random.randint(1, 26)
    encrypt_text = encrypt( plain_text, key )

    actual = crack( encrypt_text )

    expected = "Not 50 percent English text."
    
    assert actual == expected

#######################################################
