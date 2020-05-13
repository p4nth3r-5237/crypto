from sympy.crypto.crypto import  decipher_hill
from sympy import Matrix

cipher=input('Enter cipher: ')
key = Matrix([[1, 2], [3, 5]])
print(decipher_hill(cipher, key))
