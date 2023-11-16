 
#ROT13_encoder.py
#
#An encoder that uses ROT13 algorithm to encode/decode method. Assignment 2
#
#Author: Chaitanya Mittal
#Date: 2023-10-05 12:18:38.326213

"""Basic idea:
- define function
- get set of aplhabets, both lowercase and uppercase.
- <formula> used: manipulate indexes of list of alphabets(upper and lower separate),
                add 13. if =< 26 no problem; if > 26, then - 26. so for that we can use remainder when 
                divided by 26, i.e., (x + 13) % 26 
- store and return result
"""
"""Execution:
-get input
-call function
- give output
continue this till the time empty string not entered """

import string 
import time

# printing after "thinking" (just a cool spy-ish effect)
def prt(x,ending = " "):
    time.sleep(1)
    for char in x:
        print(char, end = "", flush=True)
        time.sleep(0.05)
    if ending != "":
        print()

# taking input        
def takeinput():
    return input(">>> ")


#define a function that will both decrypt and encrypt as bot-13 will function same both ways (Wiki explanation)
def ROT(msg):
    answer = ""    #empty string to store answer
    #list of lowercase alphabets  
    lower = list(string.ascii_lowercase)  
    #list of uppercase alphabets  
    upper = list(string.ascii_uppercase)  
    
    #for loop to traverse each character in msg
    for char in msg:
        if char.isalpha(): #checking whether character is an alphabet or not
            #lowercase
            if char.islower():  
                index = int(lower.index(char))  #getting index of the char
                new_index = (index + 13) % 26  #apply <formula>
                new_char = lower[new_index]  #new character
            #uppercase
            else:              
                index = int(upper.index(char))  #getting index of the char
                new_index = (index + 13) % 26  #apply <formula>
                new_char = upper[new_index] #new character
            char = new_char  #assigning char the new value (new) to do line 44
        answer += (char) #add char [new or unchanged(if not alphabhet)] to empty string
    return answer


#intro
prt("Welcome to Code Handling Program")

#a variable to set condition for repeating while loop
continuing = True
#while loop to continue getting input
while continuing:
    prt("Please, enter a message to encrypt/decrypt or enter an empty string to exit the program: ")
    msg = takeinput()
    if msg == "":
        continuing = False #breaking from loop when "" entered.
    else:
        #printing output
        prt("Output = ", "")
        prt(ROT(msg),"")
    print()

#end-ing of the program
prt("Exiting....")
prt("Bye see you again :)")
