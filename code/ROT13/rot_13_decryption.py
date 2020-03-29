
word=input("Enter word: ")
for char in word:
    if((ord(char) >=65 and ord(char) <=90) or ( ord(char)>=97 and ord(char)<=122)):
        # below if is for big alphabet
        if(ord(char) >=65 and ord(char) <=90):
            ascii_=ord(char)+13
            if(ascii_>=65 and ascii_<=90):
                print(chr(ascii_),end="")
            else:
                ascii_change=64+(ascii_-90)
                print(chr(ascii_change),end="")
        else:
            # small alphabet
            small_ascii=ord(char)+13
            if(small_ascii>=90 and small_ascii<=122):
                print(chr(small_ascii),end="")
            else:
                small_ascii_change=96+(small_ascii-122)
                print(chr(small_ascii_change),end="")
    else:
        print(char,end="")
