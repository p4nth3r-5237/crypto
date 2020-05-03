# Encryption  e(x) = (x+k) mod 26
# character+key in integer add it and take modulus and then make character

plain_text=input("Enter Plain Text: ")
print("Shift by\t\t","Encrypted data")
for shift in range(27):
    num=97
    print("---------------------------\n",shift,":\t\t", end="")
    for i  in plain_text:
        if ord(i) >= 97 and ord(i) <=122 :
            var=((ord(i)-97)+shift) % 26
            alpha=97
            for ch in range(0,26):
                if var == ch:
                    print(chr(alpha), end="")
                else:
                    alpha+=1
        elif ord(i) >= 65 and ord(i) <=90 :
            var=((ord(i)-65)+shift) % 26
            alpha=65
            for ch in range(0,26):
                if var == ch:
                    print(chr(alpha), end="")
                else:
                    alpha+=1
        else:
            print(i, end="")
    print()
