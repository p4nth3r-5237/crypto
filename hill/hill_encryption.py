from sympy.crypto.crypto import encipher_hill
from sympy import Matrix

plain=input('Enter plain text: ')
key = Matrix([[1, 2], [3, 5]])
print(encipher_hill(plain, key))
