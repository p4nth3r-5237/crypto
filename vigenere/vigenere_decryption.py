 # Pi = (Ci-Ki) mod 26  where Pi=Plain text, Ci=Cipher text and Ki=Key
# It is like caesar cipher but key is different for every chracter
# ex- P=Anoop  K=abc   so P len is 5 but k len is 3 so repeat key and make it equal
plain_text=input("Enter Cipher: ")
shift_key=input("Enter key: ")
temp_key=[]
count=0
for i in range(len(plain_text)):
    if len(plain_text) <= len(temp_key):
        break
    elif (ord(plain_text[i]) >= 97 and ord(plain_text[i]) <=122) or (ord(plain_text[i]) >= 65 and ord(plain_text[i]) <=90):
        temp_key+=shift_key[count%len(shift_key)]
        count+=1
    else:
        temp_key+=plain_text[i]

shift_key=''.join(temp_key)
num=97
for (shift,i) in zip(shift_key,plain_text):
    if ord(i) >= 97 and ord(i) <=122 :
        var=((ord(i)-97)-(ord(shift)-97)) % 26
        alpha=97
        for ch in range(0,26):
            if var == ch:
                print(chr(alpha), end="")
            else:
                alpha+=1
    elif ord(i) >= 65 and ord(i) <=90 :
        var=((ord(i)-65)-(ord(shift)-65)) % 26
        alpha=65
        for ch in range(0,26):
            if var == ch:
                print(chr(alpha), end="")
            else:
                alpha+=1
    else:
        print(i, end="")
print()
