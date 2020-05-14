'''This script uses a dictionary instead of 'chr()' & 'ord()' function'''

'''
Dictionary to map plaintext with ciphertext
(key:value) => (plaintext:ciphertext)
This script uses the 26 letter baconian cipher
in which I,J & U,V have distinct patterns
'''
lookup = {'A':'aaaaa', 'B':'aaaab', 'C':'aaaba', 'D':'aaabb','E':'aabaa',
    'F':'aabab', 'G':'aabba', 'H':'aabbb', 'I':'abaaa', 'J':'abaab',
    'K':'abaab', 'L':'ababa', 'M':'ababb', 'N':'abbaa', 'O':'abbab',
    'P':'abbba', 'Q':'abbbb', 'R':'baaaa', 'S':'baaab', 'T':'baaba',
    'U':'babaa', 'V':'babab', 'W':'babaa', 'X':'babab', 'Y':'babba',
    'Z':'babbb'}
#Function to encrypt the string according to the cipher provided
def encrypt(message):
    cipher = ''
    for letter in message:
        #checks for space
        if(letter != ' '):
            #adds the ciphertext corresponding to the plaintext from the dictionary
            cipher += lookup[letter]
        else:
            #adds space
            cipher += ' '

    return cipher

#Function to decrypt the string according to the cipher provided
def decrypt(message):
    decipher = ''
    i = 0

    #emulating a do-while loop

plain=input('Enter plain text: ')
print(encrypt(plain))
