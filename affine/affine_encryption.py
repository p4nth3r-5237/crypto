# (num+x)  mod 26  num=1,2,3,4....  x=plain_text

plain_text=input("Enter Plain Text: ")

a=3
b=2
for i  in plain_text:
    if ord(i) >= 97 and ord(i) <=122 :
        var=abs((a*(ord(i)-97)+b) % 26)
        var+=97
        if var > 122:
            print(chr((var-122)+97), end="")
        else:
            print(chr(var), end="")
    elif ord(i) >= 65 and ord(i) <=90 :
        var=abs((a*(ord(i)-65)+b) % 26)
        var+=65
        if var > 90:
            print(chr((var-90)+65), end="")
        else:
            print(chr(var), end="")
    else:
        print(i, end="")
