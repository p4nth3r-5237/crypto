import pybase64


data=input("Enter text: ")
data_byte=data.encode('utf-8')
encoded_data=pybase64.b64decode(data_byte)
print(encoded_data.decode('utf-8'))
