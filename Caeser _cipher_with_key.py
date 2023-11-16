 
# Caeser _cipher_with_key.py
#
# Description: A program that encrypts data according to Caeser cipher with key. NOT CASE-SENSTIVE (add description?)
#
# Author: Chaitanya Mittal
# Date: 2023-11-16 11:32:05.792395


"""basic idea:
-define function
-make a list of alphabets(lowercase is ok since encryption is case-insensitive)
- get the key 'values'
-iterate through string : 
    if character is alphabet, then get alphabet index and: 
            add key value. if =< 26 no problem; if > 26, then - 26. so for that we can use remainder when 
            divided by 26, i.e., (x + 13) % 26
-store output and return it
"""
"""Execution:
-get input
-call function
-give output"""

def caeser_encrypt(string,key):
    string = list(string.lower()) # convert to lowercase list
    key = key.lower() # convert to lowercase string

    lst_key = list() # initialize empty list
    alphabet = list("abcdefghijklmnopqrstuvwxyz") # create list of alphabets

    for character in key:
        lst_key.append(alphabet.index(character)) # store indices of characters in key

    key_count = 0 # initialize count for key characters

    # Note: here we shift only if character is a letter. if it is a number/ space, then we dont shift it.
    #       if we directly iterate the key in for loop, then it will progress even for non-alphabetic characters.
    #       to avaiod that, we initialise a key_count and add update it only if the character is alphabet.

    encrypted_text = "" #intitialize empty string to hold result
    for i in range(len(string)):
        if string[i].isalpha(): # if character is a letter
            # shift character based on key character
            if i % len(lst_key) == 0:
                string[i] = alphabet[(alphabet.index(string[i]) + lst_key[key_count]) % len(alphabet)] 
            elif i % len(lst_key) == 1:
                string[i] = alphabet[(alphabet.index(string[i]) + lst_key[key_count]) % len(alphabet)] 
            else:
                string[i] = alphabet[(alphabet.index(string[i]) + lst_key[key_count]) % len(alphabet)] 
            key_count = (key_count + 1)% 3 # update count for key characters
        encrypted_text += string[i]
    
    return encrypted_text

#getting input
string = input("String to encrypt: ")
key = input("Key to use: ")

#calling function and printing output
print(caeser_encrypt(string,key))